from fastapi import APIRouter, Depends, status, HTTPException

from app.core.security import hash_password
from app.db.deps import get_db
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserRead, UserCreate

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user_in.email).first()
    if existing_user:
        raise HTTPException(status_code=400,
                            detail="User with this email already exists")

    user = User(email=user_in.email,
                hashed_password=hash_password(user_in.password),
                )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user