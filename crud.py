from sqlalchemy.orm import Session
from models import ProductCreate, ProductUpdate
from database import Product as DBProduct

def get_product(db: Session, product_id: int):
    return db.query(DBProduct).filter(DBProduct.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DBProduct).offset(skip).limit(limit).all()

def create_product(db: Session, product: ProductCreate):
    db_product = DBProduct(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product: ProductUpdate, product_id: int):
    db_product = get_product(db, product_id)
    if db_product is None:
        return None
    for key, value in product.dict().items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if db_product is None:
        return None
    db.delete(db_product)
    db.commit()
    return db_product
