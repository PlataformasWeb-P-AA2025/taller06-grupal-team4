# Presentar los lenguajes de cada país.
from sqlalchemy.orm import sessionmaker
from crear_base import Pais
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).all()

for p in paises:
    print(f"{p.nombre}: {p.lenguajes}")
