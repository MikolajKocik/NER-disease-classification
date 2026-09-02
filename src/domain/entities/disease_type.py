from enum import Enum

class DiseaseType(str, Enum):
    PROBLEM = "PROBLEM"
    TEST = "TEST"
    TREATMENT = "TREATMENT"