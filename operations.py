import datetime
import random

# from numpy import isin
from model import Appointment, CoronaTest, CoronaVaccination, Patient
from db_access import Database


# use if you need
# # if_acts_for(bookAppointment, patient) then
# #   isInDB_declass = declassify(isInDB, {shs: shs})
# isInDB_declass = isInDB


def bookAppointment(patient: Patient, date: str, appointment_type: str, db: Database):
    """
        patient          {shs: shs}
        date             {shs: shs}
        appointment_type {shs: shs}
        db               {⊥}
    """
    # Check if patient exists
    isInDB = False  # {shs: shs}
    i = 0  # {⊥}
    while i < len(db.patients):
        if db.patients[i] == patient:
            isInDB = True
            # implicit patient, db.patients -> isInDB {shs: shs} -> {shs: shs}
            # implicit i -> isInDB {⊥} -> {shs: shs}
            break
        i += 1  # {⊥} -> {⊥}

    if isInDB:
        print("Patient exists, making appointment")  # printed to {shs: shs}
        db.appointments.append(Appointment(patient.id, date, appointment_type))
        # {shs: shs} -> {shs: shs}
    else:
        # printed to {shs: shs}
        print("Patient does not exist, no appointment booked")


def uploadTestResult(patient_id: int, uploadDate: str, result: str, db: Database):
    '''
        patient_id {shs: shs}
        uploadDate {shs: shs}
        result     {shs: shs}
        db         {⊥}
    '''
    db.coronaTests.append(CoronaTest(patient_id, uploadDate, result))
    # {shs: shs} -> {shs: shs}


def updateVaccinationStatus(patient_id: int, uploadDate: str, db: Database):
    '''
        patient_id {shs: shs, patient: shs}
        uploadDate {shs: shs}
        db         {⊥}
    '''
    db.coronaVaccinations.append(CoronaVaccination(patient_id, uploadDate))
    # {shs: shs} -> {shs: shs}


def retrievePatientData(patient_id: int, db: Database):
    """
    patient_id       {shs: shs}
    db               {⊥}
    name_patient    {shs: shs, patient:shs}
    cpr_patient     {shs: shs, patient:shs}
    correct_idx     {shs:shs}
    corona_test     {shs:shs}
    corona_vaccine  {shs:shs}
    """
    # Check if patient exists
    isInDB = False  # {shs: shs}
    i = 0  # {⊥}
    correct_idx = -100
    while i < len(db.patients):
        if db.patients[i].id == patient_id:  # {shs: shs} -> {shs: shs}
            isInDB = True
            correct_idx = i  # {⊥} -> {shs: shs}
            # implicit patient_id, db.patients[i].id  -> isInDB {shs: shs} -> {shs: shs}
            # implicit i -> isInDB {⊥} -> {shs: shs}

            break
        i += 1  # {⊥} -> {⊥}

    # use if you need
    # # if_acts_for(bookAppointment, patient) then
    # #   isInDB_declass = declassify(isInDB, {⊥})
    isInDB_declass = isInDB

    if isInDB_declass:
        # Implicit flows from the IF statement:
        # implicit isInDB -> name_patient, cpr_patient {⊥} -> {shs: shs, patient:shs}
        # implicit isInDB -> corona_tests, db.coronaTests[i], db.coronaTests[idx].patient_id, patient_id, idx {⊥} -> {shs:shs}
        # implicit isInDB -> corona_vaccinations, db.coronaVaccinations[idx], db.coronaVaccinations[i].patient_id {⊥} -> {shs:shs}
        # implicit isInDB -> corona_test, corona_vaccine {⊥} -> {shs:shs}
        # (after de-classification) implicit isInDB -> corona_test, corona_vaccine {⊥} -> {patient: shs}

        name_patient = db.patients[correct_idx].name  # {shs: shs, patient:shs} -> {shs: shs, patient:shs}
        cpr_patient = db.patients[correct_idx].cpr  # {shs: shs, patient:shs} -> {shs: shs, patient:shs}

        corona_tests = []  # {shs: shs}
        idx = 0  # {shs:shs}
        while idx < len(db.coronaTests):
            if db.coronaTests[idx].patient_id == patient_id:
                corona_tests.append(db.coronaTests[idx])  # {shs: shs} -> {shs: shs}
                # implicit patient_id, db.coronaTests[idx].patient_id -> corona_tests {shs: shs} -> {shs: shs}
                # implicit idx -> corona_tests {shs: shs} -> {shs: shs}
                break
            idx += 1  # {shs:shs} -> {shs:shs}

        corona_vaccinations = []  # {shs: shs}
        idx = 0  # {shs: shs}
        while i < len(db.coronaVaccinations):
            if db.coronaVaccinations[idx].patient_id == patient_id:  # {shs: shs} -> {shs:shs}
                corona_vaccinations.append(db.coronaVaccinations[idx])  # {shs: shs} -> {shs: shs}
                # implicit patient_id, db.coronaVaccinations[idx].patient_id -> corona_vaccinations {shs: shs} -> {shs: shs}
                # implicit idx -> corona_vaccinations {shs: shs} -> {shs: shs}
                break
            idx += 1  # {shs: shs} -> {shs: shs}

        corona_vaccine = corona_vaccinations[-1]  # {shs:shs} -> {shs:shs}
        corona_test = corona_tests[-1]  # {shs:shs} -> {shs:shs}

        # # if_acts_for(retrievePatientData, patient) then
        # #   name_patient_declass = declassify(name_patient, {patient: {shs,patient}})
        # #   cpr_patient_declass = declassify(cpr_patient, {patient: shs,patient})

        # #   corona_vaccine_class = classify(corona_vaccine, {shs: shs, patient:shs})
        # #   corona_vaccine_declass = declassify(corona_vaccine_class, {patient:shs})

        # #   corona_test_class = classify(corona_test, {shs: shs, patient:shs})
        # #   corona_test_declass = declassify(corona_test_class, {patient:shs})

        corona_test_declass = corona_test
        corona_vaccine_declass = corona_vaccine

        print("patient info:")
        print(
            f"\tPrinting results for patient ID: {patient_id}\n")  # print to {shs:shs}
        print(
            f"\tName Patient: {name_patient}, \n\tCPR: {cpr_patient}\n")  # print to {patient:shs}
        print(
            f"\tLast corona test date: {corona_test_declass.date}, \n\tcorona test result: {corona_test_declass.result}\n") # print to {patient:shs}
        print(
            f"\tLast vaccination: {corona_vaccine_declass.date}")
    else:
        print("Patient was not found")  # print to {shs: shs}

