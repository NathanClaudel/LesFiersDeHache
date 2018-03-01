from vehicule import *
from Ride import *

def algo(rides, vehicles, T):
    '''rides are sorted by (first start date, last possible start date) '''
    
    waiting_vehicles = vehicles
    
    for t in T:
        
        rides_to_check = rides_to_check_gen(rides, t) #rides with start_date <= t <= latest_start
        
        for ride in rides_to_check:
            
            try:
                vehicle = choose_vehicle(t, ride, waiting_vehicles)
                vehicle.set_ride(ride, t)
                
            except Exception:
                pass
        
        waiting_vehicles = []
        
        for vehicle in vehicles:
            vehicle.update()
            if not vehicle.is_used:
                waiting_vehicles.append(vehicle)
    
    return vehicles
        
            
def choose_vehicle(t, ride, waiting_vehicles):
    '''returns a vehicle able to make the ride'''
    for vehicle in waiting_vehicles:
        d = dist(vehicle.pos, ride.posStart)
        if(d <= vehicle.waiting_time):
            return vehicle
    
    raise Exception("No vehicle can do this ride")
    
    

def rides_to_check_gen(rides, t):
    '''rides possible to start at time t'''
    r_list = []
    for ride in rides:
        if(t > ride.latestStart):
            rides.remove(ride)
        if(t >= ride.earlyStart):
            r_list.append(ride)
    return r_list


def dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)