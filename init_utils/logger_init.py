import logging

try:

    logger = logging.getLogger(__name__)

except Exception as e:

    print('Error while creating the logger')
