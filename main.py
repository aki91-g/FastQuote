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
from fastapi import FastAPI

app = FastAPI()

@app.get("/quote")
def get_quote():
    return {"quote"}