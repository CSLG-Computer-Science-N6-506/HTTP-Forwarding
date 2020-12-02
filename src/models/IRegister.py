from typing import Optional

import pydantic
from datetime import datetime
from requests import Session

class IRegister(pydantic.BaseModel):
    ip: str
    port: int
    send_time: datetime

    token: Optional[str]
