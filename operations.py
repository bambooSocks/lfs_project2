import datetime
import random

from numpy import isin
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
        patient_id {shs: shs}
        uploadDate {shs: shs}
        db         {⊥}
    '''
    db.coronaVaccinations.append(CoronaVaccination(patient_id, uploadDate))
    # {shs: shs} -> {shs: shs}


def retrievePatientData(patient_id_low: int, db: Database):
    '''
    Questions:
    We tried to apply Myers' Approach for de-classifying information. Is it correct?
    Should we still do Information Flow Analysis on the rest of the code?
    '''

    def declassify(match):
        return match

    def if_acts_for(patient_id: int):
        print('Are you acting (logged-in) as a hospital patient with id={}? y/n'.format(patient_id))
        answer = input()
        if str(answer) == 'y' or str(answer) == 'yes' or str(answer) == 'Yes':
            print(
                '\nYou have the right to access the test results. Here is your COVID-test information:\n')
            permission = True
        else:
            print('\nYou do not have the right to access to this information. Information will not be de-classified.\n')
            permission = False
        return permission

    def check_user(db_patientsList: list, patient_id: int):
        # returns ret:bool{client:hospitalAdmin}

        i = 0  # int{hospitalAdmin:hospitalAdmin}
        # bool{client:hospitalAdmin, hospitalAdmin:hospitalAdmin}
        match = False
        while i < len(db_patientsList):
            if db_patientsList[i].id == patient_id:
                match = True
            i += 1
        ret = False

        if if_acts_for(patient_id):
            ret = declassify(match)  # {client:hospitalAdmin}

        return ret, match

    patient_id = patient_id_low  # patient id:int{hospitalAdmin}
    ret, match = check_user(db.patients, patient_id)

    # get all patients id's
    patient_ids = [patient.id for patient in db.patients]

    # check if patient id exists
    if patient_id in patient_ids:
        # patient id exists, get patient
        # patient:int{hospitalAdmin}
        patient = db.patients[patient_ids.index(patient_id)]
        # loop through coronaTests, find all tests for patient and add to list

        # Corona tests:
        corona_tests = []
        for coronaTest in db.coronaTests:
            if coronaTest.patient_id == patient_id:
                corona_tests.append(coronaTest)

        # loop through coronaVaccinations, find all vaccinations for patient and add to list
        corona_vaccinations = []
        for coronaVaccination in db.coronaVaccinations:
            if coronaVaccination.patient_id == patient_id:
                corona_vaccinations.append(coronaVaccination)

        if not ret:
            print('Please try again to log in.')

        else:
            # de-classification:
            patient_revealed = patient
            corona_tests_revealed = corona_tests
            corona_vaccinations_revealed = corona_vaccinations

            print("patient info:")
            print(
                f"\tPatient ID: {patient_revealed.id}, \n\tName: {patient_revealed.name}, \n\tCPR: {patient_revealed.cpr}\n")

            print("Corona tests:")
            # check if corona_tests is empty
            if corona_tests_revealed:
                # get last index of corona_tests and print it
                last_index = len(corona_tests_revealed) - 1
                print(
                    f"\tLast corona test date: {corona_tests_revealed[last_index].date}, \n\tcorona test result: {corona_tests_revealed[last_index].result}\n")
            else:
                print("No tests found")

            print("Corona vaccinations:")
            # check if corona_vaccinations is empty
            if corona_vaccinations_revealed:
                # get last index of corona_vaccinations and print it
                last_index = len(corona_vaccinations_revealed) - 1
                print(
                    f"\tLast vaccination: {corona_vaccinations_revealed[last_index].date}, \n\tvaccination number: {corona_vaccinations_revealed[last_index].shot_number}")
            else:
                print("No vaccinations found")
    if not match:
        print(f"Patient id {patient_id_low} does not exist in the database")


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
