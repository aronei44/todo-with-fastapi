from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import setting

engine = create_engine("{}://{}:{}@{}:{}/{}".format(setting.DATABASE,setting.DATABASE_USERNAME,setting.DATABASE_PASSWORD,setting.DATABASE_URL,setting.DATABASE_PORT,setting.DATABASE_NAME))

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)