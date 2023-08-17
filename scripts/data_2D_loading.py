# %%
import numpy as np
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
from make_plot import *
from functions import *


# %%
rotation_003125x = xr.open_dataset('/work/mh0066/m300909/mpiesm-landveg/mpiesm-landveg/experiments/aquaplanet_sponge_layer_rotation_003125x/outdata/aquaplanet_sponge_layer_rotation_003125x_echam6_BOT_1976_2015.nc',decode_times=True)
rotation_00625x = xr.open_dataset('/work/mh0066/m300909/mpiesm-landveg/mpiesm-landveg/experiments/aquaplanet_sponge_layer_rotation_00625x/outdata/aquaplanet_sponge_layer_rotation_00625x_echam6_BOT_1976_2015.nc',decode_times=True)
rotation_0125x = xr.open_dataset('/work/mh0066/m300909/mpiesm-landveg/mpiesm-landveg/experiments/aquaplanet_sponge_layer_rotation_0125x/outdata/aquaplanet_sponge_layer_rotation_0125x_echam6_BOT_1976_2015.nc',decode_times=True)
rotation_025x = xr.open_dataset('/work/mh0066/m300909/mpiesm-landveg/mpiesm-landveg/experiments/aquaplanet_sponge_layer_rotation_025x/outdata/aquaplanet_sponge_layer_rotation_025x_echam6_BOT_1976_2015.nc',decode_times=True)
rotation_05x = xr.open_dataset('/work/mh0066/m300909/mpiesm-landveg/mpiesm-landveg/experiments/aquaplanet_sponge_layer_rotation_05x_redo/outdata/aquaplanet_sponge_layer_rotation_05x_redo_echam6_BOT_1976_2015.nc',decode_times=True)
rotation_1x = xr.open_dataset('/work/mh0066/m300909/mpiesm-landveg/mpiesm-landveg/experiments/aquaplanet_sponge_layer_rotation_1x/outdata/aquaplanet_sponge_layer_rotation_1x_echam6_BOT_1976_2015.nc',decode_times=True)
rotation_2x = xr.open_dataset('/work/mh0066/m300909/mpiesm-landveg/mpiesm-landveg/experiments/aquaplanet_sponge_layer_rotation_2x/outdata/aquaplanet_sponge_layer_rotation_2x_echam6_BOT_1976_2015.nc',decode_times=True)
rotation_4x = xr.open_dataset('/work/mh0066/m300909/mpiesm-landveg/mpiesm-landveg/experiments/aquaplanet_sponge_layer_rotation_4x/outdata/aquaplanet_sponge_layer_rotation_4x_echam6_BOT_1976_2015.nc',decode_times=True)
rotation_8x = xr.open_dataset('/work/mh0066/m300909/mpiesm-landveg/mpiesm-landveg/experiments/aquaplanet_sponge_layer_rotation_8x/outdata/aquaplanet_sponge_layer_rotation_8x_echam6_BOT_1976_2015.nc',decode_times=True)

# %%
# CLEAR SKY LONGWAVE RADIATION
clrsky_003125x = rotation_003125x.var188[120:]
clrsky_00625x = rotation_00625x.var188[120:]
clrsky_0125x = rotation_0125x.var188[120:]
clrsky_025x = rotation_025x.var188[120:]
clrsky_05x = rotation_05x.var188[120:]
clrsky_1x = rotation_1x.var188[120:]
clrsky_2x = rotation_2x.var188[120:]
clrsky_4x = rotation_4x.var188[120:]
clrsky_8x = rotation_8x.var188[120:]

line_plot_2D(clrsky_003125x,clrsky_00625x,clrsky_0125x,clrsky_025x,
             clrsky_05x,clrsky_1x,clrsky_2x,clrsky_4x,clrsky_8x, 
             'Clear sky LW / '+ r'$W/m^2$', 'plots/clrolr.pdf', y_invert = True)



# %%
# ALL SKY LONGWAVE RADIATION
allsky_003125x = rotation_003125x.var179[120:]
allsky_00625x = rotation_00625x.var179[120:]
allsky_0125x = rotation_0125x.var179[120:]
allsky_025x = rotation_025x.var179[120:]
allsky_05x = rotation_05x.var179[120:]
allsky_1x = rotation_1x.var179[120:]
allsky_2x = rotation_2x.var179[120:]
allsky_4x = rotation_4x.var179[120:]
allsky_8x = rotation_8x.var179[120:]

