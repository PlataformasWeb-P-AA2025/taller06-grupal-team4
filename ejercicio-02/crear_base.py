from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from configuracion import engine

Base = declarative_base()

class Pais(Base):
    __tablename__ = 'pais'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    capital = Column(String(200))
    continente = Column(String(200))
    dial = Column(String(200))
    geoname_id = Column(Integer)
    itu = Column(String(200))
    lenguajes = Column(String(200))
    independiente = Column(String(200))

    def __repr__(self):
        return f"Pais(nombre={self.nombre}, capital={self.capital}, continente={self.continente})"

Base.metadata.create_all(engine)
