

class Bottle:
    def _init_(self, volume, type_):
        self.volume = volume
        self.type_ = type_

    def pour(self):
        print("Pouring...")

    def fill(self):
        print("Filling...")

    def recycle(self):
        print("Recycling")

botella=Bottle()
botella.volume=25
botella.type_="plastic"
botella.pour()
botella.fill()
botella.recycle()
print(botella.volume)
print(botella.type_)






