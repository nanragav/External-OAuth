from fastapi import HTTPException
from starlette.config import Config
import os
from dotenv import load_dotenv
from init_utils.logger_init import logger

load_dotenv()

try:

    config = Config(environ=os.environ)

except Exception as e:

    logger.error(f'Error while initialing the config')

    raise HTTPException(status_code=500, detail='Environmental file is missing')