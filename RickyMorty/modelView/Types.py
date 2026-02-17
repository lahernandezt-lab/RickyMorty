from enum import Enum

class NodeType(Enum):
    STORY = "story"
    DIALOGUE = "dialogue"
    FIGHT = "fight"
    SPECIAL = "special"
    BLANK = "blank"
    UNDEFINED = "undefined"

class Option(Enum):
    LEFT = 0
    RIGHT = 1

class Code(Enum):
    DKTMU = "Rick y Morty en la nacional"
    EXIT_0 = 0

from enum import Enum

class RickStacks(Enum):

    BATERIA_MICROVERSAL = "Batería_Microversal"
    CRISTAL_DE_CULILLOS = "Cristal_de_Culillos"  
    CHIP_ESTABILIDAD = "Chip_de_Estabilidad_Portal"
    CARGADOR_DE_PLASMA = "Cargador_de_Plasma_Verde"
    PORTAL_INESTABLE = "Portal_Inestable"
    CAJA_DE_MEESEEKS = "Caja_de_Meeseeks"
    
class ConsoleColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
