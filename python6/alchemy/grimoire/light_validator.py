
def validate_ingredients(ingredients: str):
    from .light_spellbook import light_spell_allowed_ingredients

    valids = light_spell_allowed_ingredients()
    ingredients_list = ingredients.lower().split()

    for ingredient in ingredients_list:
        if ingredient in valids:
            return f"{ingredients} VALID"
    return f"{ingredients} INVALID"
