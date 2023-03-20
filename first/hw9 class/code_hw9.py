# Придумать класс и методы к нему, использовать инкапсуляцию, полиморфизм и наследование

class Cars:
    def __init__(self, model, engine, speed):
        self.model = model
        self.engine = engine
        self.speed = speed

    def car_model(self):
        return self.car_model() + ' ' + 'car_model'

    def res(self):
        return 'res'


class Bmw(Cars):
    def which(self):
        return self.model + ' ' + 'company'

    def biggest(self):
        return self.speed + ' ' + 'biggest'

    def res(self):
        return self.model + ',  ' + self.engine + ' ' + 'res'


class Ford(Cars):
    def country(self):
        return self.model + ' ' + 'America'