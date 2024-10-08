from enum import Enum


class LanguageType(Enum):
    eng: str = "eng"


class OrderByType(Enum):
    created_at: str = "created_at"


class OrderType(Enum):
    asc: str = "asc"
    desc: str = "desc"
