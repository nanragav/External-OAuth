from fastapi import HTTPException, Request, APIRouter, Depends
from starlette.responses import JSONResponse
from oauth_utils.oauth_init import oauth
from .google_utils import get_redirect, get_callback
from authlib.integrations.starlette_client import OAuthError
from init_utils.logger_init import logger
from fastapi.responses import RedirectResponse, HTMLResponse
import json
from json import JSONDecodeError
from crud_utils.crud import adduserinfo
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(tags=['/Google OAuth'])

@router.get('/google-login')
async def google_login(request: Request):

    try:

        return await get_redirect(request=request)

    except OAuthError as oe:

        logger.error(f'Error in Google Login {oe}')

        raise HTTPException(status_code=400, detail='Cannot Login with the provider')

    except KeyError as ke:

        logger.error(f'Used key {ke} is not found')

        raise HTTPException(status_code=404, detail='The key is not found')

    except HTTPException as he:

        raise he

    except Exception as e:

        logger.error(f'Unknown error in Google Login {e}')

        raise HTTPException(status_code=500, detail='Server Error while login a connection with Provider')

@router.get('/auth/google/callback')
async def google_callback(request: Request, db: AsyncSession = Depends(get_db)):

    try:

        user, drive = await get_callback(request=request)

        if isinstance(user, JSONResponse):
            error_details = {
                "error_type": "Google Authorization Error",
                "message": user.body.decode('utf-8')
            }

            return RedirectResponse(
                url=f'/google/error?error={json.dumps(error_details)}',  # In the Future, I will enhance this with the redis id to reference the error to display
                status_code=303
            )

        if isinstance(drive, JSONResponse):
            error_details = {
                "error_type": "Google Authorization Error",
                "message": drive.body.decode('utf-8')
            }

            return RedirectResponse(
                url=f'/google/error?error={json.dumps(error_details)}',  # In the Future, I will enhance this with the redis id to reference the error to display
                status_code=303
            )

        if not user.get('phone_number'):

            error_details = {'error_type': 'Detail Missing', 'message': 'Phone Number is Missing'}

            return RedirectResponse(
                url=f'/google/error?error={json.dumps(error_details)}', status_code=303
            )

        if not user.get('email_verified'):

            error_details = {'error_type': 'Not Verified', 'message': 'Email is not verified'}

            return RedirectResponse(
                url=f'/google/error?error={json.dumps(error_details)}', status_code=303
            )

        return user, drive

    except OAuthError as oe:

        logger.error(f'Error in Google Callback {oe}')

        raise HTTPException(status_code=400, detail='Cannot Callback with the provider')

    except KeyError as ke:

        logger.error(f'Used key {ke} is not found')

        raise HTTPException(status_code=404, detail='The key is not found')

    except HTTPException as he:

        raise he

    except Exception as e:

        logger.error(f'Unknown error in Google Callback {e}')

        raise HTTPException(status_code=500, detail='Server Error while callback a connection with Provider')

@router.get('/google/error', response_class=HTMLResponse)
async def google_error(request: Request, error: str = None):

    try:

        error_details = {
            "error_type": "Unknown",
            "message": "No specific error details available."
        }

        if error:
            try:
                error_details = json.loads(error)
                if not isinstance(error_details, dict):
                    # raise ValueError("Parsed error is not a dictionary.")
                    error_details = {
                        "error_type": "Invalid Error Type",
                        "message": "Parsed error is not a dictionary."
                    }
            except (JSONDecodeError, ValueError) as parse_err:
                logger.warning(f"Invalid error query parameter: {error} — {parse_err}")
                error_details = {
                    "error_type": "Malformed Error Parameter",
                    "message": "The error information provided is not in a valid format."
                }

        return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Google OAuth Error</title>
            <style>
                body {{ 
                    font-family: Arial, sans-serif; 
                    max-width: 600px; 
                    margin: 0 auto; 
                    padding: 20px; 
                    background-color: #f4f4f4;
                    line-height: 1.6;
                }}
                .error-container {{
                    background-color: white;
                    border-radius: 8px;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    padding: 30px;
                    margin-top: 50px;
                }}
                .error-box {{ 
                    background-color: #f8d7da; 
                    color: #721c24; 
                    padding: 15px; 
                    border-radius: 5px; 
                    margin-top: 20px; 
                    border: 1px solid #f5c6cb;
                }}
                h1 {{
                    color: #333;
                    text-align: center;
                    border-bottom: 2px solid #e0e0e0;
                    padding-bottom: 15px;
                }}
                .error-type {{
                    font-weight: bold;
                    color: #d9534f;
                    margin-bottom: 10px;
                }}
                .error-message {{
                    color: #721c24;
                }}
                .actions {{
                    margin-top: 30px;
                    text-align: center;
                }}
                .btn {{
                    display: inline-block;
                    padding: 10px 20px;
                    background-color: #007bff;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    transition: background-color 0.3s ease;
                }}
                .btn:hover {{
                    background-color: #0056b3;
                }}
            </style>
        </head>
        <body>
            <div class="error-container">
                <h1>Google OAuth Error</h1>
                <div class="error-box">
                    <div class="error-type">
                        Error Type: {error_details.get('error_type', 'Unknown Error')}
                    </div>
                    <div class="error-message">
                        {error_details.get('message', 'An unexpected error occurred')}
                    </div>
                </div>
                <div class="actions">
                    <a href="/google-login" class="btn">Try Again</a>
                    <a href="/" class="btn" style="background-color: #6c757d;">Return to Home</a>
                </div>
            </div>
        </body>
        </html>
        '''

    except OAuthError as oe:

        logger.error(f'Error in Google Error {oe}')

        raise HTTPException(status_code=400, detail='Cannot handle with the error')

    except KeyError as ke:

        logger.error(f'Used key {ke} is not found')

        raise HTTPException(status_code=404, detail='The key is not found')

    except HTTPException as he:

        raise he

    except Exception as e:

        logger.error(f'Unknown error in Google Error {e}')

        raise HTTPException(status_code=500, detail='Server Error while handling the error')
