stor
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
# from sqlalchemy.sql.expression import false

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)