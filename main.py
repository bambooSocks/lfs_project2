from pprint import pprint
from db_access import Database
from model import Appointment, CoronaTest, CoronaVaccination, Patient

if __name__ == "__main__":
    db = Database()
    db.load("db.json")

    db.patients.append(Patient(9, "Spongebob Squarepants", "010599-4321"))

    pprint(db.patients)
    pprint(db.appointments)
    pprint(db.coronaTests)
    pprint(db.coronaVaccinations)
