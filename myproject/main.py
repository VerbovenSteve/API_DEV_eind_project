import os.path
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import crud
import models
import schemas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1:8000",
    "https://main--illustrious-daifuku-1e9cbe.netlify.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db_session():
    db = SessionLocal()
    try:  ## probeerd de sessie aan te maken en door te geven als dat niet lukt vangt hij het op zodat de app niet crashed
        yield db
    finally:
        db.close()


# Endpoint to get all films
@app.get("/films", response_model=schemas.FilmListOut)
def read_films(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    films = crud.get_films(db, skip=skip, limit=limit)
    if not films:
        raise HTTPException(status_code=404, detail="No films found")
    return {"films": films}



# Endpoint to create a film
@app.post("/films", response_model=schemas.FilmOut)
def create_film(film: schemas.FilmCreate, db: Session = Depends(get_db_session)):
    db_film = crud.create_film(db, film)
    if db_film is None:
        raise HTTPException(status_code=400, detail="Film already exist!")
    return db_film


# Endpoint to delete all films
@app.delete("/films/")
def delete_films(db: Session = Depends(get_db_session)):
    result = crud.delete_films(db)
    if result:
        raise HTTPException(status_code=500, detail="Failed to delete films")
    return {"message": "All films deleted"}


# Endpoint to delete one film
@app.delete("/films/{film_id}")
def delete_film(film_id: int, db: Session = Depends(get_db_session)):
    film = crud.get_film_by_id(db, film_id=film_id)
    if not film:
        raise HTTPException(status_code=404, detail="Film not Found")
    crud.delete_film(db, film_id)
    return {"message": "Film was succesfully deleted!"}


@app.get("/persons/")
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
@app.post("/persons", response_model=schemas.PersonOut)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db_session)):
    db_person = crud.create_person(db, person)
    if db_person is None:
        raise HTTPException(status_code=400, detail="Person already exists")
    return db_person


# Endpoint to delete all persons
@app.delete("/persons")
def delete_persons(db: Session = Depends(get_db_session)):
    result = crud.delete_persons(db)
    if result:
        raise HTTPException(status_code=400, detail="Failed to delete persons")
    return {"message": "All persons deleted"}


# Endpoint to get all starships
@app.get("/starships", response_model=schemas.StarshipListOut)
def read_starships(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    starships = crud.get_starships(db, skip=skip, limit=limit)
    if not starships:
        raise HTTPException(status_code=404, detail="No starships found")
    return {"starships": starships}


# Endpoint to create a starship
@app.post("/starships", response_model=schemas.StarshipOut)
def create_starship(starship: schemas.StarshipCreate, db: Session = Depends(get_db_session)):
    db_starship = crud.create_starship(db, starship)
    if db_starship is None:
        raise HTTPException(status_code=400, detail="Starship already exists")
    return db_starship


# Endpoint to delete all starships
@app.delete("/starships")
def delete_starships(db: Session = Depends(get_db_session)):
    result = crud.delete_starships(db)
    if result:
        raise HTTPException(status_code=500, detail="Failed to delete starships")
    return {"message": "All starships deleted"}


@app.get("/films/all_with_characters_starships")
def get_all_films_with_characters_starships(db: Session = Depends(get_db_session)):
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


if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)
