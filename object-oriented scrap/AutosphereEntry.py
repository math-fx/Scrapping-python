class AutosphereEntry:
    def __init__(self, model, price, fuel, counter, release, type):
        
        self.model = model
        self.price = price
        self.fuel = fuel
        self.counter = counter
        self.release = release
        self.type = type

    def getDictEntry(self):
        return {
            "model":self.model,
            "price":self.price,
            "fuel":self.fuel,
            "counter":self.counter,
            "release":self.release,
            "type":self.type
        }