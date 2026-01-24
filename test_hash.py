from passlib.context import CryptContext

try:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed = pwd_context.hash("password123")
    print(f"Hash: {hashed}")
    verified = pwd_context.verify("password123", hashed)
    print(f"Verified: {verified}")
except Exception as e:
    print(f"Error: {e}")
