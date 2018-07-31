from enum import Enum

class Environment(Enum):
    InternalDev = 1
    InternalQa = 2
    Stage = 3
    Prod = 4
    none = 5

