from dataclasses import dataclass


@dataclass
class Patient:  # {⊥}
    id: int     # {shs: shs}
    name: str   # {shs: shs; patient: {shs, patient}}
    cpr: str    # {shs: shs; patient: {shs, patient}}


@dataclass
class CoronaTest:    # {⊥}
    patient_id: int  # {shs: shs}
    date: str        # {shs: shs}
    result: str      # {shs: shs}


@dataclass
class CoronaVaccination:  # {⊥}
    patient_id: int       # {shs: shs}
    date: str             # {shs: shs}


@dataclass
class Appointment:    # {⊥}
    patient_id: int   # {shs: shs}
    date: str         # {shs: shs}
    appointment: str  # {shs: shs}
