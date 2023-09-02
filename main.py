class Car:
    color = "white"

    def __init__(self,model,color,year):
        self.model = model
        self.color = color
        self.year = year


    def show_info(self):
        print("color:", self.color)
        print("model", self.model)
        print("year", self.year)

    def set_color(self, newColor):
        self.color = newColor

    def set_model(self, newModel):
        self.model = newModel

    def set_year(self, newYear):
        self.year = newYear

myCar = Car("audi", "red", 2020)
myCar.color = "red"
myCar.show_info()

myCar2 = Car("lambo", "yellow", 2021)
myCar2.color = "black"

myCar2.show_info()

