import petl as etl
import psycopg2
from datetime import datetime

# remove rows with no grade date?

restaurants = (
	etl
	.fromcsv('i.csv')
	.rename({'CAMIS': 'id', 'DBA': 'name'})
	.cut("id", "name", "BORO", "BUILDING", "STREET", "ZIPCODE", "PHONE", "CUISINE DESCRIPTION", "GRADE", "GRADE DATE")
	.selectisnot("GRADE", u"")
	.select("CUISINE DESCRIPTION",lambda cuisine: 'thai' in cuisine.lower())
	.cutout("CUISINE DESCRIPTION")
	.convert("GRADE DATE", lambda date: datetime.strptime(date, '%m/%d/%Y'))
	.groupselectmax("name", "GRADE DATE")
	.cutout("GRADE DATE")
	.select("GRADE", lambda grade: grade.lower() <= u"b")
	.addfield('address',lambda table: table['BUILDING'] + ' ' + table['STREET'])
	.cutout("BUILDING","STREET")
)

etl.tocsv(restaurants, 'cleaned_inspections.csv')

db_connection = psycopg2.connect('dbname=example user=postgres')
etl.todb(restaurants, db_connection, 'restaurants')


