import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from crear_base import Pais

# Leer JSON desde web
url = "https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json"
response = requests.get(url)
data = response.json()

# Conexión a la base de datos
engine = create_engine('sqlite:///country.db')
Session = sessionmaker(bind=engine)
session = Session()

for item in data:
    pais = Pais(
        nombre=item.get("CLDR display name", ""),
        capital=item.get("Capital", ""),
        continente=item.get("Continent", ""),
        dial=item.get("Dial", ""),
        geoname_id=item.get("Geoname ID", 0),
        itu=item.get("ITU", ""),
        lenguajes=item.get("Languages", ""),
        independiente=item.get("is_independent", "")
    )
    session.add(pais)

session.commit()
print("Datos importados exitosamente.")
