from math import sin, cos, sqrt, atan2, radians

def lonlatCalculator(lat1, lon1, lat2, lon2):
    
    R = 6373.0 
    lat1 = radians(lat1) 
    lon1 = radians(lon1) 
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2 
    c = 2 * atan2(sqrt(a), sqrt(1 - a)) 
    distance = R * c #거리, KM단위로 0.1=100M
    print("Result:", distance)
    
    return distance