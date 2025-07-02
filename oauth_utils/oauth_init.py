from authlib.integrations.starlette_client import OAuth, OAuthError
from init_utils.logger_init import logger
from fastapi import HTTPException
from init_utils.init_config import config

try:

    oauth = OAuth(config=config)

    new_oauth = oauth.register(
        name='google',
        client_id=config('GOOGLE_CLIENT_ID'),
        client_secret=config('GOOGLE_CLIENT_SECRET'),
        server_metadata_url=config('GOOGLE_SERVER_METADATA_URL'),
        client_kwargs={
            'scope': 'openid profile email https://www.googleapis.com/auth/drive',
            'consent': 'true'
        }
    )

except OAuthError as oe:

    logger.error(f'Error in OAuth Register {oe}')

    raise HTTPException(status_code=400, detail='Cannot Register with the provider')

except HTTPException as he:

    raise he

except Exception as e:

    logger.error(f'Unknown error in OAuth Register {e}')

    raise HTTPException(status_code=500, detail='Server Error while creating a connection with Provider')
