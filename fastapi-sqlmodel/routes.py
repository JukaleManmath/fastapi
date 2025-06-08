from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from sqlmodel import Session, select
import models 
from db import get_session


router = APIRouter()

@router.get("/",status_code=status.HTTP_200_OK, response_model=List[models.PostResponse])
async def get_all_posts(db: Session = Depends(get_session)):
    posts = db.exec(select(models.Post)).all()
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=List[models.PostResponse])
async def post_created(post_input : models.PostCreate, db : Session = Depends(get_session)):
    new_post = models.Post(**post_input.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return [new_post]

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=models.PostResponse)
async def get_one_post(id: int, db: Session = Depends(get_session)):
    id_post = db.exec(select(models.Post).where(models.Post.id == id)).first()
    if id_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id: {id} you requested for does not exist")
    return id_post

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delet_a_post(id: int, db: Session= Depends(get_session)):
    deleted_post = db.exec(select(models.Post).where(models.Post.id == id)).first()

    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {id} you requested for does not exist ")

    db.delete(deleted_post)
    db.commit()
    return {"msg": "post deleted successfully"}


@router.put("/posts/{id}", response_model=models.PostResponse)
async def update_a_post(update_post: models.PostBase, id: int, db: Session = Depends(get_session)):
    updated_post = db.exec(select(models.Post).where(models.Post.id == id)).first()
    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The id:{id} does not exist")
    for key, value in update_post.dict().items():
        setattr(updated_post, key, value)
    db.add(updated_post)
    db.commit()
    db.refresh(updated_post)
    return updated_post