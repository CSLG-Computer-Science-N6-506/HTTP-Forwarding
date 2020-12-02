from fastapi import APIRouter

from src.models import IRegister
from src.services import DeviceService

view = APIRouter()


@view.post('/set')
def register(item: IRegister):
    return DeviceService.save(item)


@view.get('/get')
def register():
    return DeviceService.items
