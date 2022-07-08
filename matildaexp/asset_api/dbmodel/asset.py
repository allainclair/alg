from sqlmodel import Field, SQLModel


class Asset(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    ir: float
    fix_interest: float
    duration: int  # Years
    id_index: float
