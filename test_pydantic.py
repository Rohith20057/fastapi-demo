from app import models, schemas
from app.database import SessionLocal
from datetime import datetime

db = SessionLocal()
try:
    user = db.query(models.User).first()
    if user:
        print(f"User from DB: {user.email}, created_at: {user.created_at}, type: {type(user.created_at)}")

        try:
            user_out = schemas.UserOut.model_validate(user)
            print("Pydantic validation: SUCCESS")
            print(user_out)
        except Exception as e:
            print(f"Pydantic validation: FAILED - {e}")
    else:
        print("No user found in DB")
except Exception as e:
    print(f"DB Error: {e}")
finally:
    db.close()
