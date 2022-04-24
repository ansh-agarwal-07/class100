class Car(object):

    def __init__(self,model,colour,company,speed_limit,acceleration):
        self.colour = colour
        self.company = company
        self.speed_limit = speed_limit
        self.model = model
        self.acceleration = acceleration
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
    def accelerate(self): 
        print("accelerating")   

audi = Car("grandsphere","rosegold","Audi",260,3)
print(audi.model)
    