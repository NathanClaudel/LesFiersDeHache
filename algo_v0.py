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
            if not vehicle.isUsed:
                waiting_vehicles.append(vehicle)
            
        
            
def choose_vehicle(t, ride, waiting_vehicles):
    '''returns a vehicle able to make the ride'''
    for vehicle in waiting_vehicles:
        d = dist(vehicle.pos, ride.posStart)
        
        if(d <= vehicle.time_waited):
            return vehicle
    
    raise Exception("No vehicle can do this ride")
    
    

def rides_to_check_gen(rides, t):
    '''rides possible to start at time t'''
    r_list = []
    for ride in rides:
        if(t > ride.latestFinish):
            rides.remove(ride)
        if(t >= ride.earlyStart):
            r_list.append(ride)

