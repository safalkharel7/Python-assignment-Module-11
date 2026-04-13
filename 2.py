class Car:
    def __init__(self,reg_num:str ,max_speed:float, cur_speed = 0, distance = 0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.distance = distance

    def accelerate(self, change):
        self.cur_speed += change
        if self.cur_speed<0:
            self.cur_speed = 0
        if self.cur_speed>self.max_speed:
            self.cur_speed = self.max_speed

    def drive(self, hours):
        self.distance += self.cur_speed * hours
        return self.distance

    def get_info(self):
        return {"reg_num":self.reg_num, "max_speed":self.max_speed,
                "cur_speed": self.cur_speed, "distance":self.distance}

class ElectricCar(Car):
    def __init__(self, reg_num, max_speed, battery):
        super().__init__(reg_num, max_speed)
        self.battery = battery

class GasolineCar(Car):
    def __init__(self, reg_num, max_speed, tank_vol):
        super().__init__(reg_num, max_speed)
        self.tank_vol = tank_vol

Car1 = ElectricCar("ABC-15", 180, 52.5)
Car2 = GasolineCar("ACD-123", 165, 32.3)
Car1.accelerate(10)
dist1 = Car1.drive(3)
Car2.accelerate(12)
dist2 = Car2.drive(3)
print(dist1)
print(dist2)