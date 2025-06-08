from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from sqlalchemy.orm import Session
import models 
import schema
from db import get_db


router = APIRouter()

@router.get("/",status_code=status.HTTP_200_OK, response_model=List[schema.PostResponse])
async def get_all_posts(db: Session = Depends(get_db)):
    post = db.query(models.Post).all()
    return post

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=List[schema.PostResponse])
async def post_created(post_input : schema.CreatePost, db : Session = Depends(get_db)):
    new_post = models.Post(**post_input.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return [new_post]

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schema.PostResponse)
async def get_one_post(id: int, db: Session = Depends(get_db)):
    id_post = db.query(models.Post).filter(models.Post.id == id).first()
    if id_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id: {id} you requested for does not exist")
    return id_post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delet_a_post(id: int, db: Session= Depends(get_db)):
    deleted_post = db.query(models.Post).filter(models.Post.id == id)

    if deleted_post.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {id} you requested for does not exist ")

    deleted_post.delete(synchronize_session=False)
    db.commit()


@router.put("/posts/{id}", response_model=schema.PostResponse)
async def update_a_post(update_post: schema.PostBase, id: int, db: Session = Depends(get_db)):
    updated_post = db.query(models.Post).filter(models.Post.id == id)
    if updated_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The id:{id} does not exist")
    updated_post.update(update_post.dict(), synchronize_session=False)
    db.commit()

    return updated_post.first()