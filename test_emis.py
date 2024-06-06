import pytest
from resource_services.patient_resource import format_pat_response
from resource_services.encounter_resource import format_encounter_response


@pytest.fixture
def sample_resource_patient():
    return {
        "id": "123",
        "name": [{"given": ["John"], "family": "Doe"}],
        "gender": "male",
        "birthDate": "1990-01-01",
        "maritalStatus": {"text": "Single"},
        "address": [{"city": "City", "state": "State", "country": "Country", "line": ["Address Line"]}],
        "identifier": [{"type": {"text": "Medical Record Number"}, "value": "MRN123"}]
    }


@pytest.fixture
def sample_resource_encounter():
    return {
            "id": "1",
            "status": "completed",
            "class": {"code": "AMB"},
            "type": [{"text": "Checkup"}],
            "subject": {"display": "123456qwert7890"},
            "participant": [{"individual": {"display": "Dr. Smith"}}],
            "period": {"start": "2024-06-01", "end": "2024-06-02"},
            "location": [{"location": {"display": "Hospital A"}}],
            "serviceProvider": {"display": "Clinic XYZ"}
        }


def test_patient_format(sample_resource_patient):
    patients_list = []
    patients_list = format_pat_response(sample_resource_patient)
    print(patients_list)
    assert len(patients_list) == 10
    assert patients_list == ("123", "John Doe", "male", "1990-01-01", "Single", "City", "State", "Country",
                             "Address Line", "MRN123")


def test_encounter_format(sample_resource_encounter):
    encounter_list = []
    encounter_list = format_encounter_response(sample_resource_encounter)
    print(encounter_list)
    assert len(encounter_list) == 10
    assert encounter_list == ("1", "completed", "AMB", "Checkup", "123456qwert7890", "Dr. Smith", "2024-06-01", "2024-06-02", "Hospital A", "Clinic XYZ")
