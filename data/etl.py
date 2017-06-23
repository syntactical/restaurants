import petl as etl
import psycopg2
from datetime import datetime
from geopy.geocoders import Nominatim

def load_restaurant_data(conn, from_file):
    geolocator = Nominatim()

    restaurants = etl.fromcsv(from_file)
    restaurants = etl.rename(restaurants, {'CAMIS': 'id', 'DBA': 'name', 'BORO': 'city', 'ZIPCODE': 'zip_code', 'PHONE': 'phone', 'GRADE': 'grade'})
    restaurants = etl.cut(restaurants, "id", "name", "city", "BUILDING", "STREET", "zip_code", "phone", "CUISINE DESCRIPTION", "grade", "GRADE DATE")
    restaurants = etl.selectisnot(restaurants, "grade", u"")
    restaurants = etl.select(restaurants, "CUISINE DESCRIPTION",lambda cuisine: 'thai' in cuisine.lower())
    restaurants = etl.cutout(restaurants, "CUISINE DESCRIPTION")
    restaurants = etl.convert(restaurants, "GRADE DATE", lambda date: datetime.strptime(date, '%m/%d/%Y'))
    restaurants = etl.groupselectmax(restaurants, "name", "GRADE DATE")
    restaurants = etl.cutout(restaurants, "GRADE DATE")
    restaurants = etl.select(restaurants, "grade", lambda grade: grade.lower() <= u"b")
    restaurants = etl.addfield(restaurants, 'address',lambda table: table['BUILDING'] + ' ' + table['STREET'])
    restaurants = etl.cutout(restaurants, "BUILDING","STREET")
    restaurants = etl.addfield(restaurants, 'geolocation', lambda restaurant: geolocator.geocode(restaurant['address'] + ' ' + restaurant['city'], timeout=10))

    etl.tocsv(restaurants, 'cleaned_inspections.csv')
    etl.todb(restaurants, conn, 'restaurants', drop=True, create=True)
