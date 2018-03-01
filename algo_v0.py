def algo(rides, vehicles, T):
    '''rides are sorted by (first start date, last possible start date) '''
    
    waiting_vehicles = [(vehicle, 0) for vehicle in vehicles]
    
    for t in range(T):
        
        rides_to_check = rides_to_check(rides, t) #rides with start_date <= t <= latest_start
        
        for ride in rides_to_check:
            
            try:
                choose_vehicle(t, ride, waiting_vehicles).set_ride(t, ride)
            
                    

                 
            
def choose_vehicle(t, ride, waiting_vehicles):
    
    for (vehicle, time_waited) in waiting_vehicles:
        d = dist(vehicle.pos, ride.posStart)
        
        if(d <= time_waited):
            return vehicle
    
    raise Exception("No vehicle can do this ride")
    