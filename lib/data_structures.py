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
    list_food = [dict.get("name") for dict in spicy_foods]
    return list_food


def get_spiciest_foods(spicy_foods):
    hot_list = [dict for dict in spicy_foods if dict.get("heat_level") > 5]
    return hot_list

def print_spicy_foods(spicy_foods):
    spicy_list = [f"{dict.get('name')} ({dict.get('cuisine')}) | Heat Level: {'🌶' * dict.get('heat_level')}" for dict in spicy_foods]
    for food in spicy_list:
        print(food)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for dict in spicy_foods:
        if (dict.get('cuisine') == cuisine):
            return dict
    
def print_spiciest_foods(spicy_foods):
    spicy_list = [f"{dict.get('name')} ({dict.get('cuisine')}) | Heat Level: {'🌶' * dict.get('heat_level')}" 
                  for dict in spicy_foods if dict.get('heat_level') > 5]
    for food in spicy_list:
        print(food)

def get_average_heat_level(spicy_foods):
    heat_levels = [dict.get('heat_level') for dict in spicy_foods]
    return sum(heat_levels) / len(heat_levels)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
