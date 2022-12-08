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
    assert response.json()["job_company"] == "doogle"
    assert response.json()["job_description"] == "python"


def test_read_job(client):
    data = {
        "job_title": "SDE super",
        "job_company": "doogle",
        "job_company_url": "www.doogle.com",
        "job_location": "USA,NY",
        "job_description": "python",
        "job_date_posted": "2022-03-20",
    }
    response = client.post("/jobs/create-job/", json.dumps(data))
    response = client.get("/jobs/get/1/")
    assert response.status_code == 200
    assert response.json()["job_title"] == "SDE super"
