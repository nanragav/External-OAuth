from pydantic import BaseModel

class GetPhoneNumber(BaseModel):

    phone_number: str