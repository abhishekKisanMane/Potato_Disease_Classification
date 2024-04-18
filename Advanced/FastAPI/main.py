from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class AvailableCuisines(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"
    japanese = "japanese"


food_item = {
    'indian' : ["Samasa", "Vadapaw", "Dosa", "Uttapm", "Puran Poli"],
    'amerian' : ["Burger", "Hot Dog"],
    'italian' : ["Ravioli", "Pizza"],
    'japanese' : ["Sakana", "Sushi"]
}

valid_cuisines = food_item.keys()

@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisines):
    return food_item.get(cuisine)

coupon_code = {
    1 : '10%',
    2 : '20%',
    3 : '30%'
}

@app.get("/get_coupon/{code}")
async def get_items(code: int):
    return {'discount_amount' : coupon_code.get(code)}
