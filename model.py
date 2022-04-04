from dataclasses import dataclass

from numpy import integer


@dataclass
class Patient:
    id: int
    name: str
    cpr: str


@dataclass
class CoronaTest:
    patient_id: int
    date: str
    result: str


@dataclass
class CoronaVaccination:
    patient_id: int
    date: str
    shot_number: int


@dataclass
class Appointment:
    patient_id: int
    date: str
    appointment: str
