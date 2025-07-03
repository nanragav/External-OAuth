from oauth_utils.oauth_init import oauth
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from authlib.integrations.starlette_client import OAuthError
from init_utils.logger_init import logger
import httpx
from init_utils.init_config import config


async def get_redirect(request: Request):

    try:

        if not request.cookies.get('session'):

            return JSONResponse(status_code=400, content={'detail':'Persist Session is required'})

        redirect_uri = request.url_for('google_callback')

        return await oauth.google.authorize_redirect(request, redirect_uri)

    except OAuthError as oe:

        logger.error(f'Error in OAuth Redirect {oe}')

        return JSONResponse(status_code=400, content={'detail':'Cannot Redirect with the provider'})

    except Exception as e:

        logger.error(f'Unknown error in OAuth Register {e}')

        return JSONResponse(status_code=500, content={'detail':'Server Error while redirecting a connection with Provider'})


async def get_callback(request: Request):

    try:

        token = await oauth.google.authorize_access_token(request)

        async with httpx.AsyncClient() as client:

            user_response = await client.get(url=config('GOOGLE_GET_USERINFO'), headers={'Authorization': f"Bearer {token['access_token']}"})

            if user_response.status_code == 403:

                return JSONResponse(status_code=403, content={'detail':'Please grant access in Google Authorization Page'})

            if user_response.status_code != 200:

                return JSONResponse(status_code=user_response.status_code, content={'detail':'Failed to fetch User Scope. Try again'})

            user = user_response.json()

            return user

    except OAuthError as oe:

        logger.error(f'Error in OAuth callback {oe}')

        return JSONResponse(status_code=400, content={'detail':'Please allow authorize to continue'})

    except Exception as e:

        logger.error(f'Unknown error in OAuth Callback {e}')

        return JSONResponse(status_code=500, content={'detail': 'Failed with unknown Error'})