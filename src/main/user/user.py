import inspect
from hashlib import sha1

class User(object):
    def __init__(self, email=None, display_name=None, _id=None):
        self.email = email
        self.display_name = display_name
        if _id:
            self._id = _id
        else:
            self._id = sha1(email).hexdigest() if email else None

    def __iter__(self):
        # create a list of attributes that are common to all objects
        common_attrs = dir(type('dummy', (object,), {}))
        # yield key-value pairs for all of the user defined attributes
        for item in inspect.getmembers(self):
            if item[0] not in common_attrs and not item[0] in ['__iter__', '__eq__']:
                if item[1]:
                    yield item[0], item[1]

    def __eq__(self, other):
        return dict(self) == dict(other)
