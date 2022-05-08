from model import Appointment, CoronaTest, CoronaVaccination, Patient
from db_access import Database


def bookAppointment(patient: Patient, date: str, appointment_type: str, db: Database):
    """
        patient          {⊥}
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
            # explicit True -> isInDB {⊥} -> {shs: shs}
            # implicit db.patients -> isInDB {shs: shs} -> {shs: shs}
            # implicit patient, i -> isInDB {⊥} -> {shs: shs}
            break
        i += 1  # explicit i -> i {⊥} -> {⊥}

    print("Booking appointment:")
    print("\t\u001b[31m-- Printed to shs --\u001b[0m")
    if isInDB:
        # printed to {shs: shs}
        print("\tPatient exists, new appointment booked")
        db.appointments.append(Appointment(patient.id, date, appointment_type))
        # implicit patient.id, date, appointment_type, isInDB -> db.appointment {shs: shs} -> {shs: shs}
    else:
        # printed to {shs: shs}
        print("\tPatient does not exist, no appointment booked")


def uploadTestResult(patient_id: int, uploadDate: str, result: str, db: Database):
    '''
        patient_id {shs: shs}
        uploadDate {shs: shs}
        result     {shs: shs}
        db         {⊥}
    '''
    db.coronaTests.append(CoronaTest(patient_id, uploadDate, result))
    # implicit patient_id, uploadDate, result -> db.coronaTests {shs: shs} -> {shs: shs}


def updateVaccinationStatus(patient_id: int, uploadDate: str, db: Database):
    '''
        patient_id {shs: shs}
        uploadDate {shs: shs}
        db         {⊥}
    '''
    db.coronaVaccinations.append(CoronaVaccination(patient_id, uploadDate))
    # implicit patient_id, uploadDate -> db.coronaVaccinations {shs: shs} -> {shs: shs}


def retrievePatientData(patient_id: int, db: Database):
    """
    patient_id       {shs: shs}
    db               {⊥}
    """

    isInDB = False  # {shs: shs}
    i = 0  # {⊥}
    name_patient = ""  # {shs: shs, patient: {shs, patient}}
    cpr_patient = ""  # {shs: shs, patient: {shs, patient}}
    while i < len(db.patients):
        if db.patients[i].id == patient_id:
            isInDB = True
            # explicit True -> isInDB {⊥} -> {shs: shs}
            # implicit patient_id, db.patients, db.patients[i].id -> isInDB {shs: shs} -> {shs: shs}
            # implicit i -> isInDB {⊥} -> {shs: shs}
            name_patient = db.patients[i].name
            # explicit db.patients[i].name -> name_patient {shs: shs, patient: {patient, shs}} -> {shs: shs, patient: {patient, shs}}
            # implicit patient_id, db.patients, db.patients[i].id  -> name_patient {shs: shs} -> {shs: shs, patient: {patient, shs}}
            # implicit i -> name_patient {⊥} -> {shs: shs, patient: {patient, shs}}
            cpr_patient = db.patients[i].cpr
            # explicit db.patients[i].cpr -> cpr_patient {shs: shs, patient: {patient, shs}} -> {shs: shs, patient: {patient, shs}}
            # implicit patient_id, db.patients, db.patients[i].id -> cpr_patient {shs: shs} -> {shs: shs, patient: {patient, shs}}
            # implicit i -> cpr_patient {⊥} -> {shs: shs, patient: {patient, shs}}
            break
        i += 1  # {⊥} -> {⊥}

    isInDB_declass = False  # {⊥}
    # if_acts_for(bookAppointment, shs) then
    #   isInDB_declass = declassify(isInDB, {⊥})
    isInDB_declass = isInDB

    if isInDB_declass:

        corona_tests = []  # {shs: shs}
        # implicit isInDB_declass -> corona_tests {⊥} -> {shs:shs}
        idx = 0  # {⊥}
        # implicit isInDB_declass -> idx {⊥} -> {⊥}
        while idx < len(db.coronaTests):
            if db.coronaTests[idx].patient_id == patient_id:
                corona_tests.append(db.coronaTests[idx])
                # implicit db.coronaTests[idx], patient_id, db.coronaTests, db.coronaTests[idx].patient_id -> corona_tests {shs: shs} -> {shs: shs}
                # implicit idx -> corona_tests {⊥} -> {shs: shs}
            idx += 1  # explicit idx -> idx {⊥} -> {⊥}

        corona_vaccinations = []  # {shs: shs}
        # implicit isInDB_declass -> corona_vaccinations {⊥} -> {shs:shs}
        idx = 0  # {⊥}
        # implicit isInDB_declass -> idx {⊥} -> {⊥}
        while idx < len(db.coronaVaccinations):
            if db.coronaVaccinations[idx].patient_id == patient_id:
                corona_vaccinations.append(db.coronaVaccinations[idx])
                # implicit db.coronaVaccinations[idx], patient_id, db.coronaVaccinations, db.coronaVaccinations[idx].patient_id -> corona_vaccinations {shs: shs} -> {shs: shs}
                # implicit idx -> corona_vaccinations {⊥} -> {shs: shs}
            idx += 1  # {⊥} -> {⊥}

        last_corona_test = corona_tests[-1]
        # explicit corona_tests[-1] -> last_corona_test {shs:shs} -> {shs:shs}
        # implicit isInDB_declass -> last_corona_test {⊥} -> {shs:shs}
        last_corona_vaccine = corona_vaccinations[-1]
        # explicit corona_vaccinations[-1] -> last_corona_vaccine {shs:shs} -> {shs:shs}
        # implicit isInDB_declass -> last_corona_vaccine {⊥} -> {shs:shs}

        name_patient_declass = ""  # {patient: {shs, patient}}
        cpr_patient_declass = ""  # {patient: {shs, patient}}
        # if_acts_for(retrievePatientData, shs) then
        #   name_patient_declass = declassify(name_patient, {patient: {shs, patient}})
        #   cpr_patient_declass = declassify(cpr_patient, {patient: {shs, patient}})
        name_patient_declass = name_patient
        cpr_patient_declass = cpr_patient

        last_corona_test_declass = None  # {patient: {shs, patient}}
        last_corona_vaccine_declass = None  # {patient: {shs, patient}}
        # if_acts_for(retrievePatientData, shs) then
        #   last_corona_test_declass = declassify(last_corona_test, {⊥})
        #   last_corona_vaccine_declass = declassify(last_corona_vaccine, {⊥})
        last_corona_test_declass = last_corona_test
        last_corona_vaccine_declass = last_corona_vaccine

        print("Patient info:")
        print("\t\u001b[31m-- Printed to shs --\u001b[0m")
        print(
            f"\tPrinting results for patient ID: {patient_id}\n")  # print to {shs:shs}
        print("\t\u001b[32m-- Printed to patient --\u001b[0m")
        print(
            f"\tName Patient: {name_patient_declass}, \n\tCPR: {cpr_patient_declass}\n")  # print to {patient: {patient, shs}}
        print(
            f"\tLast corona test date: {last_corona_test_declass.date}, \n\tcorona test result: {last_corona_test_declass.result}\n")  # print to {patient: {patient, shs}}
        print(
            f"\tLast vaccination: {last_corona_vaccine_declass.date}")  # print to {patient: {patient, shs}}
    else:
        print("\u001b[31m-- Printed to shs --\u001b[0m")
        print("Patient was not found")  # print to {shs: shs}


def getStats(db: Database, data_from_date: str):
    """
    db               {⊥}
    data_from_date   {⊥}
    """

    # get amount of corona tests after data_from_date
    corona_tests = 0   # {shs: shs}
    positive_tests = 0  # {shs: shs}
    idx = 0  # {⊥}
    while idx < len(db.coronaTests):
        if db.coronaTests[idx].date > data_from_date:
            corona_tests += 1
            # explicit corona_tests -> corona_tests {shs: shs} -> {shs: shs}
            # implicit db.coronaTests[idx].date, db.coronaTests -> corona_tests {shs: shs} -> {shs: shs}
            # implicit idx, data_from_date -> corona_tests {⊥} -> {shs: shs}
            if db.coronaTests[idx].result == "paavist":
                positive_tests += 1
                # explicit positive_tests -> positive_tests {shs: shs} -> {shs: shs}
                # implicit db.coronaTests[idx].date, db.coronaTests[idx].result, db.coronaTests ->
                #   positive_tests {shs: shs} -> {shs: shs}
                # implicit idx, data_from_date -> positive_tests {⊥} -> {shs: shs}
        idx += 1
        # explicit idx -> idx {⊥} -> {⊥}

    corona_tests_declass = 0  # {⊥}
    # if_acts_for(getStats, shs) then
    #   corona_tests_declass = declassify(corona_tests, {⊥})
    corona_tests_declass = corona_tests

    positive_tests_declass = 0  # {⊥}
    # if_acts_for(getStats, shs) then
    #   positive_tests_declass = declassify(positive_tests, {⊥})
    positive_tests_declass = positive_tests

    # publishing to a channel with security lattice {⊥}
    print("Corona tests:")
    print("\t\u001b[34m-- Printed to public --\u001b[0m")
    print(f"\tAmount of corona tests: {corona_tests_declass}")
    # printed to {⊥}
    print(f"\tAmount of positive corona tests: {positive_tests_declass}\n")
    # printed to {⊥}
