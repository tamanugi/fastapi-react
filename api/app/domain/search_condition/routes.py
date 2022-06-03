from app.core.database import get_db
from app.domain.search_condition.schema import (
    CreateSearchCondition,
    SearchConditionRead,
    SearchConditionResponse,
)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud as search_condition_crud

router = APIRouter(prefix="/search_conditions", tags=["search"])


@router.get("/", response_model=SearchConditionResponse)
def list_search_conditions(db: Session = Depends(get_db)) -> SearchConditionResponse:
    entities = search_condition_crud.list_search_condition(db, user_id=1)

    conditions = [SearchConditionRead(id=v.id, condition=v.condition) for v in entities]
    return SearchConditionResponse(conditions=conditions)


@router.post("/", response_model=SearchConditionRead)
def create_search_conditions(
    search_condition: CreateSearchCondition, db: Session = Depends(get_db)
) -> SearchConditionRead:
    entity = search_condition_crud.create_search_condition(
        db,
        search_condition=search_condition,
        # TODO: implemnent user_id with Authentication
        user_id=1,
    )

    return SearchConditionRead(id=entity.id, condition=entity.condition)


@router.delete("/{id}")
def delete_search_conditions(id: int, db: Session = Depends(get_db)) -> None:
    entity = search_condition_crud.get_search_condition(db, id=id)

    if entity is None:
        raise HTTPException(status_code=404, detail="指定された検索条件が存在していません")

    search_condition_crud.delete_search_condition(db, entity=entity)
