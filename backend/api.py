from fastapi import APIRouter, status, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from typing import List
from database import SessionLocal
from schema import (
    ProjectSchema,
    ProjectAllocationOutputSchema,
    ProjectAllocationInputSchema,
    EmployeeSchema,
    FormDataSchema,
)
from models import ProjectAllocation, EmployeeDetail, ProjectDetail


router = APIRouter()


@router.post("/", response_model=None)
def create(project_allocation_payload: ProjectAllocationInputSchema):
    db = SessionLocal()
    try:
        pa = ProjectAllocation(
            project_id=project_allocation_payload.project_id,
            project_owner_id=project_allocation_payload.project_owner_id,
            scrum_master_id=project_allocation_payload.scrum_master_id,
            start_date=project_allocation_payload.start_date,
        )
        db.add(pa)
        for e in project_allocation_payload.developers:
            emp_obj = db.query(EmployeeDetail).filter(EmployeeDetail.id == e.id).first()
            db.add(emp_obj)
            pa.developers.append(emp_obj)
        db.commit()
        return {"message": "Project Allocation created successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=409, detail=f"Error creating project allocation - {e}"
        )
    finally:
        db.close()


@router.put("/{id}", response_model=None)
def update(project: ProjectAllocationInputSchema, id: int):
    try:
        db = SessionLocal()
        project_allocation_obj = db.query(ProjectAllocation).filter_by(id=id).first()
        if not project_allocation_obj:
            raise HTTPException(
                status_code=404, detail="Project Allocation object Not Found"
            )
        else:
            project_allocation_obj.project_id = project.project_id
            project_allocation_obj.project_owner_id = project.project_owner_id
            project_allocation_obj.scrum_master_id = project.scrum_master_id
            project_allocation_obj.start_date = project.start_date
            project_allocation_obj.developers = (
                []
            )  # removing existing value before updating
            for e in project.developers:
                emp_obj = (
                    db.query(EmployeeDetail).filter(EmployeeDetail.id == e.id).first()
                )
                db.add(emp_obj)
                project_allocation_obj.developers.append(emp_obj)
            db.commit()
            return {"message": f"Project Allocation updated with ID : {project.id}."}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        db.close()


@router.get("/{id}", response_model=ProjectAllocationOutputSchema)
async def read_allocation(id: int):
    db = SessionLocal()
    query = (
        select(ProjectAllocation)
        .where(ProjectAllocation.id == id)
        .options(
            joinedload(ProjectAllocation.project),
            joinedload(ProjectAllocation.project_owner),
            joinedload(ProjectAllocation.developers),
            joinedload(ProjectAllocation.scrum_master),
        )
    )
    result = db.execute(query).first()
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    else:
        return ProjectAllocationOutputSchema.from_orm(result[0])


@router.get("/", response_model=List[ProjectAllocationOutputSchema])
async def get_all():
    db = SessionLocal()
    query = select(ProjectAllocation).options(
        joinedload(ProjectAllocation.project),
        joinedload(ProjectAllocation.project_owner),
        joinedload(ProjectAllocation.developers),
        joinedload(ProjectAllocation.scrum_master),
    )
    results = db.execute(query).unique().scalars().all()
    return [ProjectAllocationOutputSchema.from_orm(result) for result in results]


@router.get("/get_form_iniital_data/", response_model=FormDataSchema)
async def get_form_iniital_data():
    db = SessionLocal()
    projects = db.query(ProjectDetail).all()
    employees = db.query(EmployeeDetail).all()
    return {
        "projects": [ProjectSchema.from_orm(project) for project in projects],
        "employees": [EmployeeSchema.from_orm(employee) for employee in employees],
    }


@router.delete("/{id}")
def delete_item(id):
    try:
        db = SessionLocal()
        item_to_remove = db.query(ProjectAllocation).filter_by(id=id).first()
        if not item_to_remove:
            raise HTTPException(
                status_code=404, detail="Item with this ID does not exist."
            )
        db.delete(item_to_remove)
        db.commit()
        return {"message": "Successfully deleted"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        db.close()
