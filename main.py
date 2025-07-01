from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from starlette.middleware.sessions import SessionMiddleware
from init_utils.init_config import config
from dotenv import load_dotenv
import os
from google_router import google_login
import uvicorn
from init_utils.logger_init import logger
from generate_cert import cert_gen

certs_dir = "certs"
key_path = os.path.join(certs_dir, "key.pem")
cert_path = os.path.join(certs_dir, "cert.pem")

# Check if certs folder or files are missing
if not os.path.exists(certs_dir) or not os.path.isfile(key_path) or not os.path.isfile(cert_path):
    logger.error("🔔 Certs folder or key/cert files missing. Generating new certificates...")
    cert_gen()
else:
    logger.error("✅ Certificates already exist. Skipping generation.")

current_dir = os.path.dirname(os.path.abspath(__file__))

ssl_keyfile = os.path.join(current_dir, 'certs', 'key.pem')

ssl_certfile = os.path.join(current_dir, 'certs', 'cert.pem')

load_dotenv()

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key=config('SESSION_COOKIE_SECRET'))

app.include_router(google_login.router)

@app.get('/', response_class=HTMLResponse)
async def root(request: Request):

    return '''
    <a href='/google-login'>Login with Google</a>'''

if __name__ == '__main__':

    uvicorn.run(app='main:app', host='0.0.0.0', port=8000, reload=True, ssl_keyfile=ssl_keyfile, ssl_certfile=ssl_certfile)