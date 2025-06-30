from fastapi import HTTPException, Request, APIRouter
from .google_utils import get_redirect, get_callback
from authlib.integrations.starlette_client import OAuthError
import logging

logger = logging.getLogger(__name__)

router = APIRouter(tags=['/Google OAuth'])

@router.get('/google-login')
async def google_login(request: Request):

    try:

        return await get_redirect(request=request)

    except OAuthError as oe:

        logger.error(f'Error in Google Login {oe}')

        raise HTTPException(status_code=400, detail='Cannot Login with the provider')

    except HTTPException as he:

        raise he

    except Exception as e:

        logger.error(f'Unknown error in Google Login {e}')

        raise HTTPException(status_code=500, detail='Server Error while login a connection with Provider')

@router.get('/auth/google/callback')
async def google_callback(request: Request):

    try:

        user = await get_callback(request=request)

        return user

    except OAuthError as oe:

        logger.error(f'Error in Google Callback {oe}')

        raise HTTPException(status_code=400, detail='Cannot Callback with the provider')

    except HTTPException as he:

        raise he

    except Exception as e:

        logger.error(f'Unknown error in Google Callback {e}')

        raise HTTPException(status_code=500, detail='Server Error while callback a connection with Provider')

