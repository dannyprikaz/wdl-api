class UserService(object):
    def __init__(self, db_conn):
        self.db_conn = db_conn

    def create_user(self, user):
        self.db_conn.index_user(user)