line_plot_2D(allsky_003125x,allsky_00625x,allsky_0125x,allsky_025x,
             allsky_05x,allsky_1x,allsky_2x,allsky_4x,allsky_8x, 
             'Net OLR / '+ r'$W/m^2$', 'allolr.pdf', y_invert = True)



# %%
# LONGWAVE CLOUD RADIATIVE EFFECT
line_plot_2D(allsky_003125x - clrsky_003125x,allsky_00625x - clrsky_00625x, 
             allsky_0125x - clrsky_0125x, allsky_025x - clrsky_025x, 
             allsky_05x - clrsky_05x, allsky_1x - clrsky_1x, 
             allsky_2x - clrsky_2x, allsky_4x - clrsky_4x, 
             allsky_8x - clrsky_8x, 'LW cloud radiative effect / '+ r'$W/m^2$', 
             'cloud_LW.pdf', y_invert = False)


# %%
# ALL SKY SHORTWAVE RADIATION
rsw_003125x = rotation_003125x.var178[120:]
rsw_00625x = rotation_00625x.var178[120:]
rsw_0125x = rotation_0125x.var178[120:]
rsw_025x = rotation_025x.var178[120:]
rsw_05x = rotation_05x.var178[120:]
rsw_1x = rotation_1x.var178[120:]
rsw_2x = rotation_2x.var178[120:]
rsw_4x = rotation_4x.var178[120:]
rsw_8x = rotation_8x.var178[120:]

line_plot_2D(rsw_003125x,rsw_00625x,rsw_0125x,rsw_025x,rsw_05x,rsw_1x,
             rsw_2x,rsw_4x, rsw_8x, 'Net SW '+ r'($W/m^2$)', 
             'net_sw.pdf', y_invert = False)


# %%
# SHORTWAVE CLOUD RADIATIVE EFFECT
isw_003125x = rotation_003125x.var187[120:]
isw_00625x = rotation_00625x.var187[120:]
isw_0125x = rotation_0125x.var187[120:]
isw_025x = rotation_025x.var187[120:]
isw_05x = rotation_05x.var187[120:]
isw_1x = rotation_1x.var187[120:]
isw_2x = rotation_2x.var187[120:]
isw_4x = rotation_4x.var187[120:]
isw_8x = rotation_8x.var187[120:]

line_plot_2D(isw_003125x, isw_00625x,  isw_0125x, isw_025x,isw_05x, isw_1x, isw_2x, isw_4x, 
             isw_8x, 'Clear sky SW '+ r'($W/m^2$)', 'clrsky_sw.pdf', 
             y_invert = False)

line_plot_2D(rsw_003125x - isw_003125x,rsw_00625x - isw_00625x, 
             rsw_0125x - isw_0125x, rsw_025x - isw_025x, 
             rsw_05x - isw_05x, rsw_1x - isw_1x, rsw_2x - isw_2x, 
             rsw_4x - isw_4x, rsw_8x - isw_8x, 'Cloud SW radiative effect '+ r'($W/m^2$)', 
             'cloud_sw.pdf', y_invert = True)

line_plot_2D_slow(rsw_003125x - isw_003125x,rsw_00625x - isw_00625x, 
             rsw_0125x - isw_0125x, rsw_025x - isw_025x, 
             rsw_05x - isw_05x, rsw_1x - isw_1x, rsw_2x - isw_2x, 
             rsw_4x - isw_4x, rsw_8x - isw_8x, 'Cloud SW radiative effect '+ r'($W/m^2$)', 
             'cloud_sw_slow.pdf', y_invert = True)


# %%
# VERTICALLY INTEGRATED CLOUD WATER
xlvi_003125x = rotation_003125x.var231[120:]
xlvi_00625x = rotation_00625x.var231[120:]
xlvi_0125x = rotation_0125x.var231[120:]
xlvi_025x = rotation_025x.var231[120:]
xlvi_05x = rotation_05x.var231[120:]
xlvi_1x = rotation_1x.var231[120:]
xlvi_2x = rotation_2x.var231[120:]
xlvi_4x = rotation_4x.var231[120:]
xlvi_8x = rotation_8x.var231[120:]

line_plot_2D(xlvi_003125x,xlvi_00625x,xlvi_0125x,xlvi_025x,xlvi_05x,xlvi_1x,xlvi_2x,
             xlvi_4x, xlvi_8x, 'Cloud water '+ r'($kg/m^2$)', 
             'cloud_water.pdf', y_invert = False)

