# /data/database/utils/setconn.py
"""
This module sets up the connection to the database. 
db_host, db_port, db_name, db_user, and db_password are environment variables.
details are stored in .env file
"""
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from dotenv import load_dotenv

load_dotenv()

# Define the database details
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

# Create the engine
engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

# Reflect the tables
metadata = MetaData()
metadata.reflect(engine)


# Generate mapped classes
Base = automap_base(metadata=metadata)
Base.prepare()

# Now you can access your tables as classes. For example:
DockerImages = Base.classes.dockerimages
Agents = Base.classes.agents
# ...

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Now you can query your tables. For example:
images = session.query(DockerImages).all()

# Reflect the tables
metadata = MetaData()
metadata.reflect(engine)

