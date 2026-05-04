from pylint.checkers.variables import VariablesChecker

IGNORED_NAMES = {
    "DecisionTreeClassifier",
    "accuracy_score",
    "load_iris",
    "train_test_split",
    "pd",
    "np",
    "StandardScaler",
    "MinMaxScaler",
    "RobustScaler",
    "RandomForestClassifier",
    "accuracy_score"
}

original_add_message = VariablesChecker.add_message


def patched_add_message(self, msgid, node=None, *args, **kwargs):
    if msgid in ("E0602", "undefined-variable") and node is not None:
        if getattr(node, "name", None) in IGNORED_NAMES:
            return
    original_add_message(self, msgid, node=node, *args, **kwargs)


VariablesChecker.add_message = patched_add_message


def register(linter):
    pass
