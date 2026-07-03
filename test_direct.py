import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "lib"))
sys.path.insert(0, str(Path(__file__).parent))

print("Imports...")
from app import models, schemas, crud
from app.database import SessionLocal, engine
from sqlalchemy.orm import Session
from app.security import hash_password

print("Creating DB...")
models.Base.metadata.create_all(bind=engine)

print("Creating session...")
db = SessionLocal()

print("Testing create_user...")
test_user = schemas.UserCreate(
    full_name="Direct Test",
    email="direct@test.com",
    password="test123"
)
try:
    user = crud.create_user(db, test_user)
    print(f"SUCCESS! Created user: {user}")
except Exception as e:
    print(f"ERROR: {type(e).__name__}: {e}")
    import traceback
    print(traceback.format_exc())
finally:
    db.close()
