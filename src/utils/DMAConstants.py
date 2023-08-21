import os
# GENERAL
SUCCESS = 0
FAIL = 1
# DEFAULTS
DEFAULT_SEC = "defaults"
HOME = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", '..'))
SRC = os.path.join(HOME , "src")
# DATA
DATA_SEC = "data"
DATA = os.path.join(SRC , "data")
DATASET = os.path.join(DATA, "dataset")
PREPROCESSING = os.path.join(DATA , "preprocessing")
PREPROCESSORS = os.path.join(PREPROCESSING , "preprocssors")
DISRUPTORS = os.path.join(PREPROCESSING , "disruptors")
# DECISION_MAKING
DECISION_MAKING_SEC = "decision_making"
DECISION_MAKING = os.path.join(SRC , "decision_making")
ACTIONS = os.path.join(DECISION_MAKING , "actions")
MECHANISMS = os.path.join(DECISION_MAKING , "mechanisms")
PERFORMANCE_MEASUREMENTS = os.path.join(DECISION_MAKING , "performance_measurements")
# RESULTS
RESULTS_SEC = "results"
RESULTS = os.path.join(SRC , "results")
DUMPS = os.path.join(RESULTS , "dump")
# INI CONFS
INI_FILE_PATH = os.path.join(SRC, "utils", "confs.ini")
LEVEL_1_SECTIONS = [DEFAULT_SEC, DATA_SEC, DECISION_MAKING_SEC, RESULTS_SEC]
DATA_DATASET_PATH_INI = "data.dataset.input.path"
RESULTS_DUMPS_PATH_INI = "results.dumps.path"
SPLIT_DATA_VALUE_INI = "data.data_split"

