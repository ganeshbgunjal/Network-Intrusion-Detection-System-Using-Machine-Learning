from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    """
    Represents an artifact generated during the data ingestion phase
    of a network security project.
    """
    trained_file_path: str
    test_file_path: str

@dataclass
class DataValidationArtifact:
    """
    Represents an artifact generated during the data validation phase
    of a network security project.
    """
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str
    
