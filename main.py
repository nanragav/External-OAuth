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
from generate_jwt_secret import generate_key

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

keys_dir = 'keys'

priv_path = os.path.join(keys_dir, 'private.pem')

pub_path = os.path.join(keys_dir, 'public.pem')

if not os.path.exists(keys_dir) or not os.path.isfile(priv_path) or not os.path.isfile(pub_path):

    logger.error("🔔 Missing Jwt Secrets Private Key and Public Key. Generating new keys...")

    generate_key()

else:

    logger.error("✅ Keys already exist. Skipping generation.")

load_dotenv()

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key=config('SESSION_COOKIE_SECRET'))

app.include_router(google_login.router)


@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>OAuth Login Page</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                background-color: #f0f2f5;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                padding: 20px;
                box-sizing: border-box;
            }
            .login-container {
                background-color: white;
                border-radius: 12px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                padding: 40px;
                text-align: center;
                max-width: 400px;
                width: 100%;
            }
            .login-title {
                color: #333;
                margin-bottom: 30px;
                font-size: 24px;
                font-weight: 500;
            }
            .google-login-btn {
                display: flex;
                align-items: center;
                justify-content: center;
                background-color: #4285f4;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 24px;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s ease;
                width: 90%;
                text-decoration: none;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            .google-login-btn:hover {
                background-color: #357ae8;
            }
            .google-login-btn img {
                width: 24px;
                height: 24px;
                margin-right: 12px;
            }
            .additional-info {
                margin-top: 20px;
                color: #666;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <div class="login-container">
            <h1 class="login-title">Welcome to OAuth Login</h1>

            <a href='/google-login' class="google-login-btn">
                Login with Google
            </a>

            <div class="additional-info">
                <p>Secure login using Google OAuth 2.0</p>
            </div>
        </div>

        <script>
            document.querySelector('.google-login-btn').addEventListener('mouseenter', function() {
                this.style.transform = 'scale(1.05)';
            });
         
            document.querySelector('.google-login-btn').addEventListener('mouseleave', function() {
                this.style.transform = 'scale(1)';
            });
        </script>
    </body>
    </html>
    '''


if __name__ == '__main__':

    uvicorn.run(app='main:app', host='0.0.0.0', port=8000, ssl_keyfile=ssl_keyfile, ssl_certfile=ssl_certfile)