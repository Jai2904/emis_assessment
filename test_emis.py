import pytest
from resource_services.patient_resource import format_pat_response


@pytest.fixture
def sample_resource():
    return {
        "id": "123",
        "name": [{"given": ["John"], "family": "Doe"}],
        "gender": "male",
        "birthDate": "1990-01-01",
        "maritalStatus": {"text": "Single"},
        "address": [{"city": "City", "state": "State", "country": "Country", "line": ["Address Line"]}],
        "identifier": [{"type": {"text": "Medical Record Number"}, "value": "MRN123"}]
    }


def test_patient_insert(sample_resource):
    patients_list = []
    patients_list = format_pat_response(sample_resource)
    print(patients_list)
    assert len(patients_list) == 10
    assert patients_list == ("123", "John Doe", "male", "1990-01-01", "Single", "City", "State", "Country",
                             "Address Line", "MRN123")
