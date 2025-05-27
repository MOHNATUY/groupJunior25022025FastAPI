from http.client import responses

from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory='templates')

@router.get('/')
async def index(request: Request):
    context = {'request': request}
    response = templates.TemplateResponse('index.html', context=context)
    return response

@router.get('/login')
@router.post('/login')
async def login(request: Request, user_email: str = Form(''), password: str = Form('')):
    print(request.method,5555)
    print(F"{user_email}")
    print(F"{password}")
    context = {'request': request}
    response = templates.TemplateResponse('index.html', context=context)
    return response