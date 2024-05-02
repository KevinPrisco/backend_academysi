from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from Model import schemes
from sqlalchemy.orm.exc import NoResultFound
from Database.Connection import get_db
from dependencies import get_current_user, get_token_scopes