import uuid

from database import Database


class Counselor(object):

    def __init__(self, first_name, last_name, id=None):

        self.first_name = first_name
        self.last_name = last_name
        # Generate new id if not supplied
        self.id = uuid.uuid4() if id is None else id

    def save_to_db(self):
        Database.insert('counselors', self.get_json())

    def get_json(self):
        return{
            'first_name': self.first_name,
            'last_name': self. last_name,
            'id': self.id,
        }

    @classmethod
    def from_db(cls, counselor_id):
        info = Database.find_one('counselors', {'id': counselor_id})
        return cls(info['first_name'],
                   info['last_name'],
                   info['id'])
