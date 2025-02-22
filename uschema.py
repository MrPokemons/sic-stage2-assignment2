from datetime import datetime
from pydantic import BaseModel

class SensorData(BaseModel):
    timestamp: datetime
    humidity: float
    ldr: float
    temperature: float
