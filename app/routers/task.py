from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.models import Task
from app.schemas.task import TaskCreate, TaskRead

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=TaskRead)
def create_task(task_in: TaskCreate, db: Session = Depends(get_db)):
    task = Task(title = task_in.title,
                user_id = task_in.user_id) # TODO: remove hardcoded user_id after auth
    db.add(task)
    db.commit()
    db.refresh(task)
    return task



@router.get("/", response_model=List[TaskRead])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).filter().all()


@router.delete("/{id}", response_model=TaskRead)
def del_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id==task_id).first()
    if not db_task:
        return None
    db.delete(db_task)
    db.commit()
    return db_task
