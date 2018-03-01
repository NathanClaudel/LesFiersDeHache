from Ride import Ride


class Vehicule():
    pos = 0, 0
    time_counter = 0
    is_used = False
    waiting_time = 0
    
    rides_done = []
    
    #constructeur
    def __init__(self):
        pass
    
    #set a ride
    def set_ride(self, ride):
        self.time_counter = ride.time + dist(ride.posStart, self.pos)
        self.pos = ride.posEnd
        self.is_used = True
        self.rides_done.append(ride.id_number)
    
    def update(self):
        if(self.time_counter > 0):
            self.time_counter -= 1
            if(self.time_counter == 0):
                self.is_used = False
                waiting_time = 0
        else:
            waiting_time += 1

    
    def get_pos(self):
        return self.pos

def dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)