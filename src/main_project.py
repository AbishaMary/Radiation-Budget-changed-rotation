# %%
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

# %%
control_run = xr.open_dataset('/work/mh0066/m300909/mpiesm-landveg/mpiesm-landveg/experiments/aquaplanet_sponge_layer_rotation_1x/outdata/aquaplanet_sponge_layer_rotation_1x_echam6_ATM_1976_2015.nc',decode_times=True)
# %%
