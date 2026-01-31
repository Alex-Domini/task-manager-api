from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.db.deps import get_db
from app.models import Task, User
from app.schemas.task import TaskCreate, TaskRead

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=TaskRead)
def create_task(task_in: TaskCreate,
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user),):
    task = Task(title = task_in.title,
                user_id = current_user.id,)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task



@router.get("/", response_model=List[TaskRead])
def get_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Task).filter(Task.user_id == current_user.id).all()


@router.delete("/{id}", response_model=TaskRead)
def del_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id==task_id).first()
    if not db_task:
        return None
    db.delete(db_task)
    db.commit()
    return db_task
