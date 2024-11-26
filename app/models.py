from typing import Optional
from pydantic import BaseModel


class Weather(BaseModel):
    country_id: int
    weather_type: str
    temp: float
    pressure: int
    humidity: int
    temp_min: float
    temp_max: float
    country: str
    name: str
