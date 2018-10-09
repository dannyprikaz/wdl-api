import inspect
from hashlib import sha1

class User(object):
    def __init__(self, email, display_name):
        self.email = email
        self.dispaly_name = display_name
        self.user_id = sha1(email).hexdigest()

    def __iter__(self):
        # create a list of attributes that are common to all objects
        common_attrs = dir(type('dummy', (object,), {}))
        # yield key-value pairs for all of the user defined attributes
        for item in inspect.getmembers(self):
            if item[0] not in common_attrs and not item[0] in ['__iter__', '__eq__']:
                yield item[0], item[1]

    def __eq__(self, other):
        return dict(self) == dict(other)
