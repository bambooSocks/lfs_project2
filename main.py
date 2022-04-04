from pprint import pprint
from db_access import loadDB
from model import Appointment, CoronaTest, CoronaVaccination, Patient

if __name__ == "__main__":
    db = loadDB()
    patients: list[Patient] = db["patients"]
    coronaTests: list[CoronaTest] = db["corona_tests"]
    coronaVaccinations: list[CoronaVaccination] = db["corona_vaccination"]
    appointments: list[Appointment] = db["appointments"]

    pprint(patients)
