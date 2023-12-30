import os.path
import secrets
from fastapi import FastAPI, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import crud
import models
import schemas
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import auth

app = FastAPI()

origins = [
    "http://localhost",
    "https://illustrious-daifuku-1e9cbe.netlify.app",
    "https://localhost:8080",
    "http://127.0.0.1:5500",
    "https://localhost.tiangolo.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db_session():
    db = SessionLocal()
    try:  ## probeerd de sessie aan te maken en door te geven als dat niet lukt vangt hij het op zodat de app niet crashed
        yield db
    finally:
        db.close()




@app.post("/token", tags=["Post"])
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db_session)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}



@app.get("/users/me", response_model=schemas.User, tags=["Get"])
def read_users_me(db: Session = Depends(get_db_session), token: str = Depends(oauth2_scheme)):
    current_user = auth.get_current_active_user(db, token)
    return current_user


@app.post("/users/", response_model=schemas.User, tags=["Post"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db_session)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


# Endpoint to get all films
@app.get("/films", response_model=schemas.FilmListOut, tags=["Get"])
def read_films(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    films = crud.get_films(db, skip=skip, limit=limit)
    if not films:
        raise HTTPException(status_code=404, detail="No films found")
    return {"films": films}


# Endpoint to create a film
@app.post("/films", response_model=schemas.FilmOut, tags=["Post"])
def create_film(film: schemas.FilmCreate, db: Session = Depends(get_db_session)):
    db_film = crud.create_film(db, film)
    if db_film is None:
        raise HTTPException(status_code=400, detail="Film already exist!")
    return db_film


# Endpoint to delete all films


# Endpoint to delete one film
@app.delete("/films/{film_id}", tags=["delete"])
def delete_film(film_id: int, db: Session = Depends(get_db_session)):
    film = crud.get_film_by_id(db, film_id=film_id, )
    if not film:
        raise HTTPException(status_code=404, detail="Film not Found")
    crud.delete_film(db, film_id)
    return {"message": "Film was succesfully deleted!"}


@app.get("/persons/", tags=["Get"])
def read_persons_by_name(name: str = Query(None, description="Name of the person to search for"),
                         db: Session = Depends(get_db_session)):
    if name:
        persons = crud.get_persons_by_name(db, name)
    else:
        persons = crud.get_persons(db)

    if not persons:
        raise HTTPException(status_code=404, detail="No persons found")

    return {"persons": persons}


# Endpoint to create a person
@app.post("/persons", response_model=schemas.PersonOut, tags=["Post"])
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db_session)):
    db_person = crud.create_person(db, person)
    if db_person is None:
        raise HTTPException(status_code=400, detail="Person already exists")
    return db_person


# Endpoint to get all starships
@app.get("/starships", response_model=schemas.StarshipListOut, tags=["Get"])
def read_starships(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    starships = crud.get_starships(db, skip=skip, limit=limit)
    if not starships:
        raise HTTPException(status_code=404, detail="No starships found")
    return {"starships": starships}


# Endpoint to create a starship
@app.post("/starships", response_model=schemas.StarshipOut, tags=["Post"])
def create_starship(starship: schemas.StarshipCreate, db: Session = Depends(get_db_session)):
    db_starship = crud.create_starship(db, starship)
    if db_starship is None:
        raise HTTPException(status_code=400, detail="Starship already exists")
    return db_starship


@app.get("/films/all_with_characters_starships", tags=["Get"])
def get_all_films_with_characters_starships(db: Session = Depends(get_db_session), token: str = Depends(oauth2_scheme)):
    films = db.query(models.Film).all()
    film_data = []

    for film in films:
        characters, starships = crud.get_persons_and_starships_in_film(db, film.id)
        film_info = {
            "film_id": film.id,
            "title": film.title,
            "release_year": film.release_year,
            "characters": characters,
            "starships": starships
        }
        film_data.append(film_info)

    return film_data

@app.put("/films/{film_id}", tags=["Put"])
def update_film_title(film_id: int, film_update: schemas.FilmUpdate):
    db = SessionLocal()
    film = db.query(models.Film).filter(models.Film.id == film_id).first()

    if film:
        film.title = film_update.title
        db.commit()
        db.refresh(film)
        return {"message": "Titel bijgewerkt"}
    else:
        raise HTTPException(status_code=404, detail="Film niet gevonden")


if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)


