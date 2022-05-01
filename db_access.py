import json
from model import Appointment, CoronaTest, CoronaVaccination, Patient


class Database:                                       # {⊥}
    patients: list[Patient] = []                      # {shs: shs}
    coronaTests:  list[CoronaTest] = []               # {shs: shs}
    coronaVaccinations: list[CoronaVaccination] = []  # {shs: shs}
    appointments: list[Appointment] = []              # {shs: shs}

    def load(self, filePath: str):
        f = open(filePath)
        db = json.load(f)
        self.patients = list(map(lambda p: Patient(
            p["id"], p["name"], p["cpr"]), db["patients"]))
        self.coronaTests = list(map(lambda ct: CoronaTest(
            ct["patient_id"], ct["date"], ct["result"]), db["corona_tests"]))
        self.coronaVaccinations = list(map(lambda cv: CoronaVaccination(
            cv["patient_id"], cv["date"]), db["corona_vaccination"]))
        self.appointments = list(map(lambda a: Appointment(
            a["patient_id"], a["date"], a["appointment"]), db["appointments"]))
        f.close()
