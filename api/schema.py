from dataclasses import dataclass
from typing import List
from datetime import date

@dataclass
class Patient:
    asc_number: int
    test_type: str

@dataclass
class BatchSchema:
    batch_number: int
    patients: List[Patient]
    date: date
