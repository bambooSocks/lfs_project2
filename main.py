from pprint import pprint
from db_access import Database
from model import Appointment, CoronaTest, CoronaVaccination, Patient
from operations import bookAppointment, uploadTestResult, updateVaccinationStatus, retrievePatientData, getStats

if __name__ == "__main__":
    db = Database()
    db.load("testdb.json")

    # db.patients.append(Patient(9, "Spongebob Squarepants", "010599-4321"))

    bookAppointment(Patient(6, "Jens Jensen", "050443-1235"),
                    "21/12/2021 10:55", "corona_vaccination", db)

    # retrievePatientData(10, db)

    # getStats(db, "17/05/2021 12:30")

    # pprint(db.appointments)

    pprint(db.coronaVaccinations)
    pprint(type(db.patients))
    pprint(retrievePatientData(100, db))
