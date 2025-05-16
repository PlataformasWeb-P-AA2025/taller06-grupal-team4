from sqlalchemy.orm import sessionmaker
from crear_base import Pais
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).filter(Pais.continente == 'EU').order_by(Pais.capital).all()

for p in paises:
    print(p)
