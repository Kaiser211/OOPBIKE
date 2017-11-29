class Bike(object):
    def __init__(self, price, max_speed):
        print "creating Bike"
        self.price=price
        self.max_speed=max_speed
        self.miles=0

    def displayInfo(self):
        print "Bike's price $", self.price
        print  "The max speed is",  self.max_speed ,"mph"
        print "The total miles are", self.miles, "miles"
       
    def ride(self):
        print "Riding"
        self.miles+=10
        
    def reverse(self):
        print "Reversing"
        if self.miles>5:
           self.miles-=5
       

bike1 = Bike(200,25)
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(150, 20)
bike2.ride()
bike2.reverse()
bike2.displayInfo()