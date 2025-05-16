#Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from crear_base import Pais
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).filter(
    or_(
        Pais.nombre.like("%uador%"),
        Pais.capital.like("%ito%")
    )
).all()

for p in paises:
    print(p)
