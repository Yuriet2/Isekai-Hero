from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.database import Base, engine, SessionLocal
from backend.models import User, Hero

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Isekai RPG Backend")

# Dependencia DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create_hero/")
def create_hero(telegram_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if not user:
        user = User(telegram_id=telegram_id)
        db.add(user)
        db.commit()
        db.refresh(user)

    hero = Hero(user_id=user.id)
    db.add(hero)
    db.commit()
    db.refresh(hero)

    return {"msg": "Héroe creado", "hero": hero.__dict__}


@app.get("/get_hero/{telegram_id}")
def get_hero(telegram_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if not user:
        return {"error": "Usuario no encontrado"}

    hero = db.query(Hero).filter(Hero.user_id == user.id).first()
    if not hero:
        return {"error": "Héroe no encontrado"}

    return {"hero": hero.__dict__}
