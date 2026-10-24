from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Temperature Converter API")


# --- Pydantic Models ---
class CelsiusInput(BaseModel):
    celsius: float = Field(..., description="Temperature in Celsius", example=25.0)


class FahrenheitInput(BaseModel):
    fahrenheit: float = Field(..., description="Temperature in Fahrenheit", example=77.0)


class TemperatureResponse(BaseModel):
    celsius: float
    fahrenheit: float
    converted_from: str


# --- Endpoints ---
@app.post("/convert/celsius-to-fahrenheit", response_model=TemperatureResponse)
async def convert_celsius_to_fahrenheit(data: CelsiusInput):
    f_val = round((data.celsius * 9 / 5) + 32, 2)
    return TemperatureResponse(
        celsius=data.celsius,
        fahrenheit=f_val,
        converted_from="celsius",
    )


@app.post("/convert/fahrenheit-to-celsius", response_model=TemperatureResponse)
async def convert_fahrenheit_to_celsius(data: FahrenheitInput):
    c_val = round((data.fahrenheit - 32) * 5 / 9, 2)
    return TemperatureResponse(
        celsius=c_val,
        fahrenheit=data.fahrenheit,
        converted_from="fahrenheit",
    )