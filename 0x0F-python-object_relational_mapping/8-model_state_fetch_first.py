#!/usr/bin/python3
'''
Module: printfirst state in database
'''
if __name__ == '__main__':
    from sqlalchemy import create_engine
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    url = f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}'
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).first()
    if (query):
        print(f'{query.id}: {query.name}')
    else:
        print('Nothing')
    session.close()
