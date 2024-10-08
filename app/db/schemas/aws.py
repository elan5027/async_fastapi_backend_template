from typing import Optional
from datetime import datetime
from pydantic.dataclasses import dataclass


@dataclass
class AWSReq:
    directory: str
    file_name: str
