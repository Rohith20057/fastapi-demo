from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session  # <--- FIXED: Added Session here
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

# Update this URL with your specific credentials
# Format: postgresql://<username>:<password>@<ip-address>/<hostname>
# SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi_v2.db"

# This is the 'engine' variable your main.py is looking for
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# This is the 'get_db' dependency used in your route
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# def init_db():
#     Base.metadata.create_all(bind=engine)
    
# if __name__ == "__main__":
#     init_db()

# Loop to ensure DB is ready before starting (Optional, but helpful)
# Loop to ensure DB is ready before starting (Optional, but helpful)
# while True:
#     try:
#         conn = psycopg2.connect(
#             host=settings.database_hostname, 
#             database=settings.database_name, 
#             user=settings.database_username, 
#             password=settings.database_password, 
#             cursor_factory=RealDictCursor
#         )
#         cursor = conn.cursor()
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)