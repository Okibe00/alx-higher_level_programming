#!/usr/bin/python3
'''
Module deletes state which start with letter a
'''
if __name__ == '__main__':
    from model_state import Base, State
    from model_city import City
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
    query = session.query(City).all()
    count = 1
    for city in query:
        print(f'{city.state.name}: ({count}) {city.name}')
        count += 1
    session.commit()
    session.close()
