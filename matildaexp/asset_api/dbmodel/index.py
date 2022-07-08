from sqlmodel import Field, SQLModel


class Index(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    value: float
