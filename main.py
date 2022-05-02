from pprint import pprint
from db_access import Database
from model import Appointment, CoronaTest, CoronaVaccination, Patient
from operations import bookAppointment, uploadTestResult, updateVaccinationStatus, retrievePatientData, getStats

if __name__ == "__main__":
    db = Database()
    db.load("testdb.json")

    bookAppointment(Patient(6, "Jens Jensen", "050443-1235"),
                    "21/12/2021 10:55", "corona_vaccination", db)
    retrievePatientData(2, db)
    getStats(db, "07/02/2021 14:45")
