from oops2 import Car

car1=Car(brand="Ford",name="Mustang",door_count=4,capacity=4,engine_power=400)
car2=Car(brand="Porsche",name="Carrera 911",door_count=2,capacity=2,engine_power=800)

car1.drive(5)
car2.drive(3)

car1.park()
car2.park()

car1.get_details()
car2.get_details()

car1.car_service()