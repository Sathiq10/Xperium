from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm  import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from dbsettings import postgresql as settings

# engine = create_engine('postgres:///sqlalchemy.postgres',echo=True)

base=declarative_base()

class Users(base):
    __tablename__= 'users'
    
    user_id= Column('user_id',Integer, primary_key=True)
    name=Column('name',String)
    email=Column('email',String)
    phone_number=Column('phone_number',Integer)
    age=Column('age',Integer)
    gender=Column('gender',String)
    salary=Column('salary',Integer)
    date_of_birth=Column('date_of_birth',Integer)
    Created_date=Column('Created_date',Integer)


    def __init__(self,user_id,name,email,phone_number,age,gender,salary,date_of_birth,Created_date):
        self.user_id=user_id
        self.name=name
        self.email=email
        self.phone_number=phone_number
        self.age=age
        self.gender=gender
        self.salary=salary
        self.date_of_birth=date_of_birth
        self.Created_date=Created_date

    def __repr__(self):
        return f"({self.user_id}),{self.name},{self.email},{self.phone_number},({self.age},{self.gender}),{self.salary},{self.date_of_birth},{self.Created_date}"

# engine = create_engine("postgresql://postgres:root@localhost:5432/People",echo=True)
engine=create_engine("postgresql+psycopg2://postgres:root@localhost:5432/People")




base.metadata.create_all(bind=engine)
Session =sessionmaker(bind=engine)
session=Session()

user=Users("10","le","leo@gl.com",987187,25,"M",12000,13-12-2005,20-10-2025)
session.add(user)
session.commit()

user1=Users("11","rel","Raph@il.com",987187,26,"M",12000,13-12-2004,21-10-2025)
user2=Users("13","dolo","don@gil.com",987187,27,"M",12000,13-12-2003,22-10-2025)

session.add(user1)
session.add(user2)
session.commit()