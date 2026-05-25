from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from enum import Enum
from typing import Optional

class Types (str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"

class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: Types
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("ID must start with'AC'")
        
        if self.contact_type == Types.physical:
            self.is_verified = True
        else:
            self.is_verified = False
        
        if self.contact_type == Types.telepathic and self.witness_count < 3:
            raise ValueError()

        

