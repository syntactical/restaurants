from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()

def Restaurant(Base):
	__tablename__ = 'restaurants'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	address = Column(String)
	zip_code = Column(String)
	city = Column(String)
	phone = Column(String)
	grade = Column(String)
	def __repr__(self):
	   return "<User(name='%s', address='%s', phone='%s', grade='%s')>" % (
	                        self.name, self.address + ' ' + self.city + ', NY ' + self.zip_code, self.phone, self.grade)