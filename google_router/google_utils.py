from oauth_utils.oauth_init import oauth
from fastapi import Request, HTTPException
from authlib.integrations.starlette_client import OAuthError
from init_utils.logger_init import logger
import httpx


async def get_redirect(request: Request):

    try:

        # if not request['session']:
        #
        #     raise HTTPException(status_code=400, detail='Persist Session is required')

        redirect_uri = request.url_for('google_callback')

        return await oauth.google.authorize_redirect(request, redirect_uri)


    except OAuthError as oe:

        logger.error(f'Error in OAuth Redirect {oe}')

        raise HTTPException(status_code=400, detail='Cannot Redirect with the provider')

    except HTTPException as he:

        raise he

    except Exception as e:

        logger.error(f'Unknown error in OAuth Register {e}')

        raise HTTPException(status_code=500, detail='Server Error while redirecting a connection with Provider')


async def get_callback(request: Request):

    try:

        token = await oauth.google.authorize_access_token(request)

        async with httpx.AsyncClient() as client:

            response = await client.get('https://openidconnect.googleapis.com/v1/userinfo', headers={'Authorization': f"Bearer {token['access_token']}"})

        user = response.json()

        return user

    except OAuthError as oe:

        logger.error(f'Error in OAuth callback {oe}')

        raise HTTPException(status_code=400, detail='Cannot callback with the provider')

    except HTTPException as he:

        raise he

    except Exception as e:

        logger.error(f'Unknown error in OAuth Callback {e}')

        raise HTTPException(status_code=500, detail='Server Error while callback a connection with Provider')