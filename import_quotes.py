import json
from db import SessionLocal
import models

def main():
    with open("data/quotes.JSON", "r") as file:
        quotes_data = json.load(file)
    db = SessionLocal()
    for quote in quotes_data:
        author_data = quote["author"]
        author = db.query(models.Author).filter_by(name=author_data["name"]).first()
        if not author: 
            author = models.Author(
                name=author_data["name"],
                birth_year=author_data.get("birth_year"),
                death_year=author_data.get("death_year"),
                bio=author_data.get("bio")
            )
            db.add(author)
            db.commit()
            db.refresh(author)
        
        quote_obj = models.Quote(
            text=quote["text"],
            author_id=author.id if author else None
        )
        db.add(quote_obj)
    db.commit()
    db.close()

if __name__ == "__main__":
    main()