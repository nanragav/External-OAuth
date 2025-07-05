from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from models import User, Drive
from uuid import uuid4


async def adduserinfo(user: dict, db: AsyncSession):

    if not user['phone_number']:

        return JSONResponse(status_code=303, content={'error_type': 'Detail Missing', 'error_detail': 'Phone Number is Missing'})

    if not user['email_verified']:
        return JSONResponse(status_code=303, content={'error_type': 'Not Verified', 'error_detail': 'Email is not verified'})

    # user = User(id=uuid4(), user_name=user['name'], email=user['email'])