import numpy as np

"""
based on: 
https://github.com/afar/robinson_projection/blob/master/robinson.js
"""

class Robinson:
    """
    valid for maps which width to height ratio is around 1.9716551906973
    """
    def __init__(self):
        self.orig_map_shape = 2754, 1398 
        self.map_shape = self._rescale() 
        self.R = (self.map_shape[1]/2.666269758)
        self.AA = [0.8487,0.84751182,0.84479598,0.840213,0.83359314,0.8257851,0.814752,0.80006949,0.78216192,0.76060494,0.73658673,0.7086645,0.67777182,0.64475739,0.60987582,0.57134484,0.52729731,0.48562614,0.45167814]
        self.BB = [0,0.0838426,0.1676852,0.2515278,0.3353704,0.419213,0.5030556,0.5868982,0.67182264,0.75336633,0.83518048,0.91537187,0.99339958,1.06872269,1.14066505,1.20841528,1.27035062,1.31998003,1.3523]
    
    def _rescale(self):
        return self.orig_map_shape
        # width, height = self.orig_map_shape
        # return int(height*1.97165551906973), height
    
    def round_to_nearest(self, roundTo, value):
        return np.floor(value/roundTo)*roundTo

    def to_robinson(self, lng, lat):
        lng_s, lat_s = np.sign([lng, lat])
        lng, lat = abs(lng), abs(lat)
        
        low = self.round_to_nearest(5, lat-0.0000000001) if lat > 0 else 0
        high = low + 5
        
        low_idx = int(low/5)
        high_idx = int(high/5)
        ratio = (lat - low)/5
        
        adjAA = (self.AA[high_idx] - self.AA[low_idx])*ratio + self.AA[low_idx]
        adjBB = (self.BB[high_idx] - self.BB[low_idx])*ratio + self.BB[low_idx]

        Xr = adjAA * lng * np.pi/180 * lng_s * self.R + self.map_shape[0]//2
        Yr = adjBB * lat_s * self.R + self.map_shape[1]//2

        return int(Xr), int(Yr)


