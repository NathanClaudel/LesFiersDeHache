from Ride.py import Ride

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
        self.time_counter = ride.time + abs(self.pos[0] - ride.posStart[0]) + abs(self.pos[1] - ride.posStart[1])
        self.pos = ride.posEnd
        self.is_used = True
        self.rides_done.append(ride.id_number)
    
    def update(self):
        if(self.time_counter > 0):
            self.time_counter -= 1
            if(self.time_counter == 0):
                self.is_used = False
            
    def update_time(self, current_time):
        if(current_time >= time_counter):
            is_used = False

    
    def get_pos(self):
        return self.pos