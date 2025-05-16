from sqlalchemy.orm import sessionmaker
from crear_base import Pais
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).filter(Pais.continente == 'NA')  # Norteamérica
paises = paises.union_all(session.query(Pais).filter(Pais.continente == 'SA'))  # Sudamérica

for p in paises:
    print(p)
