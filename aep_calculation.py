from Farm_Evaluator_Vec import *
import numpy as np

def aep_calculation(locs):
    turb_specs    =  {   
                         'Name': 'Anon Name',
                         'Vendor': 'Anon Vendor',
                         'Type': 'Anon Type',
                         'Dia (m)': 100,
                         'Rotor Area (m2)': 7853,
                         'Hub Height (m)': 100,
                         'Cut-in Wind Speed (m/s)': 3.5,
                         'Cut-out Wind Speed (m/s)': 25,
                         'Rated Wind Speed (m/s)': 15,
                         'Rated Power (MW)': 3
                     }
    turb_diam      =  turb_specs['Dia (m)']
    turb_rad       =  turb_diam/2 
    loc = []
    for i in locs:
        loc.append((i.x,i.y))

    df = pd.DataFrame(loc, columns =['x','y'])
    turb_coords = df.to_numpy(dtype = np.float32)
    power_curve   =  loadPowerCurve('../../Shell_Hackathon Dataset/power_curve.csv')
    wind_inst_freq =  binWindResourceData(r'../../Shell_Hackathon Dataset/Wind Data/wind_data_2007.csv')   
    n_wind_instances, cos_dir, sin_dir, wind_sped_stacked, C_t = preProcessing(power_curve)
    checkConstraints(turb_coords, turb_diam)
    AEP = getAEP(turb_rad, turb_coords, power_curve, wind_inst_freq, 
                  n_wind_instances, cos_dir, sin_dir, wind_sped_stacked, C_t) 

    return AEP 
