from datetime import datetime
from database import Base
from sqlalchemy import (
    Column,
    String,
    Boolean,
    Integer,
    ForeignKey,
    Table,
    TIMESTAMP,
    text,
    event,
)
from sqlalchemy.orm import relationship

# from sqlalchemy import event
# from sqlalchemy.orm import Session
# from models import ProjectAllocation, ActivityLog


association_table = Table(
    "association_table",
    Base.metadata,
    Column("employee_id", Integer, ForeignKey("EmployeeDetail.id")),
    Column("projectallocation_id", Integer, ForeignKey("ProjectAllocation.id")),
)


class EmployeeDetail(Base):
    __tablename__ = "EmployeeDetail"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class ProjectDetail(Base):
    __tablename__ = "ProjectDetail"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


# class ProjectAllocation(Base):
#     __tablename__ = "ProjectAllocation"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     project = Column(ForeignKey("ProjectDetail.id"), nullable=False)
#     # developers: Mapped[List[EmployeeDetail]] = relationship(secondary=association_table)
#     developers = relationship(
#         "EmployeeDetail", secondary=association_table, backref="EmployeeDetail"
#     )
#     project_owner = Column(ForeignKey("EmployeeDetail.id"), nullable=False)
#     scrum_master = Column(ForeignKey("EmployeeDetail.id"), nullable=False)
#     start_date = Column(String)
class ProjectAllocation(Base):
    __tablename__ = "ProjectAllocation"
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("ProjectDetail.id"), nullable=False)
    project = relationship("ProjectDetail", back_populates="allocations")
    developers = relationship("EmployeeDetail", secondary=association_table)
    project_owner_id = Column(Integer, ForeignKey("EmployeeDetail.id"), nullable=False)
    project_owner = relationship("EmployeeDetail", foreign_keys=[project_owner_id])
    scrum_master_id = Column(Integer, ForeignKey("EmployeeDetail.id"), nullable=False)
    scrum_master = relationship("EmployeeDetail", foreign_keys=[scrum_master_id])
    start_date = Column(String)


class ActivityLog(Base):
    __tablename__ = "ActivityLog"
    id = Column(Integer, primary_key=True, autoincrement=True)
    activity = Column(String)
    timestamp = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )


ProjectDetail.allocations = relationship("ProjectAllocation", back_populates="project")


# Define an event listener for the 'after_insert' event on ProjectAllocation
@event.listens_for(ProjectAllocation, "after_insert")
def receive_after_insert(mapper, connection, target):
    # Create an insert statement for ActivityLog
    insert_stmt = ActivityLog.__table__.insert().values(
        activity=f"ProjectAllocation created with id {target.id}",
        timestamp=datetime.utcnow(),
    )

    # Execute the statement with the connection
    connection.execute(insert_stmt)
