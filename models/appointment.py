from database import Database


class Appointment(object):
    def __init__(self, subject, duration, start_time, client_name, counselor_id):
        self.subject = subject
        self.duration = duration
        self.start_time = start_time
        self.client_name = client_name
        self.counselor_id = counselor_id

    def get_json(self):
        return {
            'subject': self.subject,
            'duration': self.duration,
            'start_time': self.start_time,
            'client_name': self.client_name,
            'counselor_id': self.counselor_id
        }

    def save_to_db(self):
        Database.insert('appointments', self.get_json())

    @staticmethod
    def from_db(counselor_id):
        return [appointment for appointment in Database.find('appointments', {'counselor_id': counselor_id})]
