class Allergies:

    ALLERGENS = {
        1: 'eggs',
        2: 'peanuts',
        4: 'shellfish',
        8: 'strawberries',
        16: 'tomatoes',
        32: 'chocolate',
        64: 'pollen',
        128: 'cats'
    }

    def __init__(self, score: int):
        self.score = score

    def allergic_to(self, item: str) -> bool:
        return item in self.lst

    @property
    def lst(self):
        return [allergen for value, allergen in self.ALLERGENS.items() if self.score & value]