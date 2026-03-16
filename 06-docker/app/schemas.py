from pydantic import BaseModel, Field

class NumberBase(BaseModel):
    value: int = Field(..., ge=0, le=1_000_000)

class NumberCreate(NumberBase):
    pass

class NumberUpdate(NumberBase):
    pass

class NumberResponse(NumberBase):
    id: int

    class Config:
        from_attributes = True
