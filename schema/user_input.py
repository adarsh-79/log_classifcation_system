from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Literal
from fastapi import HTTPException
import re

class UserInput(BaseModel):
    timestamp: Annotated[str, Field(description="timestamp of the log when generated") ]
    source: Annotated[Literal['ModernCRM', 'AnalyticsEngine', 'ModernHR', 'BillingSystem',
       'ThirdPartyAPI', 'LegacyCRM'], Field(..., description= "source from where the log got generated")]
    log_message: Annotated[str, Field(..., description="the actual log message")]

    @field_validator("timestamp")
    @classmethod
    def timestamp_validator(cls, value):
        pattern = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"   
        if re.match(pattern, value):
            return value
        raise HTTPException(status_code=400, detail="not a valid time stamp")