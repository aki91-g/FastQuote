#!/usr/bin/env python3

# quote_api_project/
# ├── main.py                  # Entry point
# ├── models.py                # SQLAlchemy models
# ├── schemas.py               # Pydantic schemas
# ├── crud.py                  # DB interaction functions
# ├── db.py                    # DB connection setup
# ├── routers/
# │   └── quotes.py            # Routes for /quotes
# ├── __init__.py              # Makes it a Python package
# └── .env                     # Environment variables (optional)

##
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
import models
import schemas
from db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/quotes/ramdom/unseen", response_model=schemas.QuoteRead)
def read_quote_ramdom_unseen(user_id: int, db: Session = Depends(get_db)):
    seen_ids = db.execute(
        "SELECT quote_id FROM user_seen_quotes WHERE user_id = :user_id",
        {"user_id": user_id}
    ).scalars().all()

    quote = (
        db.query(models.Quote)
        .filter(~models.Quote.id.in_(seen_ids))
        .order_by(func.random())
        .first()
    )

    if not quote:
        raise HTTPException(status_code=404, detail="No unseen quotes left for this user.")

    db.execute(
        "INSERT INTO user_seen_quotes (user_id, quote_id) VALUES (:user_id, :quote_id)",
        {"user_id": user_id, "quote_id": quote.id}
    )
    db.commit()

    return quote