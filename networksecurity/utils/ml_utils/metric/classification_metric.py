
from sklearn.metrics import f1_score, precision_score, recall_score
from networksecurity.entity.artifact_entity import ClassificationMetricArtifact
from networksecurity.exception.exception import NetworkSecurityException
import sys

class ClassificationMetricArtifact:
    def __init__(self,
                f1_score: float,
                precision_score: float,
                recall_score: float
            ):
        self.f1_score = f1_score
        self.precision_score = precision_score
        self.recall_score = recall_score


def get_classification_score(y_true, y_pred) -> ClassificationMetricArtifact:
    """
    Computes classification metrics safely for binary or multi-class problems.
    """
    try:
        model_f1_score = f1_score(y_true, y_pred, average="weighted")
        model_precision_score = precision_score(y_true, y_pred, average="weighted")
        model_recall_score = recall_score(y_true, y_pred, average="weighted")

        return ClassificationMetricArtifact(f1_score = model_f1_score,
                        precision_score = model_precision_score,
                        recall_score = model_recall_score
        )

    except Exception as e:
        raise NetworkSecurityException(e, sys)
