import requests

data = {
    "features": {
        "Rooms": 3,
        "Distance": 5.0,
        "Bathroom": 2,
        "Car": 1,
        "Landsize": 400,
        "Bedroom2": 2,
        "Type": "h",
        "Method": "S",
        "Postcode": 3000,
        "Propertycount": 5000,
        "Lattitude": -37.8136,
        "Longtitude": 144.9631
    }
}


res = requests.post("http://127.0.0.1:5000/predict", json=data)
print(res.json())