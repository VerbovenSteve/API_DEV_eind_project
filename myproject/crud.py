from sqlalchemy.orm import Session

import models
import schemas
from models import Film, Person, Starship
from schemas import FilmCreate, PersonCreate, StarshipCreate
import auth


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_films(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Film).offset(skip).limit(limit).all()


def get_film_by_id(db: Session, film_id: int):
    return db.query(Film).filter(Film.id == film_id).first()


def get_persons(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Person).offset(skip).limit(limit).all()


def get_persons_by_name(db: Session, name: str):
    return db.query(Person).filter(Person.name == name).all()


def get_starships(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Starship).offset(skip).limit(limit).all()


# CRUD operations for films
def create_film(db: Session, film: FilmCreate):
    existing_film = db.query(models.Film).filter(models.Film.title == film.title).first()
    if existing_film:
        return None
    db_film = Film(**film.dict())
    db.add(db_film)
    db.commit()
    db.refresh(db_film)
    return db_film


# CRUD operations for persons
def create_person(db: Session, person: PersonCreate):
    existing_person = db.query(models.Person).filter(models.Person.film_id == person.film_id,
                                                     models.Person.name == person.name).first()
    if existing_person:
        return None
    db_person = Person(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


# CRUD operations for starships
def create_starship(db: Session, starship: StarshipCreate):
    existing_starship = db.query(models.Starship).filter(models.Starship.film_id == starship.film_id,
                                                         models.Starship.name == starship.name).first()
    if existing_starship:
        return None
    db_starship = Starship(**starship.dict())
    db.add(db_starship)
    db.commit()
    db.refresh(db_starship)
    return db_starship


def delete_film(db: Session, film_id: int):
    film = get_film_by_id(db, film_id)
    if film:
        db.delete(film)
        db.commit()
        return True
    return False


def get_persons_and_starships_in_film(db: Session, film_id: int):
    film = db.query(models.Film).filter(models.Film.id == film_id).first()
    if film is None:
        return None

    persons = db.query(models.Person).filter(models.Person.film_id == film_id).all()
    starships = db.query(models.Starship).filter(models.Starship.film_id == film_id).all()

    return persons, starships


def get_characters_and_starships(self, db: Session):
    characters = db.query(Person).filter_by(film_id=self.id).all()
    starships = db.query(Starship).filter_by(film_id=self.id).all()
    return characters, starships