def getStats(db: Database, data_from_date: str = None):
    # check if data_from_date is None
    if data_from_date is None:
        # get amount of corona tests
        corona_tests = len(db.coronaTests)

        # get amount of corona tests with positive result
        positive_tests = 0
        for coronaTest in db.coronaTests:
            if coronaTest.result == "paavist":
                positive_tests += 1

        print("Corona tests:")
        print(f"\tAmount of corona tests: {corona_tests}")
        print(f"\tAmount of positive corona tests: {positive_tests}\n")

        # get amount of corona vaccinations
        corona_vaccinations = len(db.coronaVaccinations)

        # get amount of patients who got 1 shot, 2 shots, 3 shots
        # shots = [{1: 0}, {2: 0}, {3: 0}]
        # for coronaVaccination in db.coronaVaccinations:
        #     if coronaVaccination.shot_number == 1:
        #         shots[0][1] += 1
        #     elif coronaVaccination.shot_number == 2:
        #         shots[1][2] += 1
        #     elif coronaVaccination.shot_number == 3:
        #         shots[2][3] += 1

        print("Corona vaccinations:")
        print(f"\tAmount of corona vaccinations: {corona_vaccinations}")
        print(f"\tAmount of patients who got 1 shot: {shots[0][1]}")
        print(f"\tAmount of patients who got 2 shots: {shots[1][2]}")
        print(f"\tAmount of patients who got 3 shots: {shots[2][3]}\n")

    else:
        # get amount of corona tests after data_from_date
        corona_tests = 0
        for coronaTest in db.coronaTests:
            if coronaTest.date > data_from_date:
                corona_tests += 1

        # get amount of corona tests with positive result after data_from_date
        positive_tests = 0
        for coronaTest in db.coronaTests:
            if coronaTest.date > data_from_date and coronaTest.result == "paavist":
                positive_tests += 1

        print("Corona tests:")
        print(f"\tAmount of corona tests: {corona_tests}")
        print(f"\tAmount of positive corona tests: {positive_tests}\n")

        # get amount of corona vaccinations after data_from_date
        corona_vaccinations = 0
        for coronaVaccination in db.coronaVaccinations:
            if coronaVaccination.date > data_from_date:
                corona_vaccinations += 1

        # get amount of patients who got 1 shot, 2 shots, 3 shots after data_from_date
        # shots = [{1: 0}, {2: 0}, {3: 0}]
        # for coronaVaccination in db.coronaVaccinations:
        #     if coronaVaccination.date > data_from_date and coronaVaccination.shot_number == 1:
        #         shots[0][1] += 1
        #     elif coronaVaccination.date > data_from_date and coronaVaccination.shot_number == 2:
        #         shots[1][2] += 1
        #     elif coronaVaccination.date > data_from_date and coronaVaccination.shot_number == 3:
        #         shots[2][3] += 1

        print("Corona vaccinations:")
        print(f"\tAmount of corona vaccinations: {corona_vaccinations}")
        print(f"\tAmount of patients who got 1 shot: {shots[0][1]}")
        print(f"\tAmount of patients who got 2 shots: {shots[1][2]}")
        print(f"\tAmount of patients who got 3 shots: {shots[2][3]}\n")
