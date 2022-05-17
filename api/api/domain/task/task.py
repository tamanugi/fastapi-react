from datetime import datetime


class Task:
    def __init__(
        self,
        id: str,
        title: str,
        created_at: datetime = None,
        updated_at: datetime = None,
    ):
        self.id: str = id
        self.title: str = title
        self.created_at: datetime | None = created_at
        self.updated_at: datetime | None = updated_at

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Task):
            return self.id == o.id

        return False
