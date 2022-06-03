from app.core.database import Base
from app.domain.shared.model_base import TimestampMixin
from sqlalchemy import JSON, Column, Integer


class SearchCondition(Base, TimestampMixin):
    __tablename__ = "search_conditions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    condition = Column(JSON, nullable=False)

    class Config:
        orm_mode = True
