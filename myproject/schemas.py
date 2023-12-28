# basemodel van response model  maar aangepast
from pydantic import BaseModel


# Film schemas
class FilmBaseIn(BaseModel):
    title: str  # in
    release_year: int  # in


class FilmCreate(FilmBaseIn):
    pass


class FilmOut(FilmBaseIn):
    id: int  # out

    class Config:
        orm_mode = True


class FilmListOut(BaseModel):
    films: list[FilmOut] = []  # out


# Person schemas
class PersonBaseIn(BaseModel):
    name: str  # in
    age: int  # in
    film_id: int  # in


class PersonCreate(PersonBaseIn):
    pass  # in


class PersonOut(PersonBaseIn):
    id: int  # out

    class Config:
        orm_mode = True


class PersonListOut(BaseModel):
    persons: list[PersonOut] = []  # out


# Starship schemas
class StarshipBaseIn(BaseModel):
    name: str  # in
    model: str  # in
    film_id: int  # in


class StarshipCreate(StarshipBaseIn):
    pass  # in


class StarshipOut(StarshipBaseIn):
    id: int  # out

    class Config:
        orm_mode = True


class StarshipListOut(BaseModel):
    starships: list[StarshipOut] = []  # out


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class FilmUpdate(BaseModel):
    title: str