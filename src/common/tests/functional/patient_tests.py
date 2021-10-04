from django.urls import reverse


def test_patient_list(db, user, doctor_client, diagnoses) -> None:
    path = reverse(viewname='patients-list')
    response = doctor_client.get(path=path)
    assert response.status_code == 200
    json_response = response.json()
    assert json_response['count'] == 1
    assert len(json_response['results'][0]['diagnoses']) == 3
    keys = ('id', 'date_of_birth', 'diagnoses', 'created_at')
    for key in keys:
        assert key in json_response['results'][0]
