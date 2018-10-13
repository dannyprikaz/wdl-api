class UserService(object):
    def __init__(self, db_conn):
        self.db_conn = db_conn

    def create_user(self, user):
        self.db_conn.index_user(user)

    def get_user(self, user):
        return self.db_conn.get_user(user)

    def check_user(self, user):
        return bool(dict(self.db_conn.get_user(user)))
