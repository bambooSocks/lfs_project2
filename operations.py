import datetime
import random
from model import Appointment, CoronaTest, CoronaVaccination, Patient
from db_access import Database


def bookAppointment(patient: Patient, date: str, appointment_type: str, db: Database):

    # Check if patient exists
    if patient in db.patients:
        # Patient exists, make appointment
        print("Patient exists, making appointment")
        db.appointments.append(Appointment(patient.id, date, appointment_type))
    else:
        # Patient does not exist, create patient and appointment
        print("Patient does not exist, creating patient and appointment")
        db.patients.append(patient)
        db.appointments.append(Appointment(patient.id, date, appointment_type))

    if appointment_type == "corona_test":
        uploadTestResult(patient.id, date, db)
    elif appointment_type == "corona_vaccination":
        updateVaccinationStatus(patient.id, date, db)


def uploadTestResult(patient_id: int, date: str, db: Database):
    # get date after date
    date_after = datetime.datetime.strptime(
        date, "%d/%m/%Y %H:%M") + datetime.timedelta(days=1)

    # convert date_after to string
    date_after_str = date_after.strftime("%d/%m/%Y %H:%M")

    # get random result
    result = ["paavist", "ikke paavist"][int(round(random.random()))]

    # append new coronaTest to db.coronaTests
    db.coronaTests.append(CoronaTest(patient_id, date_after_str, result))


def updateVaccinationStatus(patient_id: int, date: str, db: Database):
    # get date after date
    date_after = datetime.datetime.strptime(
        date, "%d/%m/%Y %H:%M") + datetime.timedelta(days=1)

    # convert date_after to string
    date_after_str = date_after.strftime("%d/%m/%Y %H:%M")

    # get amount of shots for patient_id
    shots = len([coronaVaccination.shot_number for coronaVaccination in db.coronaVaccinations if coronaVaccination.patient_id == patient_id]) + 1

    # append new coronaTest to the database
    db.coronaVaccinations.append(
        CoronaVaccination(patient_id, date_after_str, shots))


def retrievePatientData(patient_id: int, db: Database):

    # get all patients id's
    patient_ids = [patient.id for patient in db.patients]

    # check if patient id exists
    if patient_id in patient_ids:
        # patient id exists, get patient
        patient = db.patients[patient_ids.index(patient_id)]
        print("patient info:")
        print(
            f"\tPatient ID: {patient.id}, \n\tName: {patient.name}, \n\tCPR: {patient.cpr}\n")

        # loop through coronaTests, find all tests for patient and add to list
        corona_tests = []
        for coronaTest in db.coronaTests:
            if coronaTest.patient_id == patient_id:
                corona_tests.append(coronaTest)

        print("Corona tests:")
        # check if corona_tests is empty
        if corona_tests:
            # get last index of corona_tests and print it
            last_index = len(corona_tests) - 1
            print(
                f"\tLast corona test date: {corona_tests[last_index].date}, \n\tcorona test result: {corona_tests[last_index].result}\n")
        else:
            print("No tests found")

        # loop through coronaVaccinations, find all vaccinations for patient and add to list
        corona_vaccinations = []
        for coronaVaccination in db.coronaVaccinations:
            if coronaVaccination.patient_id == patient_id:
                corona_vaccinations.append(coronaVaccination)

        print("Corona vaccinations:")
        # check if corona_vaccinations is empty
        if corona_vaccinations:
            # get last index of corona_vaccinations and print it
            last_index = len(corona_vaccinations) - 1
            print(
                f"\tLast vaccination: {corona_vaccinations[last_index].date}, \n\tvaccination number: {corona_vaccinations[last_index].shot_number}")
        else:
            print("No vaccinations found")

    else:
        # if patient id does not exist, print error message
        print(f"Patient id {patient_id} does not exist in database")


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
        shots = [{1: 0}, {2: 0}, {3: 0}]
        for coronaVaccination in db.coronaVaccinations:
            if coronaVaccination.shot_number == 1:
                shots[0][1] += 1
            elif coronaVaccination.shot_number == 2:
                shots[1][2] += 1
            elif coronaVaccination.shot_number == 3:
                shots[2][3] += 1

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
        shots = [{1: 0}, {2: 0}, {3: 0}]
        for coronaVaccination in db.coronaVaccinations:
            if coronaVaccination.date > data_from_date and coronaVaccination.shot_number == 1:
                shots[0][1] += 1
            elif coronaVaccination.date > data_from_date and coronaVaccination.shot_number == 2:
                shots[1][2] += 1
            elif coronaVaccination.date > data_from_date and coronaVaccination.shot_number == 3:
                shots[2][3] += 1

        print("Corona vaccinations:")
        print(f"\tAmount of corona vaccinations: {corona_vaccinations}")
        print(f"\tAmount of patients who got 1 shot: {shots[0][1]}")
        print(f"\tAmount of patients who got 2 shots: {shots[1][2]}")
        print(f"\tAmount of patients who got 3 shots: {shots[2][3]}\n")
