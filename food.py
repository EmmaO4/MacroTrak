class Food:
    def __init__(self, calories, fat, sat_fat, poly_fat, mono_fat, carbs, fiber, insol_fiber, sol_fiber, sugar, protein):
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

    # getters
    def get_calories(self):
        return self._calories
    def get_fat(self):
        return self._fat
    def get_sat_fat(self):
        return self._sat_fat
    def get_poly_fat(self):
        return self._poly_fat
    def get_mono_fat(self):
        return self._mono_fat
    def get_carbs(self):
        return self._carbs
    def get_fiber(self):
        return self._fiber
    def get_insol_fiber(self):
        return self._insol_fiber
    def get_sol_fiber(self):
        return self._sol_fiber
    def get_sugar(self):
        return self._sugar
    def get_protein(self):
        return self._protein

    # setters
    def set_calories(self, value):
        self._calories = value
    def set_fat(self, value):
        self._fat = value
    def set_sat_fat(self, value):
        self._sat_fat = value
    def set_poly_fat(self, value):
        self._poly_fat = value
    def set_mono_fat(self, value):
        self._mono_fat = value
    def set_carbs(self, value):
        self._carbs = value
    def set_fiber(self, value):
        self._fiber = value
    def set_insol_fiber(self, value):
        self._insol_fiber = value
    def set_sol_fiber(self, value):
        self._sol_fiber = value
    def set_sugar(self, value):
        self._sugar = value
    def set_protein(self, value):
        self._protein = value

    def to_dict(self):
        return {
            "calories": self.get_calories(),
            "fat": self.get_fat(),
            "sat_fat": self.get_sat_fat(),
            "poly_fat": self.get_poly_fat(),
            "mono_fat": self.get_mono_fat(),
            "carbs": self.get_carbs(),
            "fiber": self.get_fiber(),
            "insol_fiber": self.get_insol_fiber(),
            "sol_fiber": self.get_sol_fiber(),
            "sugar": self.get_sugar(),
            "protein": self.get_protein(),
        }
    
    @staticmethod
    def from_dict(data):
        return Food(
            data.get("calories"),
            data.get("fat"),
            data.get("sat_fat"),
            data.get("poly_fat"),
            data.get("mono_fat"),
            data.get("carbs"),
            data.get("fiber"),
            data.get("insol_fiber"),
            data.get("sol_fiber"),
            data.get("sugar"),
            data.get("protein"),
        )