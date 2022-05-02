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

        # {shs: shs, patient:shs} -> {shs: shs, patient:shs}
        name_patient = db.patients[correct_idx].name
        # {shs: shs, patient:shs} -> {shs: shs, patient:shs}
        cpr_patient = db.patients[correct_idx].cpr

        corona_tests = []  # {shs: shs}
        idx = 0  # {shs:shs}
        while idx < len(db.coronaTests):
            if db.coronaTests[idx].patient_id == patient_id:
                # {shs: shs} -> {shs: shs}
                corona_tests.append(db.coronaTests[idx])
                # implicit patient_id, db.coronaTests[idx].patient_id -> corona_tests {shs: shs} -> {shs: shs}
                # implicit idx -> corona_tests {shs: shs} -> {shs: shs}

            idx += 1  # {shs:shs} -> {shs:shs}

        corona_vaccinations = []  # {shs: shs}
        idx = 0  # {shs: shs}
        while idx < len(db.coronaVaccinations):
            # {shs: shs} -> {shs:shs}
            if db.coronaVaccinations[idx].patient_id == patient_id:
                # {shs: shs} -> {shs: shs}
                corona_vaccinations.append(db.coronaVaccinations[idx])
                # implicit patient_id, db.coronaVaccinations[idx].patient_id -> corona_vaccinations {shs: shs} -> {shs: shs}
                # implicit idx -> corona_vaccinations {shs: shs} -> {shs: shs}

            idx += 1  # {shs: shs} -> {shs: shs}

        corona_vaccine = corona_vaccinations[-1]  # {shs:shs} -> {shs:shs}
        corona_test = corona_tests[-1]  # {shs:shs} -> {shs:shs}

        # # if_acts_for(retrievePatientData, patient) then
        # #   name_patient_declass = declassify(name_patient, {patient: {shs,patient}})
        # #   cpr_patient_declass = declassify(cpr_patient, {patient: shs,patient})

        # #   corona_vaccine_declass = declassify(corona_vaccine, {patient:shs})
        # #   corona_test_declass = declassify(corona_test, {patient:shs})

        corona_test_declass = corona_test
        corona_vaccine_declass = corona_vaccine

        print("patient info:")
        print(
            f"\tPrinting results for patient ID: {patient_id}\n")  # print to {shs:shs}
        print(
            f"\tName Patient: {name_patient}, \n\tCPR: {cpr_patient}\n")  # print to {patient:shs}
        print(
            f"\tLast corona test date: {corona_test_declass.date}, \n\tcorona test result: {corona_test_declass.result}\n")  # print to {patient:shs}
        print(
            f"\tLast vaccination: {corona_vaccine_declass.date}")
    else:
        print("Patient was not found")  # print to {shs: shs}


def getStats(db: Database, data_from_date: str):
    """
    db               {⊥}
    data_from_date   {⊥}
    db.coronaTests   {shs: shs}
    """

    # get amount of corona tests after data_from_date
    corona_tests = 0   # {shs: shs}
    positive_tests = 0  # {shs: shs}
    idx = 0  # {⊥}
    while idx < len(db.coronaTests):
        if db.coronaTests[idx].date > data_from_date:
            # implicit db.coronaTests[idx].date, db.coronaTests -> corona_tests {shs: shs} -> {shs: shs}
            # implicit idx, data_from_date -> corona_tests {⊥} -> {shs: shs}
            corona_tests += 1  # {shs: shs} -> {shs: shs}
            if db.coronaTests[idx].result == "paavist":
                # implicit db.coronaTests[idx].date, db.coronaTests[idx].result, db.coronaTests ->
                #   positive_tests {shs: shs} -> {shs: shs}
                # implicit idx, data_from_date -> positive_tests {⊥} -> {shs: shs}
                positive_tests += 1  # {shs: shs} -> {shs: shs}
        idx += 1  # {⊥} -> {⊥}

    # if_acts_for(getStats, shs) then
    #   corona_tests_declass = declassify(corona_tests, {⊥})
    corona_tests_declass = corona_tests
    # if_acts_for(getStats, shs) then
    #   positive_tests_declass = declassify(positive_tests, {⊥})
    positive_tests_declass = positive_tests

    # publishing to a channel with security lattice {⊥}
    print("Corona tests:")
    print(f"\tAmount of corona tests: {corona_tests_declass}")
    print(f"\tAmount of positive corona tests: {positive_tests_declass}\n")
