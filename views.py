import fastapi
from fastapi.templating import Jinja2Templates
from fastapi import Request, Form, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.requests import Request
import algo




# Setting Jinja2 templating engine
templates = Jinja2Templates('templates')

# Creating an instance of APIRouter to have path operations related to application endpoints
router = fastapi.APIRouter()

# Enabling basic HTTP authentication
security = HTTPBasic()

# Creating a database
users = {'name': [], 'pass_enc': []}



# Defining routes:

# Get requests for main page
@router.get("/")
def form_post(request: Request):
    return templates.TemplateResponse('form.html', context={'request': request})

# Post requests for main page
@router.post("/")
def form_post(request: Request, name: str = Form(...), password: str = Form(...)):

# Checking for existing users
    if name not in users['name']:

        try:
# Encrypting and encoding password before saving 
            pass_enc = algo.enc_algo(password)
            users['pass_enc'].append(pass_enc.encode())
            users['name'].append(name)
            return templates.TemplateResponse('form.html', context={'request': request, 'pass_enc': pass_enc, 'name': name})
# Catching KeyError exceptions
        except KeyError:
            msg = '''Note: A password should only consists of lowercase or uppercase letters, numbers and special characters:
                     '.', '(', ')', '-', '>', '<', '?', '!', ';', ':', '{', '}', '[', ']', ',', '"', tab, new line and space.'''
            return templates.TemplateResponse('form.html', context={'request': request, 'msg': msg})
    else:
        msg = 'Sorry, that username already exists!'
        return templates.TemplateResponse('form.html', context={'request': request, 'msg': msg})
    
# Creating function to handle authentication process
def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):

# Assigning credentials from incoming requests
    usr_name = credentials.username
    usr_pass = credentials.password

# Checking credentials matches against database
    if usr_name in users['name']:
        x = users['name'].index(usr_name)
        pass_enc = users['pass_enc'][x]

# Decrypting and decoding password before comparing with data provided by the user
        dec_pass = algo.dec_algo(pass_enc.decode())
        if dec_pass == usr_pass:
            return credentials.username

# Throwing an exception for invalid password
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect name or password",
            headers={"WWW-Authenticate": "Basic"},)

# Throwing an exception for invalid username
    raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect name or password",
                headers={"WWW-Authenticate": "Basic"},)

@router.get("/secret")
def read_current_user(request: Request, username: str = Depends(get_current_username)):
    return templates.TemplateResponse("secret.html", {'request': request})