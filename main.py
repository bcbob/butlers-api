from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Branch, Order
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Butler's Pizza API is alive!"}

@app.get("/branches")
def get_branches(db: Session = Depends(get_db)):
    branches = db.query(Branch).all()
    return branches

@app.get("/branches/{branch_id}/kitchen")
def get_kitchen_orders(branch_id: int, db: Session = Depends(get_db)):
    branch = db.query(Branch).filter(Branch.id == branch_id).first()
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")
    
    orders = db.query(Order).filter(
        Order.branch_id == branch_id,
        Order.drivedat_no == 0
    ).order_by(Order.order_time).all()
    
    return {
        "branch": branch.name,
        "orders_in_kitchen": len(orders),
        "orders": [
            {
                "id": o.id,
                "customer_name": o.customer_name,
                "order_time": o.order_time,
                "type": "Collection" if o.collect_flag == "Y" else "Delivery",
                "drivedat_no": o.drivedat_no
            }
            for o in orders
        ]
    }