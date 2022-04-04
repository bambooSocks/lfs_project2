import json
from model import Appointment, CoronaTest, CoronaVaccination, Patient


class Database:
    patients: list[Patient] = []
    coronaTests: list[CoronaTest] = []
    coronaVaccinations: list[CoronaVaccination] = []
    appointments: list[Appointment] = []

    def load(self, filePath: str):
        f = open(filePath)
        db = json.load(f)
        self.patients = list(map(lambda p: Patient(
            p["id"], p["name"], p["cpr"]), db["patients"]))
        self.coronaTests = list(map(lambda ct: CoronaTest(
            ct["patient_id"], ct["date"], ct["result"]), db["corona_tests"]))
        self.coronaVaccinations = list(map(lambda cv: CoronaVaccination(
            cv["patient_id"], cv["date"], cv["shot_number"]), db["corona_vaccination"]))
        self.appointments = list(map(lambda a: Appointment(
            a["patient_id"], a["date"], a["appointment"]), db["appointments"]))
        f.close()
