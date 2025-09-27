from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./isekai.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class HeroDB(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    nivel = Column(Integer, default=1)
    experiencia = Column(Integer, default=0)
    fuerza = Column(Integer, default=5)
    defensa = Column(Integer, default=5)
    agilidad = Column(Integer, default=5)
    magia = Column(Integer, default=5)

Base.metadata.create_all(bind=engine)