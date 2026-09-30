from pydantic import BaseModel,Field
from typing import Annonated,


class PRODUCT(BaseModel):
    id:Annonated[int,Field(...,description="Enter id in integer")]
    name:Annonated[str,Field(...,description="Enter the name",example="IBRAHIMKHAN")]
    description=Annonated[Optional[str],Field(default=NONE)]
    