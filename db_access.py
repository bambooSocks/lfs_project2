import json
from model import Appointment, CoronaTest, CoronaVaccination, Patient


# Database class High db
    # Patient List class High db.patients
        # Patient class High db.patients[i]
            # integer High db.patients[i].id
            # string High db.patients[i].name
            # string High db.patients[i].cpr

    # Appointment List class High db.appointments
        # Appointment class High db.appointments[i]
            # integer High db.appointments[i].patient_id
            # datetime High db.appointments[i].date
            # string High db.appointments[i].appointment

    # CoronaTest List class High db.coronaTests
        # CoronaTest class High db.coronaTests[i]
            # integer High db.coronaTests[i].patient_id
            # datetime High db.coronaTests[i].date
            # string High db.coronaTests[i].result

    # CoronaVaccination List class High db.coronaVaccinations
        # CoronaVaccination class High db.coronaVaccinations[i]
            # integer High db.coronaVaccinations[i].patient_id
            # datetime High db.coronaVaccinations[i].date
            # string High db.coronaVaccinations[i].shot_number

# CoronaTest class High db.coronaTests
# CoronaVaccintation class High db.coronaVaccinations


class Database:
    patients: list[Patient] = []
    coronaTests:  list[CoronaTest] = []
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
