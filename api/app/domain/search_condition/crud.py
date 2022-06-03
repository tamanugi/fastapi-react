from sqlalchemy.orm import Session

from . import model, schema


def create_search_condition(
    db: Session, search_condition: schema.CreateSearchCondition, user_id: int
) -> model.SearchCondition:
    entity = model.SearchCondition(**search_condition.dict(), user_id=user_id)
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


def list_search_condition(db: Session, user_id: int) -> list[model.SearchCondition]:
    return (
        db.query(model.SearchCondition)
        .filter(model.SearchCondition.user_id == user_id)
        .all()
    )


def get_search_condition(db: Session, id: int) -> model.SearchCondition | None:
    return db.get(model.SearchCondition, id)


def delete_search_condition(db: Session, entity: model.SearchCondition) -> None:
    db.delete(entity)
    db.commit
