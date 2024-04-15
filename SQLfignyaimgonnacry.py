from sqlalchemy import select
import models


class Spaceship:

    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def move_to(self, x, y, session):
        self.x += x
        self.y += y

        sel = select(models.SpaceObj.name).where(models.SpaceObj.x == self.x, models.SpaceObj.y == self.y)
        res = session.execute(sel).fetchone()
        if res is None:
            return 'Корабль находится в открытом космосе'
        else:
            obj, = res
            return f'Корабль около космического тела {obj}'