line_plot_2D_slow(xlvi_003125x,xlvi_00625x,xlvi_0125x,xlvi_025x,xlvi_05x,xlvi_1x,xlvi_2x,
             xlvi_4x, xlvi_8x, 'Cloud water '+ r'($kg/m^2$)', 
             'cloud_water_slow.pdf', y_invert = False)

vertical_integrated_cloud_water = global_mean_weighted(xlvi_003125x,xlvi_00625x,
                                                       xlvi_0125x,xlvi_025x,xlvi_05x,
                                                       xlvi_1x,xlvi_2x,xlvi_4x, xlvi_8x)

global_mean_plot(vertical_integrated_cloud_water,'Clouds' , 'blue', 
                 'Liquid water path/ '+r'$kg/m^2$', 'cloud_water_mean.pdf', 
                 legend = True, y_invert=False)
# %%
# VERTICALLY INTEGRATED CLOUD WATER
xivi_003125x = rotation_003125x.var150[120:]
xivi_00625x = rotation_00625x.var150[120:]
xivi_0125x = rotation_0125x.var150[120:]
xivi_025x = rotation_025x.var150[120:]
xivi_05x = rotation_05x.var150[120:]
xivi_1x = rotation_1x.var150[120:]
xivi_2x = rotation_2x.var150[120:]
xivi_4x = rotation_4x.var150[120:]
xivi_8x = rotation_8x.var150[120:]

line_plot_2D(xivi_003125x, xivi_00625x,xivi_0125x,xivi_025x,xivi_05x,xivi_1x,xivi_2x,
             xivi_4x, xivi_8x, 'Cloud ice '+ r'($kg/m^2$)', 
             'cloud_ice.pdf', y_invert = False)

line_plot_2D_slow(xivi_003125x, xivi_00625x,xivi_0125x,xivi_025x,xivi_05x,xivi_1x,xivi_2x,
             xivi_4x, xivi_8x, 'Cloud ice '+ r'($kg/m^2$)', 
             'cloud_ice_slow.pdf', y_invert = False)

vertical_integrated_cloud_ice = global_mean_weighted(xivi_003125x,xivi_00625x,
                                                       xivi_0125x,xivi_025x,xivi_05x,
                                                       xivi_1x,xivi_2x,xivi_4x, xivi_8x)
global_mean_plot(vertical_integrated_cloud_ice,'Clouds' , 'blue', 
                 'Ice water path / '+r'$kg/m^2$', 'cloud_ice_mean.pdf', 
                 legend = True, y_invert=False)



#%%
# VERTICALLY INTEGRATED CLOUD WATER + CLOUD ICE
xlxi_003125x = xlvi_003125x + xivi_003125x
xlxi_00625x = xlvi_00625x + xivi_00625x
xlxi_0125x = xlvi_0125x + xivi_0125x
xlxi_025x = xlvi_025x + xivi_025x
xlxi_05x = xlvi_05x + xivi_05x
xlxi_1x = xlvi_1x + xivi_1x
xlxi_2x = xlvi_2x + xivi_2x
xlxi_4x = xlvi_4x + xivi_4x
xlxi_8x = xlvi_8x + xivi_8x

line_plot_2D(xlxi_003125x, xlxi_00625x,xlxi_0125x,xlxi_025x,xlxi_05x,xlxi_1x,xlxi_2x,
             xlxi_4x, xlxi_8x, 'Cloud water + ice '+ r'($kg/m^2$)', 
             'cloud_water_ice.pdf', y_invert = False)

vertical_integrated_cloud_water_ice = global_mean_weighted(xlxi_003125x,xlxi_00625x,
                                                       xlxi_0125x,xlxi_025x,xlxi_05x,
                                                       xlxi_1x,xlxi_2x,xlxi_4x, xlxi_8x)

cloud_water_ice = xr.concat([vertical_integrated_cloud_water_ice,
                             vertical_integrated_cloud_water], pd.Index(np.arange(0,2), 
                                                                        name='parameter'))

global_mean_plot(cloud_water_ice, 
                 ['Cloud water + ice', 'Cloud water'] , 
                 ['blue','steelblue'], 'Cloud water + ice / '+r'$kg/m^2$',
                 'cloud_water_ice_mean.pdf', legend = True, y_invert=False)

