#!/usr/bin/python3
'''
Module: returns states with letter a
'''
if __name__ == '__main__':
    from model_state import Base, State
    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    url = f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}'
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(State.name.like('%a%')).all()
    for row in query:
        print(f'{row.id}: {row.name}')
    session.close()
