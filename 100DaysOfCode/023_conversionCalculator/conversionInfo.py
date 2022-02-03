def distance_im(miles):
    return miles * 1.60934


def distance_mi(km):
    return km / 1.60934


def temp_im(f):
    return (f - 32) * 5 / 9


def temp_mi(c):
    return c * 9 / 5 + 32


def weight_im(lbs):
    return lbs / 2.205


def weight_mi(kg):
    return kg * 2.205


data = {
    "distance": {
        "imperial": "miles",
        "metric": "km",
        "i2m": distance_im,
        "m2i": distance_mi
    },
    "temperature": {
        "imperial": "°F",
        "metric": "°C",
        "i2m": temp_im,
        "m2i": temp_mi
    },
    "weight": {
        "imperial": "lbs",
        "metric": "kgs",
        "i2m": weight_im,
        "m2i": weight_mi
    },
}
