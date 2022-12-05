import json


def test_create_job(client):
    data = {
        "job_title": "SDE super",
        "job_company": "doogle",
        "job_company_url": "www.doogle.com",
        "job_location": "USA,NY",
        "job_description": "python",
        "job_date_posted": "2022-03-20",
    }
    response = client.post("/jobs/create-job/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["company"] == "doogle"
    assert response.json()["description"] == "python"
