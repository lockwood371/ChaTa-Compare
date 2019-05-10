from app.db.base_class import Base
from app.enums.chart_type import ChartType
from sqlalchemy import Column, Integer, String, Enum


class Chart(Base):
    id = Column(Integer, primary_key=True, index=True)
    filepath = Column(String(120))
    type = Column(Enum(ChartType), index=True)
    title = Column(String(200), index=True)
    x_axis_title = Column(String(200), index=True)
    y_axis_title = Column(String(200), index=True)
    description = Column(String(4000), index=True)