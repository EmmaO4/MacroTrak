# food.py
class Food:
    def __init__(self, item_name, calories, fat, sat_fat, poly_fat, mono_fat, carbs, fiber, insol_fiber, sol_fiber, sugar, protein):
        self._item_name = item_name
        self._calories = calories
        self._fat = fat
        self._sat_fat = sat_fat
        self._poly_fat = poly_fat
        self._mono_fat = mono_fat
        self._carbs = carbs
        self._fiber = fiber
        self._insol_fiber = insol_fiber
        self._sol_fiber = sol_fiber
        self._sugar = sugar
        self._protein = protein

    # Getters
    def get_item_name(self):
        return self._item_name
    def get_calories(self):
        return self._calories
    def get_fat(self):
        return self._fat
    def get_saturated_fat(self):
        return self._sat_fat
    def get_polyunsaturated_fat(self):
        return self._poly_fat
    def get_monounsaturated_fat(self):
        return self._mono_fat
    def get_carbs(self):
        return self._carbs
    def get_fiber(self):
        return self._fiber
    def get_insoluble_fiber(self):
        return self._insol_fiber
    def get_soluble_fiber(self):
        return self._sol_fiber
    def get_sugar(self):
        return self._sugar
    def get_protein(self):
        return self._protein