#!/usr/bin/python3
'''
Module deletes state which start with letter a
'''
if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    import sys

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    url = f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}'
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(State.name.like('%a%')).delete()
    session.commit()
    session.close()
