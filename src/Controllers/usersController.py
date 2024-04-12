from sqlalchemy.orm import Session
from Model import schemes, models
from sqlalchemy.orm.exc import NoResultFound



#LISTAR UN REGISTRO POR ID
def getUserCredentials(db: Session, username: str, password: str):
    try:
        result = db.query(models.User).filter((models.User.username == username) and (models.User.password == password)).first()
        if not result:
            raise NoResultFound('User not found')
        return result
    except:
        raise