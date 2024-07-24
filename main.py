from fastapi import FastAPI, HTTPException, Depends
from models import ProductCreate, ProductRead, ProductUpdate
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base, get_db
import crud
from typing import List 

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/products/", response_model=ProductRead)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@app.get("/products/", response_model=List[ProductRead])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@app.get("/products/{product_id}", response_model=ProductRead)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return db_product

@app.put("/products/{product_id}", response_model=ProductRead)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return crud.update_product(db=db, product=product, product_id=product_id)

@app.delete("/products/{product_id}", response_model=ProductRead)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return crud.delete_product(db=db, product_id=product_id)