#%%
# VERTICALLY INTEGRATED WATER VAPOUR
xiq_003125x = rotation_003125x.var230[120:]
xiq_00625x = rotation_00625x.var230[120:]
xiq_0125x = rotation_0125x.var230[120:]
xiq_025x = rotation_025x.var230[120:]
xiq_05x = rotation_05x.var230[120:]
xiq_1x = rotation_1x.var230[120:]
xiq_2x = rotation_2x.var230[120:]
xiq_4x = rotation_4x.var230[120:]
xiq_8x = rotation_8x.var230[120:]

line_plot_2D(xiq_003125x,xiq_00625x,xiq_0125x,xiq_025x,xiq_05x,xiq_1x,xiq_2x,
             xiq_4x, xiq_8x, 'Water vapour '+ r'($kg/m^2$)', 
             'water_vapour.pdf', y_invert = False)

vertical_integrated_water_vapor = global_mean_weighted(xiq_003125x,xiq_00625x,
                                                       xiq_0125x,xiq_025x,xiq_05x,
                                                       xiq_1x,xiq_2x,xiq_4x, xiq_8x)

global_mean_plot(vertical_integrated_water_vapor, '', 'blue', 
                 'Precipitable water / ' +r'$kg/m^2$', 'water_vapour_mean.pdf', 
                 legend = True, y_invert=False)


#%%
# TOA RADIATION
# Global mean

# Clear sky OLR
clrsky = global_mean_weighted(clrsky_003125x, clrsky_00625x, clrsky_0125x, clrsky_025x, 
                              clrsky_05x, clrsky_1x, clrsky_2x, clrsky_4x, 
                              clrsky_8x)

# All sky OLR
allsky = global_mean_weighted(allsky_003125x, allsky_00625x, allsky_0125x, allsky_025x, 
                              allsky_05x, allsky_1x, allsky_2x, allsky_4x, 
                              allsky_8x)

# Clear sky SW
isw = global_mean_weighted(isw_003125x, isw_00625x,isw_0125x, isw_025x, isw_05x, 
                           isw_1x, isw_2x, isw_4x, isw_8x)

# All sky SW
rsw = global_mean_weighted(rsw_003125x, rsw_00625x,rsw_0125x, rsw_025x, rsw_05x, 
                           rsw_1x, rsw_2x, rsw_4x, rsw_8x)

# Standard deviation
# Clear sky OLR
clrsky_error = global_std_weighted(clrsky_003125x, clrsky_00625x, clrsky_0125x, clrsky_025x, 
                                   clrsky_05x, clrsky_1x, clrsky_2x, clrsky_4x, 
                                   clrsky_8x)

# All sky OLR
allsky_error = global_std_weighted(allsky_003125x, allsky_00625x, allsky_0125x, allsky_025x, 
                                   allsky_05x, allsky_1x, allsky_2x, allsky_4x,
                                   allsky_8x)

# LW cloud effect std
LW_cloud_error = global_std_weighted(allsky_003125x-clrsky_003125x, 
                                     allsky_00625x-clrsky_00625x, 
                                     allsky_0125x-clrsky_0125x, 
                                     allsky_025x-clrsky_025x, 
                                     allsky_05x-clrsky_05x, allsky_1x-clrsky_1x, 
                                     allsky_2x-clrsky_2x, allsky_4x-clrsky_4x, 
                                     allsky_8x-clrsky_8x)

# All sky SW
rsw_error = global_std_weighted(rsw_003125x, rsw_00625x,rsw_0125x, rsw_025x, rsw_05x, 
                                rsw_1x, rsw_2x, rsw_4x, rsw_8x)

# Clear sky SW
isw_error = global_std_weighted(isw_003125x, isw_00625x,isw_0125x, isw_025x, isw_05x, 
                                isw_1x, isw_2x, isw_4x, isw_8x)

# SW cloud effect std
SW_cloud_error = global_std_weighted(rsw_003125x-isw_003125x,
                                     rsw_00625x-isw_00625x,rsw_0125x-isw_0125x, 
                                     rsw_025x-isw_025x, rsw_05x-isw_05x, 
                                     rsw_1x-isw_1x, rsw_2x-isw_2x, 
                                     rsw_4x-isw_4x, rsw_8x-isw_8x)

plot_radiation(isw, rsw, clrsky, allsky, isw_error, rsw_error, clrsky_error, 
               allsky_error, LW_cloud_error, SW_cloud_error)
# %%
