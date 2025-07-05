from oauth_utils.oauth_init import oauth
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from authlib.integrations.starlette_client import OAuthError
from init_utils.logger_init import logger
import httpx
from init_utils.init_config import config


async def get_redirect(request: Request):

    try:

        redirect_uri = request.url_for('google_callback')

        return await oauth.google.authorize_redirect(request, redirect_uri)

    except OAuthError as oe:

        logger.error(f'Error in OAuth Redirect {oe}')

        return JSONResponse(status_code=400, content='Cannot Redirect with the provider')

    except Exception as e:

        logger.error(f'Unknown error in OAuth Register {e}')

        return JSONResponse(status_code=500, content='Server Error while redirecting a connection with Provider')


async def get_callback(request: Request):

    try:

        token = await oauth.google.authorize_access_token(request)

        files = []

        params = {}

        async with httpx.AsyncClient() as client:

            user_response = await client.get(url=config('GOOGLE_GET_USERINFO'), headers={'Authorization': f"Bearer {token['access_token']}"})

            if user_response.status_code == 403:

                return JSONResponse(status_code=403, content='Please grant access in Google Authorization Page')

            if user_response.status_code != 200:

                return JSONResponse(status_code=user_response.status_code, content='Failed to fetch User Scope. Try again')

            user = user_response.json()

            while True:

                drive_response = await client.get(url=config('GOOGLE_DRIVE_LIST_URL'), headers={'Authorization': f"Bearer {token['access_token']}"}, params=params)

                if drive_response.status_code == 403:

                    return JSONResponse(status_code=403, content='Drive Access Denied')

                if drive_response.status_code != 200:

                    return JSONResponse(status_code=drive_response.status_code, content='Unable to Access the user Drive')

                drive = drive_response.json()

                files.extend(drive.get('files', []))

                next_page_token = drive.get("nextPageToken")

                if not next_page_token:

                    break

                params['pageToken'] = next_page_token

            return user, files

    except OAuthError as oe:

        logger.error(f'Error in OAuth callback {oe}')

        return JSONResponse(status_code=400, content='Please allow authorize to continue')

    except KeyError as ke:

        logger.error(f'Environment File does not contain the key {ke}')

        return JSONResponse(status_code=404, content='Environmental File missing the key')

    except Exception as e:

        logger.error(f'Unknown error in OAuth Callback {e}')

        return JSONResponse(status_code=500, content='Failed with unknown Error')