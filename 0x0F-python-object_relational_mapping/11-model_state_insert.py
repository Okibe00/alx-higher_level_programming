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
    new_state = State(name='Louisiana')
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.add(new_state)
    session.commit()
    qry = session.query(State)
    for row in session.query(State).filter(State.name == 'Louisiana'):
        print(row.id)
    session.close()
