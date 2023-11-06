from pydantic import BaseModel
from typing import List, Union


class EmployeeSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ProjectSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ProjectAllocationDetailOutputSchema(BaseModel):
    id: int
    project: ProjectSchema
    project_owner: EmployeeSchema
    developers: List[EmployeeSchema]
    scrum_master: EmployeeSchema
    start_date: str
    # methodology: str
    # location: str

    class Config:
        orm_mode = True


class ProjectAllocationOutputSchema(ProjectAllocationDetailOutputSchema):
    developers: List[EmployeeSchema]


class EmployeeInputSchema(BaseModel):
    id: int


class ProjectAllocationInputSchema(BaseModel):
    id: Union[int,None]
    project_id: int
    project_owner_id: int
    developers: List[EmployeeInputSchema]
    scrum_master_id: int
    start_date: str

class FormDataSchema(BaseModel):
    employees: List[EmployeeSchema]
    projects: List[ProjectSchema]

    class Config:
        orm_mode = True
        
