from Ride import Ride

class Vehicule():
    pos = 0, 0
    time_counter = 0
    is_used = False
    
    rides_done = []
    
    #constructeur
    def __init__(self):
        pass
    
    #set a ride
    def set_ride(self, ride, time_start):
        self.time_counter = ride.time + time_start
        self.pos = ride.posEnd
        self.is_used = True
        self.rides_done.append(ride.id_number)
    
    def update(self):
        if(self.time_counter > 0):
            self.time_counter -= 1
            if(self.time_counter == 0):
                self.is_used = False
            
    def update_time(self, current_time):
        if(current_time >= self.time_counter):
            self.is_used = False

    
    def get_pos(self):
        return self.pos
