from app import schemas, models, utils
from app.database import SessionLocal, engine

db = SessionLocal()
user_in = schemas.UserCreate(email="routertest@example.com", password="password123")

try:
    print("Hashing...")
    hash_password = utils.hash(user_in.password)
    print(f"Hash: {hash_password}")
    
    # Mutate pydantic model
    user_in.password = hash_password
    print(f"Mutated password: {user_in.password}")
    
    # Check duplicate
    existing = db.query(models.User).filter(models.User.email == user_in.email).first()
    if existing:
        db.delete(existing)
        db.commit()

    print("Creating model...")
    # NOTE: user_in.dict() might be deprecated
    new_user = models.User(**user_in.model_dump())
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    print(f"User created: {new_user.id}")
    
    # Logic from response_model
    try:
        resp = schemas.UserOut.model_validate(new_user)
        print("Response validation: SUCCESS")
        print(resp)
    except Exception as e:
        print(f"Response validation FAILED: {e}")
        import traceback
        traceback.print_exc()

except Exception as e:
    print(f"FAILED: {e}")
    import traceback
    traceback.print_exc()
finally:
    db.close()
