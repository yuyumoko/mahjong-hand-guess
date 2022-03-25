from collections import namedtuple
from .utils import init_db

UserDb = init_db(tablename="user_db")

UserInfo = namedtuple("UserInfo", "points", defaults=(0,))


class User:
    __slots__ = ["user_id"]

    def __init__(self, user_id):
        self.user_id = user_id

    def get_info(self):
        info = UserDb.get(self.user_id)
        return UserInfo(**info) if info else UserInfo()

    @property
    def points(self):
        return self.get_info().points

    def add_points(self, points):
        info = self.get_info()
        end_points = info.points + points
        UserDb[self.user_id] = UserInfo(points=end_points)._asdict()

    @staticmethod
    def points_rank():
        return
