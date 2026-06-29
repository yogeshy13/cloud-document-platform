from app.db.database import SessionLocal
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password

db = SessionLocal()

repo = UserRepository(db)

user = repo.create(
    email="admin@example.com",
    hashed_password=hash_password("Password123!")
)

print(user.id)
print(user.email)

db.close()