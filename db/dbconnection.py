import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from urllib.parse import quote_plus

class DbConnection:
    load_dotenv()
    dbuser = os.getenv("DBUSER")
    dbpassword = quote_plus(os.getenv("DBPASSWORD"))
    dburl = os.getenv("DBURL")
    dbport = os.getenv("DBPORT")
    dbdatabase = os.getenv("DBDATABASE")

    # PostgreSQL connection string
    DATABASE_URL = f'postgresql+psycopg2://{dbuser}:{dbpassword}@{dburl}:{dbport}/{dbdatabase}'

    # Create engine
    def create_session(self):
        engine = create_engine(self.DATABASE_URL)
        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
