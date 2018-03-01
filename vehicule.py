
class Vehicule():
    pos = 0, 0
    time_counter = 0
    is_used = False
    
    #constructeur
    def __init__(self):
        pass
    
    #set a ride
    def set_ride(self, time, pos_departure, pos_arrival):
        self.time_counter = time + abs(self.pos[0] - pos_departure[0]) + abs(self.pos[1] - pos_departure[1])
        self.pos = pos_arrival
        self.is_used = True
    
    def update(self):
        if(self.time_counter > 0):
            self.time_counter -= 1
            if(self.time_counter == 0):
                self.is_used = False
    
    def get_pos(self):
        return self.pos