from models.appointment import Appointment
from models.counselor import Counselor
from pprint import pprint


class Menu(object):
    def __init__(self):
        choice = input("Are you a new counselor? Y/N\n")
        if choice == 'Y':
            first_name = input("Enter your first name:")
            last_name = input("Enter your last name:")
            id = input("Enter your ID:")

            self.counselor = Counselor(first_name, last_name, id)
            self.counselor.save_to_db()

        else:
            id = input("Enter your ID:")
            self.counselor = Counselor.from_db(id)

    def run_menu(self):
        choice = input("Hello {}!\n"
                       "If you want to see your appointments, enter '1'\n"
                       "If you want to set new appointment, enter '2'\n"
                       "If you want to exit, enter '3'\n".format(self.counselor.first_name
                                                                 + " " + self.counselor.last_name))

        if choice == '1':
            results = Appointment.from_db(self.counselor.id)
            for result in results:
                pprint(result)


        elif choice == '2':
            self._set_new_appointment()
        else:
            print("Goodbye {}".format(self.counselor.first_name
                                      + "" + self.counselor.last_name))

    # if choice is '2':
    def _set_new_appointment(self):
        subject = input("Enter subject:")
        duration = input("Enter duration:")
        start_time = input("Enter start time:")
        client_name = input("Enter client name:")
        counselor_id = self.counselor.id

        appointment = Appointment(subject, duration, start_time, client_name, counselor_id)
        appointment.save_to_db()

        print("Appointment has been set successfully!")


