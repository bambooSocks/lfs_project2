from dataclasses import dataclass


@dataclass
class Patient:  # {shs: shs}
    id: int     # {shs: shs}
    name: str   # {shs: shs; patient: {shs, patient}}
    cpr: str    # {shs: shs; patient: {shs, patient}}


@dataclass
class CoronaTest:    # {shs: shs}
    patient_id: int  # {shs: shs}
    date: str        # {shs: shs}
    result: str      # {shs: shs}


@dataclass
class CoronaVaccination:  # {shs: shs}
    patient_id: int       # {shs: shs}
    date: str             # {shs: shs}


@dataclass
class Appointment:    # {shs: shs}
    patient_id: int   # {shs: shs}
    date: str         # {shs: shs}
    appointment: str  # {shs: shs}
