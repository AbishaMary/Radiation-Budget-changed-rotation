# %%
import netCDF4 as nc
import numpy as np
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
from numpy import unravel_index
import matplotlib.animation as ani
from matplotlib import rc
from IPython.display import HTML, Image
from matplotlib.ticker import EngFormatter


def consecutive(data, stepsize=1):
    return np.split(data, np.where(np.diff(data) != stepsize)[0]+1)

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def find_nearest_idx(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

def get_area():
    import xarray as xr
    area = xr.open_dataset('/work/mh0066/m300909/mpiesm-landveg/mpiesm-landveg/experiments/aquaplanet_sponge_layer_rotation_1x/outdata/grid_area.nc',decode_times=True)
    grid_area = area.cell_area[:]
    return grid_area

def get_crh(q,qs):
    int_q = q[:,:13,:,:].integrate(coord='plev')
    int_qs = qs[:,:13,:,:].integrate(coord='plev')
    crh = int_q/int_qs
    return crh

def area_weighted_mean(cc, lat1, lat2):
    grid_area = get_area()
    cc = cc[:,:,lat1:lat2,:] * grid_area[lat1:lat2,:]/grid_area[lat1:lat2,:].sum(dim = ['lat','lon'])
    cc_area = cc.sum(dim=['lat','lon'])
    return cc_area.mean(dim='time')


def zonal_time_avg(s5,s4,s3,s2,s1,ctl,f1,f2,f3,time=True,lon=True):
    import pandas as pd
    
    data_concat = xr.concat([s5,s4,s3,s2,s1,ctl,f1,f2,f3], pd.Index(np.arange(0,9), name='length'))
    if time == True and lon == True:
        data_avg = data_concat.mean(dim = ['time','lon'])
    
    elif time == True and lon == False:
        data_avg = data_concat.mean(dim = ['time'])
        
    elif time == False and lon == True:
        data_avg = data_concat.mean(dim = ['lon'])    
    return data_avg 


def global_mean_weighted(s5,s4,s3,s2,s1,ctl,f1,f2,f3):
    
    import pandas as pd

    grid_area = get_area()
    total_area = grid_area.sum(dim = ['lat','lon'])
    
    data_concat = xr.concat([s5,s4,s3,s2,s1,ctl,f1,f2,f3], pd.Index(np.arange(0,9), name='length'))
    
    global_mean = xr. DataArray(None, coords=[range(len(data_concat))],dims=("length"))
    for i in range(len(data_concat)):
        data_concat[i] = (data_concat[i] * grid_area)/total_area
        data_i_wighted_avg = data_concat[i].sum(dim=['lat','lon'])
        global_mean[i] = data_i_wighted_avg.mean(dim=['time'])
        
    return global_mean 


def global_std_weighted(s5,s4,s3,s2,s1,ctl,f1,f2,f3):
    
    import pandas as pd
    
    grid_area = get_area()
    total_area = grid_area.sum(dim = ['lat','lon'])
    data_concat = xr.concat([s5,s4,s3,s2,s1,ctl,f1,f2,f3], pd.Index(np.arange(0,9), name='length'))
    
    global_std = xr. DataArray(None, coords=[range(len(data_concat))],dims=("length"))
    for i in range(len(data_concat)):
        data_concat[i] = (data_concat[i] * grid_area)/total_area
        data_i_wighted_std = data_concat[i].sum(dim=['lat','lon'])
        global_std[i] = data_i_wighted_std.std(dim=['time'])
        
    return global_std
        
        
# %%
def global_sum(s5,s4,s3,s2,s1,ctl,f1,f2,f3):
    
    import pandas as pd
    
    data_concat = xr.concat([s5,s4,s3,s2,s1,ctl,f1,f2,f3], pd.Index(np.arange(0,9), name='length'))
    
    global_mean = xr. DataArray(None, coords=[range(len(data_concat))],dims=("length"))
    for i in range(len(data_concat)):
        data_i_wighted_avg = data_concat[i].sum(dim=['lat','lon'])
        global_mean[i] = data_i_wighted_avg.mean(dim=['time'])
        
    return global_mean