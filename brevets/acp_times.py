"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math

#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    #figure out how to use control_dist
    #we're finding start and end time for a given control???
    #brevet dist is for finding if it's start or end
    #just figure out control_dist

    brevet20 = 1.2 * brevet_dist_km
    
    if control_dist_km > brevet20:
        return flask.render_template('500.html'), 500
    if brevet_dist_km not in {200, 300, 400, 600, 1000}:
        raise ValueError;

    opening_time = 0
    if control_dist_km <= 200: 
        opening_time = control_dist_km/34
    elif control_dist_km >= 200 or brevet_dist_km == 200:
        opening_time = 200/34 #good
        if brevet_dist_km > 200 and control_dist_km < 400:
            if brevet_dist_km == 300 and control_dist_km >=300:
                opening_time = opening_time + 100/32
            else:
                opening_time = opening_time + (control_dist_km - 200)/32
        elif control_dist_km >= 400 or brevet_dist_km == 400:
            opening_time = opening_time + 200/32
            if brevet_dist_km > 400 and control_dist_km >= 400 and control_dist_km < 600:
                opening_time = opening_time + (control_dist_km-400)/30
            elif control_dist_km >= 600 or brevet_dist_km == 600:
                opening_time = opening_time + 200/30
            
                if brevet_dist_km > 600 and control_dist_km > 600 and control_dist_km < 1000:
                    opening_time = opening_time + (control_dist_km - 600)/28
                elif control_dist_km >= 1000 or brevet_dist_km == 1000:
                    opening_time = opening_time + 400/28 

    hours = math.floor(opening_time)
    minutes = (opening_time - hours) * 60
    minutes = round(minutes)
    return brevet_start_time.shift(hours=hours, minutes= minutes)

def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    brevet20 = 1.2 * brevet_dist_km
    
    if control_dist_km > brevet20:
        return flask.render_template('500.html'), 500
    if brevet_dist_km not in {200, 300, 400, 600, 1000}:
        raise ValueError;
    if control_dist_km == 0:
        closing_time = 1
    elif control_dist_km <=60:
        closing_time = control_dist_km/20 +1
    elif control_dist_km < 200: 
        closing_time = control_dist_km/15
    elif control_dist_km >= 200:
        closing_time = 200/15
        if brevet_dist_km == 200:
            closing_time = 13.5
        if brevet_dist_km > 200 and control_dist_km < 400:
            if control_dist_km >=300 and brevet_dist_km == 300:
                closing_time = closing_time + 100/15
            else:
                closing_time = closing_time + (control_dist_km - 200)/15
        elif control_dist_km >= 400 or brevet_dist_km == 400:
            closing_time = closing_time + 200/15
            
            if brevet_dist_km > 400 and control_dist_km < 600:
                closing_time = closing_time + (control_dist_km-400)/15
            elif control_dist_km >= 600 or brevet_dist_km == 600:
                closing_time = closing_time + 200/15
                if brevet_dist_km > 600 and control_dist_km < 1000:
                    closing_time = closing_time + (control_dist_km - 600)/11.428
                elif control_dist_km > 1000 or brevet_dist_km == 1000:
                    closing_time = closing_time + 400/11.428
    
   
    hours = math.floor(closing_time)
    minutes = (closing_time - hours) * 60
    minutes = round(minutes)
    
    return brevet_start_time.shift(hours = hours, minutes = minutes)
