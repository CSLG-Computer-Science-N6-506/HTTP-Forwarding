from src.models import IRegister
from collections import defaultdict


class DeviceService:
    items: dict[str, IRegister] = {}

    def __init__(self):
        pass

    @staticmethod
    def _build_key(item: IRegister):
        return f"{item.ip}:{item.port}"

    @classmethod
    def save(cls, item: IRegister):
        cls.items[cls._build_key(item)] = item
        return item

    @classmethod
    def get_by_token(cls, token: str):
        return [i for i in cls.items.values() if i.token and i.token == token]
