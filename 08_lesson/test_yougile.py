from dotenv import load_dotenv
from YouGile import YouGile


yg = YouGile()
load_dotenv()


def test_add_new_project():
    title = "Autotest"
    resp = yg.create_project(title)
    assert resp.status_code == 201


def test_add_new_project_neg():
    title = ""
    resp = yg.create_project(title)
    assert resp.status_code == 400
    assert "title should not be empty" in resp.json().get("message", "")


def test_get_project_id():
    title = "NewAutotest"
    result = yg.create_project(title)
    new_id = result.json().get("id")
    new_project = yg.get_project_id(new_id)
    assert new_project.status_code == 200
    assert new_project.json()["id"] == new_id


def test_get_project_id_neg():
    title = "NewAutotest"
    yg.create_project(title)
    new_project = yg.get_project_id("new_id")
    assert new_project.status_code == 404
    assert "Проект не найден" in new_project.json().get("message", "")


def test_put_project():
    title = "NewAutotest"
    result = yg.create_project(title)
    new_id = result.json().get("id")
    new_title = "OldAutotest"
    new_project = yg.put_project_id(new_id, new_title)
    updated_project = yg.get_project_id(new_id)
    assert new_project.status_code == 200
    assert new_project.json()["id"] == new_id
    assert updated_project.status_code == 200
    assert updated_project.json()["id"] == new_id
    assert updated_project.json()["title"] == new_title


def test_put_project_neg():
    title = "NewAutotest"
    result = yg.create_project(title)
    new_id = result.json().get("id")
    new_title = ""
    new_project = yg.put_project_id(new_id, new_title)
    assert new_project.status_code == 400
    assert "title should not be empty" in new_project.json().get("message", "")
