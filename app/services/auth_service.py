from sqlalchemy.orm import Session

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)

from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class AuthService:

    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def register(self, user: UserCreate):

        existing = self.repo.get_by_email(user.email)

        if existing:
            raise ValueError("Email already exists")

        hashed = hash_password(user.password)

        return self.repo.create(
            email=user.email,
            hashed_password=hashed,
        )

    def login(
        self,
        email: str,
        password: str,
    ):

        db_user = self.repo.get_by_email(email)

        if not db_user:
            raise ValueError("Invalid credentials")

        if not verify_password(
            password,
            db_user.hashed_password,
        ):
            raise ValueError("Invalid credentials")

        token = create_access_token(
            subject=str(db_user.id)
        )

        return token