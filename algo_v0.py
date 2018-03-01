def algo(rides, vehicles, T):
    '''rides are sorted by (first start date, last possible start date) '''
    
    waiting_vehicles = [(vehicle, 0) for vehicle in vehicles]
    
    for t in range(T):
        
        rides_to_check = rides_to_check(rides, t) #rides with start_date <= t <= latest_start
        
        for r in rides_to_check:
            
            for (vehicle, time_waited) in waiting_vehicles:
                
                if(dist(vehicle.pos)