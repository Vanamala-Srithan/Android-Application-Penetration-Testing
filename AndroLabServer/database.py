from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# ❗ FIXED: Removed convert_unicode=True
engine = create_engine('sqlite:///mydb.db')

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # Import all models here so that they get registered properly
    import models
    Base.metadata.create_all(bind=engine)
