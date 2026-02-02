from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.db.deps import get_db
from app.models import Task, User
from app.schemas.task import TaskCreate, TaskRead, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=TaskRead)
def create_task(task_in: TaskCreate,
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user),):
    task = Task(title=task_in.title,
                user_id=current_user.id, )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.get("/", response_model=List[TaskRead])
def get_tasks(db: Session = Depends(get_db),
              current_user: User = Depends(get_current_user)):
    return db.query(Task).filter(Task.user_id == current_user.id).all()


@router.patch("/{task_id}", response_model=TaskRead)
def update_task(task_id: int,
                task_in: TaskUpdate,
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user), ):
    db_task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()

    if db_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Task not found")

    if task_in.title is not None:
        db_task.title = task_in.title

    if task_in.is_completed is not None:
        db_task.is_completed = task_in.is_completed
    db.commit()
    db.refresh(db_task)
    return db_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_task = (db.query(Task)
               .filter(Task.id == task_id,
                       Task.user_id == current_user.id).first())

    if db_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    db.delete(db_task)
    db.commit()
