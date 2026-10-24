class Car:
    def __init__(self,name,door_count,capacity,brand,engine_power):
        self.name=name
        self.door_count=door_count
        self.capacity=capacity
        self.brand=brand
        self.engine_power=engine_power

    def drive(self,d):
        print(self.name,"has been driven for",d,"miles.")

    def park(self):
        print(self.name,"is now parked.")

    def get_details(self):
        print("Brand Name:",self.brand)
        print("Car Name:",self.name)
        print("Door Count:",self.door_count)
        print("Capacity:",self.capacity)
        print("Engine Power:",self.engine_power)

    def __carburetor(self):
        print("Carburetor has been changed")

    def car_service(self):
        self.__carburetor()