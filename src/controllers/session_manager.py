from typing import Optional

from fastapi import APIRouter, Response, Cookie, Request

from src.models import IRegister
from src.services import DeviceService
import random, string
import requests
from functional import seq
from fastapi.templating import Jinja2Templates

view = APIRouter()

templates = Jinja2Templates(directory="./src/templates")

@view.post("/start_new_session")
@view.get("/start_new_session")
async def start_new(ip: str, port: int, response: Response, request: Request):
    if (item := DeviceService.items.get(f"{ip}:{port}")) and item.port == port:
        token = random.choices(string.ascii_letters, k=8)
        item.token = "".join(token)
        response.set_cookie(key="session_token", value=item.token)
        return {'error': ''}
    else:
        return templates.TemplateResponse("index.html", {"request": request, "error": '未找到此设备'})

        return {'error': '未找到此设备'}


@view.api_route(
    "/{path:path}",
    methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', "TRACE", "PATCH"]
)
async def root(
        path: str,
        req: Request, res: Response,
        session_token: Optional[str] = Cookie(None)
):
    devices = DeviceService.get_by_token(session_token)
    if devices:
        device = devices[0]
        result = requests.request(
            url=f"http://{device.ip}:{device.port}/{path}",
            method=req.method,
            headers=req.headers,
            data=await req.body(),
            timeout=5
        )
        header = dict(result.headers)
        for k in ["Server", "Date", 'Transfer-Encoding', 'Content-Encoding']:
            if k in header:
                header.pop(k)
        return Response(content=result.content, headers=header)
    return {"message": 'no device', "session_token": session_token, 'cookies': req.cookies}
