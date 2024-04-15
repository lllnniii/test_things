from sqlalchemy.orm import sessionmaker
from SQLfignyaimgonnacry import Spaceship
import models


def main():
    models.Base.metadata.drop_all(bind=models.engine)
    models.Base.metadata.create_all(bind=models.engine)


if __name__ == '__main__':
    main()

Session = sessionmaker(bind=models.engine)
session = Session()

ship = Spaceship('roton', 0, 0)
earth = models.SpaceObj(id=1, name='Earth', x=2, y=10)
sun = models.SpaceObj(id=2, name='Sun', x=2, y=13)

session.add(earth)
session.add(sun)
session.commit()

print(ship.move_to(1, 2, session))
print(ship.move_to(1, 11, session))

#print(session.new)
