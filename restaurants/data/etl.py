import petl as etl
import psycopg2
from datetime import datetime

# remove rows with no grade date?

restaurants = (
    etl
    .fromcsv('inspections.csv')
    .rename({'CAMIS': 'id', 'DBA': 'name', 'BORO': 'city', 'ZIPCODE': 'zip_code', 'PHONE': 'phone', 'GRADE': 'grade'})
    .cut("id", "name", "city", "BUILDING", "STREET", "zip_code", "phone", "CUISINE DESCRIPTION", "grade", "GRADE DATE")
    .selectisnot("grade", u"")
    .select("CUISINE DESCRIPTION",lambda cuisine: 'thai' in cuisine.lower())
    .cutout("CUISINE DESCRIPTION")
    .convert("GRADE DATE", lambda date: datetime.strptime(date, '%m/%d/%Y'))
    .groupselectmax("name", "GRADE DATE")
    .cutout("GRADE DATE")
    .select("grade", lambda grade: grade.lower() <= u"b")
    .addfield('address',lambda table: table['BUILDING'] + ' ' + table['STREET'])
    .cutout("BUILDING","STREET")
)

etl.tocsv(restaurants, 'cleaned_inspections.csv')

conn = psycopg2.connect('user=postgres password=postgres')
etl.todb(restaurants, conn, 'restaurants')


