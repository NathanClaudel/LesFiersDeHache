from vehicule import *

def algo(rides, vehicles, T):
    '''rides are sorted by (first start date, last possible start date) '''
    
    waiting_vehicles = vehicles
    
    for t in range(T):
        
        rides_to_check = rides_to_check(rides, t) #rides with start_date <= t <= latest_start
        
        for ride in rides_to_check:
            
            try:
                (vehicle, time_waited) = choose_vehicle(t, ride, waiting_vehicles)
                vehicle.set_ride(ride, t)
                waiting_vehicles.remove((vehicle, time_waited))
                
            except Exception:
                pass
        
        waiting_vehicles = []
        
        for vehicle in vehicles:
            vehicle.update()
            if not vehicle.isUsed:
                waiting_vehicles.append(vehicle)
            
        
            
def choose_vehicle(t, ride, waiting_vehicles):
    
    for (vehicle, time_waited) in waiting_vehicles:
        d = dist(vehicle.pos, ride.posStart)
        
        if(d <= time_waited):
            return (vehicle, time_waited)
    
    raise Exception("No vehicle can do this ride")

