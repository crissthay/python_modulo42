from ..elements import create_air
from elements import create_fire
import alchemy.potions


def lead_to_gold():
    return (f"Recipe transmuting Lead to Gold: brew "
            f"{create_air()} and {alchemy.potions.strength_potion()} "
            f"mixed with {create_fire()}")
