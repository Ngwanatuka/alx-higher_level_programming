#!/usr/bin/python3
"""
Script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print('Usage: {} username password database_name state_name'
              .format(sys.argv[0]))
        exit(1)

    # Create SQLAlchemy engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Generate database schema via SQLAlchemy ORM
    Base.metadata.create_all(engine)

    # Create a new session that will allow us to query the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to find the state with the given name
    result = session.query(State).filter(State.name == sys.argv[4]).first()

    # If the state was found, print its ID. Otherwise, print Not found
    if result:
        print(result.id)
    else:
        print('Not found')
