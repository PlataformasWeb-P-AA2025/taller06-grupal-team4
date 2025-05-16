#Presentar los países de Asía, ordenados por el atributo Dial.
from sqlalchemy.orm import sessionmaker
from crear_base import Pais
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).filter(Pais.continente == 'AS').order_by(Pais.dial).all()

for p in paises:
    print(p)
