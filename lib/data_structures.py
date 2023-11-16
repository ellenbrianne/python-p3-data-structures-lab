spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [obj["name"] for obj in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [obj for obj in spicy_foods if obj["heat_level"] > 5]
    
def print_spicy_foods(spicy_foods):
    li = [f"{obj['name']} ({obj['cuisine']}) | Heat Level: {'🌶' * obj['heat_level']}" for obj in spicy_foods]
    for f in li: print(f)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return next(obj for obj in spicy_foods if obj["cuisine"] == cuisine)
    
def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    import statistics
    return statistics.mean([obj["heat_level"] for obj in spicy_foods])

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
