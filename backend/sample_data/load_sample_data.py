import json
from database import SessionLocal
from models import EmployeeDetail, ProjectDetail


def load_employee_sample_data():
    with open("sample_data/employee_list.json", "r") as json_file:
        data = json.load(json_file)
    db = SessionLocal()
    for each in data:
        employee = EmployeeDetail(name=each["name"])
        db.add(employee)
    db.commit()
    return {"message": "Employee Data loaded successfully."}


def load_project_sample_data():
    with open("sample_data/project_list.json", "r") as json_file:
        data = json.load(json_file)
    db = SessionLocal()
    for each in data["data"]:
        project = ProjectDetail(name=each["projectName"])
        db.add(project)
    db.commit()
    return {"message": "Project Data loaded successfully."}


def load_data():
    db = SessionLocal()
    created_project = created_employee = None
    projects = db.query(ProjectDetail).all()
    if not projects:
        created_project = load_project_sample_data()
    employees = db.query(EmployeeDetail).all()
    if not employees:
        created_employee = load_employee_sample_data()
    print(created_employee, created_project)
