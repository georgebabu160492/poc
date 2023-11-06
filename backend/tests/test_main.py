import json
from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_get_all_products():
    """
    Test case to check if all required products are added to db
    """
    response = client.get("/get_form_iniital_data")
    assert response.status_code == 200


def test_update_product():
    """
    To check if update a product is working correctly
    """
    data = {
        "id": 1,
        "project_id": 1,
        "project_owner_id": 1,
        "developers": [{"id": 13}, {"id": 12}],
        "scrum_master_id": 2,
        "start_date": "2020/12/20",
    }
    response = client.put("/api/project/1/", content=json.dumps(data))
    assert response.status_code == 200


def test_update_product_failure():
    """
    To check if update will fail if the ID values doesn't match in URL and data
    """
    data = {
        "id": 1,
        "project_id": 1,
        "project_owner_id": 1,
        "developers": [{"id": 10}, {"id": 11}],
        "scrum_master_id": 2,
        "start_date": "2020/12/20",
    }
    response = client.put("/api/project/2/", content=json.dumps(data))
    assert response.status_code == 404


def test_create_product():
    data = {
        "project_id": 1,
        "project_owner_id": 1,
        "developers": [{"id": 10}, {"id": 11}],
        "scrum_master_id": 2,
        "start_date": "2020/12/20",
    }
    response = client.post("/api/project", content=json.dumps(data))
    assert response.status_code == 200


def test_create_product_failure():
    """
    To check if the method is wrong will it work or not
    """
    data = {
        "id": 1,
        "project_id": 1,
        "project_owner_id": 1,
        "developers": [{"id": 10}, {"id": 11}],
        "scrum_master_id": 2,
        "start_date": "2020/12/20",
    }
    response = client.put("/api/project", content=json.dumps(data))
    assert response.status_code == 405


def test_product_delete():
    """
    To check if delete works or not
    """
    response = client.delete("/api/project/1")
    assert response.status_code == 200


def test_delete_product_wrong_id():
    """
    To check if we change the ID of an product it works or not
    """
    response = client.delete("/api/project/111")
    assert response.status_code == 404


def test_delete_product_wrong_method():
    """
    To check if we change the method type of an product it works or not
    """
    response = client.post("/api/project/111")
    assert response.status_code == 405


def test_delete_product_wrong_url():
    """
    To check if we change the url of an product it works or not
    """
    response = client.delete("/api/projet/111")
    assert response.status_code == 404
