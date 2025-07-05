from jose import jwt, JWTError
from cryptography.exceptions import InvalidSignature
import os
from init_utils.init_config import config
from datetime import datetime, timedelta, UTC
from init_utils.logger_init import logger
from fastapi import HTTPException, status

current_dir = os.path.dirname(os.path.abspath(__file__))

priv_key_path = os.path.abspath(os.path.join(current_dir, '../keys/private.pem'))

pub_key_path = os.path.abspath(os.path.join(current_dir, '../keys/public.pem'))

async def generate_access_token(data: dict):

    try:
        to_encode = data.copy()

        expire = datetime.now(UTC) + timedelta(minutes=int(config('ACCESS_TOKEN_EXPIRE')))

        to_encode.update({'exp': expire})

        with open(priv_key_path, 'rb') as f:

            priv_key = f.read().__str__()

        return jwt.encode(to_encode, key=priv_key, algorithm=config('ALGORITHM'))

    except JWTError as e:

        logger.error(f"JWT error during encoding: {e}")

        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Error while token creation')

    except InvalidSignature as e:

        logger.error(f"Invalid signature while signing token: {e}")

        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='Signature Verification Failed')

    except ValueError as e:

        logger.error(f"Value error during token generation: {e}")

        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Detail mismatched')

    except HTTPException as he:

        raise he

    except Exception as e:

        logger.error(f"Unexpected error in generate_access_token: {e}")

        raise HTTPException(status_code=500, detail='Internal Server Error')


async def decode_access_token(token: str):

    try:

        with open(pub_key_path, 'rb') as f:

            pub_key = f.read().__str__()

        return jwt.decode(token=token, key=pub_key, algorithms=[config('ALGORITHM')])

    except JWTError as e:

        logger.error(f"JWT error during decoding: {e}")

        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Error while token verification')

    except InvalidSignature as e:

        logger.error(f"Invalid signature while signing token: {e}")

        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='Signature Verification Failed')

    except ValueError as e:

        logger.error(f"Value error during token validation: {e}")

        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Detail mismatched')

    except HTTPException as he:

        raise he

    except Exception as e:

        logger.error(f"Unexpected error in decode_access_token: {e}")

        raise HTTPException(status_code=500, detail='Internal Server Error')

async def generate_temp_access_token(data: dict):

    try:

        to_encode = data.copy()

        expire = datetime.now(UTC) + timedelta(minutes=30)

        issued_at = datetime.now(UTC)

        to_encode.update({'exp': expire, 'iat': issued_at})

        return jwt.encode(to_encode, key=config('TEMP_TOKEN_SECRET'), algorithm=config('TEMP_TOKEN_ALGORITHM'))

    except JWTError as e:

        logger.error(f"JWT error during temp token encoding: {e}")

        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Error while temp token creation')

    except InvalidSignature as e:

        logger.error(f"Invalid signature while signing temp token: {e}")

        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='Signature Verification Failed in temp token')

    except ValueError as e:

        logger.error(f"Value error during temp token generation: {e}")

        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Detail mismatched in temp token')

    except HTTPException as he:

        raise he

    except Exception as e:

        logger.error(f"Unexpected error in generate_temp_access_token: {e}")

        raise HTTPException(status_code=500, detail='Internal Server Error')


async def decode_temp_access_token(token: str):

    try:

        return jwt.decode(token=token, key=config('TEMP_TOKEN_SECRET'), algorithms=[config('TEMP_TOKEN_ALGORITHM')])

    except JWTError as e:

        logger.error(f"JWT error during temp token decoding: {e}")

        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Error while temp token verification')

    except InvalidSignature as e:

        logger.error(f"Invalid signature while signing temp token: {e}")

        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='Signature Verification Failed in temp token')

    except ValueError as e:

        logger.error(f"Value error during temp token validation: {e}")

        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Detail mismatched in temp token')

    except HTTPException as he:

        raise he

    except Exception as e:

        logger.error(f"Unexpected error in decode_temp_access_token: {e}")

        raise HTTPException(status_code=500, detail='Internal Server Error')