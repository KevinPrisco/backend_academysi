from sqlalchemy.orm import Session
from sqlalchemy import select
from Model import schemes
from sqlalchemy.orm.exc import NoResultFound

from Services.Handlers.handler_functions import asignar_valores, getAllEntities