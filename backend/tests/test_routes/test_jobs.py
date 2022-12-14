import json

from fastapi import status


def test_create_job(client, normal_user_token_headers):
    data = {
        "job_title": "SDE super",
        "job_company": "doogle",
        "job_company_url": "www.doogle.com",
        "job_location": "USA,NY",
        "job_description": "python",
        "job_date_posted": "2022-03-20",
    }
    response = client.post("/jobs/create/", json.dumps(data))
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
    response = client.post("/jobs/create/", json.dumps(data))
    response = client.get("/jobs/get/1/")
    assert response.status_code == 200
    assert response.json()["job_title"] == "SDE super"


def test_read_all_jobs(client):
    data = {
        "job_title": "SDE super",
        "job_company": "doogle",
        "job_company_url": "www.doogle.com",
        "job_location": "USA,NY",
        "job_description": "python",
        "job_date_posted": "2022-03-20",
    }
    client.post("/jobs/create/", json.dumps(data))
    client.post("/jobs/create/", json.dumps(data))

    response = client.get("/jobs/all/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_a_job(client):
    data = {
        "job_title": "SDE super",
        "job_company": "doogle",
        "job_company_url": "www.doogle.com",
        "job_location": "USA,NY",
        "job_description": "python",
        "job_date_posted": "2022-03-20",
    }
    client.post("/jobs/create/", json.dumps(data))
    data["job_title"] = "test new title"
    response = client.put("/jobs/update/1", json.dumps(data))
    assert response.json()["msg"] == "Successfully updated data."


def test_delete_a_job(client):
    data = {
        "job_title": "SDE super",
        "job_company": "doogle",
        "job_company_url": "www.doogle.com",
        "job_location": "USA,NY",
        "job_description": "python",
        "job_date_posted": "2022-03-20",
    }
    client.post("/jobs/create/", json.dumps(data))
    client.delete("/jobs/delete/1")
    response = client.get("/jobs/get/1/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
