#!/usr/bin/python3
'''
Module: list all state objects
'''
if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    user_name = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    url = (f'mysql+mysqldb://{user_name}:{passwd}@localhost:3306/{db}')
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id)
    for row in query:
        print(f'{row.id}: {row.name}')
    session.close()
    '''
it needs to connect to the database and run a query on it
create an engine, create a session
'''
