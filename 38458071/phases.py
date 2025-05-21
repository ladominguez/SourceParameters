import pandas as pd
import numpy as np

def read_phases(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        earthquake = {}
        for k, line in enumerate(lines):
            if k == 0:
                line_split = line.strip().split()
                earthquake['earthquake_id'] = line_split[0]
                earthquake['datetime'] = line_split[3]
                earthquake['latitude'] = float(line_split[4])
                earthquake['longitude'] = float(line_split[5])
                earthquake['depth'] = float(line_split[6])
                earthquake['magnitude'] = float(line_split[7])
            elif k == 1:
                line_split = line.strip().split()
                phase = {}
                phase['network'] = line_split[0]
                phase['station'] = line_split[1]
                phase['component'] = line_split[2]
                phase['latitude'] = float(line_split[5])
                phase['longitude'] = float(line_split[6])
                phase['phase'] = line_split[8]
                phase['distance'] = float(line_split[9])
                phase['phase_time'] = line_split[10]
                print(phase)
                
    
    return earthquake, phases
            
if __name__ == "__main__":
    eq = read_phases('38458071.phase')
    pass
            

