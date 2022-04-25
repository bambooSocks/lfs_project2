import json
from model import Appointment, CoronaTest, CoronaVaccination, Patient


# Database class Low db

#   Patient List class Low db.patients
#   Patient class Low db.patients[i]
#       integer High db.patients[i].id
#       string High db.patients[i].name
#       string High db.patients[i].cpr

#   Appointment List class Low db.appointments
#   Appointment class Low db.appointments[i]
#       integer High db.appointments[i].patient_id
#       datetime High db.appointments[i].date
#       string High db.appointments[i].appointment

#   CoronaTest List class Low db.coronaTests
#   CoronaTest class Low db.coronaTests[i]
#       integer High db.coronaTests[i].patient_id
#       datetime High db.coronaTests[i].date
#       string High db.coronaTests[i].result

#   CoronaVaccination List class Low db.coronaVaccinations
#   CoronaVaccination class Low db.coronaVaccinations[i]
#       integer High db.coronaVaccinations[i].patient_id
#       datetime High db.coronaVaccinations[i].date
#       string High db.coronaVaccinations[i].shot_number

#   CoronaTest class Low db.coronaTests
#   CoronaVaccintation class Low db.coronaVaccinations


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
