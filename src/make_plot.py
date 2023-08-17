#%%
import numpy as np
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
from functions import *

#%%
def line_plot_2D(s5,s4,s3,s2,s1,ctl,f1,f2,f3, ylabel, savefig, y_invert=False): 
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    fig,ax = plt.subplots(figsize=(12,8))
    ax.spines[['right', 'top']].set_visible(False)
    ax.spines.left.set_position(('outward', 10))
    ax.spines.bottom.set_position(('outward', 10))
    
    x = np.sin(np.deg2rad(ctl.lat))
    y = zonal_time_avg(s5,s4,s3,s2,s1,ctl,f1,f2,f3,time = True, lon = True)
    cm = plt.cm.RdBu_r(np.linspace(0, 1, len(y)+1))
    cm_slow = cm[4::-1]
    cm_fast = cm[8:5:-1]
    width = 4
    label = ['1/32x','1/16x','1/8x', '1/4x', '1/2x', 'control', '2x', '4x','8x']
    
    count = 0
    for i in range(len(y)):
        if i == 5:
            ax.plot(x, y[i], color = 'black', label = label[i], linewidth = width, linestyle = 'dotted')
        elif i > 5: 
            ax.plot(x, y[i], color = cm_fast[count],label = label[i], linewidth = width)
            count+=1
        else:
            ax.plot(x, y[i], color = cm_slow[i],label = label[i], linewidth = width)
        
    ticks_deg = np.array([-90, -60, -40, -20, 0, 20, 40, 60, 90])
    ax.xaxis.set_ticks(list(np.sin(np.deg2rad(ticks_deg))))
    ax.set_xticklabels(ticks_deg)
    ax.xaxis.set_tick_params(labelsize=20)
    ax.yaxis.set_tick_params(labelsize=20)
    plt.legend(fontsize=19)
    plt.ylabel(ylabel, size=24)
    plt.xlim(0,np.sin(np.deg2rad(90)))
    if y_invert == True:
        ax.invert_yaxis()
    plt.xlabel('Latitude /'r'$^\circ$N', size=24)
    plt.savefig(savefig)
    
    
    
def line_plot_plev(s5,s4,s3,s2,s1,ctl,f1,f2,f3, xlabel, savefig, y_invert=False): 
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    fig,ax = plt.subplots(figsize=(7,7))
    ax.spines[['right', 'top']].set_visible(False)
    ax.spines.left.set_position(('outward', 10))
    ax.spines.bottom.set_position(('outward', 10))
    
    data_concat = xr.concat([s5,s4,s3,s2,s1,ctl,f1,f2,f3], pd.Index(np.arange(0,9), name='length'))
    x = (ctl.plev)/100
    y = data_concat.mean(dim = ['time','lat','lon'])
    cm = plt.cm.RdBu_r(np.linspace(0, 1, len(y)))
    width = 2
    label = ['1/32x','1/16x','1/8x', '1/4x', '1/2x', 'control', '2x', '4x','8x']
    
    for i in range(len(y)):
        if i == 5:
            ax.plot( y[i,:13], x[:13], color = 'black', label = label[i], linewidth = width, linestyle = 'dotted')
        else:
            ax.plot( y[i,:13], x[:13], color = cm[i], label = label[i], linewidth = width)
        
    ax.xaxis.set_tick_params(labelsize=14)
    ax.yaxis.set_tick_params(labelsize=14)
    plt.legend(fontsize=14)
    plt.xlabel(xlabel, size=16)
    if y_invert == True:
        ax.invert_yaxis()
    plt.ylabel('hPa', size=16)
    plt.savefig(savefig)
    
    
    
def global_mean_plot(y, label, color, ylabel, savefig, legend = True, y_invert=False):
    
    import numpy as np
    import matplotlib.pyplot as plt
    fig,ax = plt.subplots(figsize=(12,8))
    ax.spines[['right', 'top']].set_visible(False)
    ax.spines.left.set_position(('outward', 10))
    ax.spines.bottom.set_position(('outward', 10))
    
    x = np.arange(0,9)
    ticks = ['1/32','1/16','1/8','1/4','1/2','1','2','4','8']
    if len(y.shape) == 1:
        ax.plot(x,y, color = color, linewidth = 4, label = label, marker = 'o', markersize = 9)
    else:
        for i in range(len(y)):
            ax.plot(x,y[i], color = color[i], linewidth = 4, label = label[i], marker = 'o', markersize = 9)
    #ax.set_xscale('log', base=2)
    ax.xaxis.set_tick_params(labelsize=20)
    ax.yaxis.set_tick_params(labelsize=20)
    ax.xaxis.set_ticks(x)
    ax.set_xticklabels([x for x in ticks])
    plt.xlabel('Rotation rate '+ r'$\Omega/\Omega_{e}$', size=24)
    plt.ylabel(ylabel, size=24)
    if legend == True:
        plt.legend(fontsize=19)
    if y_invert == True:
        ax.invert_yaxis()
    plt.savefig(savefig)
    
    
def lat_plev_9plot(s5,s4,s3,s2,s1,ctl,f1,f2,f3, levels, vmin, vmax, clabel, savefig, extend = 'both',cmap='RdBu', y_invert=False):
    
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.axes_grid1.inset_locator import inset_axes
    
    x, y = np.meshgrid(np.sin(np.deg2rad(ctl.lat)),ctl.plev/100)
    #x, y = np.meshgrid(ctl.lat,ctl.plev/100)
    z = zonal_time_avg(s5,s4,s3,s2,s1,ctl,f1,f2,f3, time = True, lon = True)
    
    fig, ax = plt.subplots(nrows=3, ncols=3,figsize=(18,12),sharey='row',sharex='col')
    ax = ax.ravel()
    ticks_deg = np.array([ -60, -30, 0, 30, 60])
    title = ['1/32 'r'$\Omega$','1/16 'r'$\Omega$','1/8 'r'$\Omega$', 
             '1/4 'r'$\Omega$', '1/2 'r'$\Omega$', 
             'control', '2 'r'$\Omega$', '4 'r'$\Omega$',
             '8 'r'$\Omega$']
    
    for i in range(len(ax)):
        cont = ax[i].contourf(x, y, z[i], cmap = cmap, levels = levels, vmin = vmin, vmax = vmax, extend = extend); 
        #ax[i].xaxis.set_ticks(list(ticks_deg))
        ax[i].xaxis.set_ticks(list(np.sin(np.deg2rad(ticks_deg))))
        ax[i].set_xticklabels(ticks_deg)
        ax[i].set_title(title[i],fontsize=24)
        if i == 0 or i == 3 or i == 6:
            ax[i].invert_yaxis()
        ax[i].xaxis.set_tick_params(labelsize=20); ax[i].yaxis.set_tick_params(labelsize=20)
    
    plt.tight_layout()
    cbar=fig.colorbar(cont, ax=ax[:], shrink=0.6, location='right',pad=0.04,aspect=30)
    cbar.ax.tick_params(labelsize=20)
    cbar.set_label(clabel,rotation=0,fontsize=20,labelpad=-40, y=1.2)
    
    plt.savefig(savefig)
    

def line_plot_2D_slow(s5,s4,s3,s2,s1,ctl,f1,f2,f3, ylabel, savefig, y_invert=False): 
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    fig,ax = plt.subplots(figsize=(12,8))
    ax.spines[['right', 'top']].set_visible(False)
    ax.spines.left.set_position(('outward', 10))
    ax.spines.bottom.set_position(('outward', 10))
    
    x = np.sin(np.deg2rad(ctl.lat))
    y = zonal_time_avg(s5,s4,s3,s2,s1,ctl,f1,f2,f3,time = True, lon = True)
    #color = ['maroon','firebrick','indianred','lightcoral','black','lightsteelblue','cornflowerblue','royalblue']
    cm = plt.cm.RdBu_r(np.linspace(0, 1, len(y)+1))
    cm_slow = cm[4::-1]
    cm_fast = cm[8:5:-1]
    width = 4
    label = ['1/32x','1/16x','1/8x', '1/4x', '1/2x', 'control', '2x', '4x','8x']
    
    count = 0
    for i in range(len(y)):
        if i < 4:
            ax.plot(x, y[i], color = cm_slow[i],label = label[i], linewidth = width)
        
    ticks_deg = np.array([-90, -60, -40, -20, 0, 20, 40, 60, 90])
    ax.xaxis.set_ticks(list(np.sin(np.deg2rad(ticks_deg))))
    ax.set_xticklabels(ticks_deg)
    ax.xaxis.set_tick_params(labelsize=20)
    ax.yaxis.set_tick_params(labelsize=20)
    plt.legend(fontsize=19)
    plt.ylabel(ylabel, size=24)
    plt.xlim(0,np.sin(np.deg2rad(90)))
    if y_invert == True:
        ax.invert_yaxis()
    plt.xlabel('Latitude /'r'$^\circ$N', size=24)
    plt.savefig(savefig)

# %%
def plot_radiation(isw, rsw, clrsky, allsky, isw_error, rsw_error, clrsky_error, allsky_error, LW_cloud_error, SW_cloud_error):
    fig, ax = plt.subplots(nrows=2, ncols=2,figsize=(14,14),gridspec_kw={'height_ratios': [2, 1]},sharex='col') # sharey='row'

    x = np.arange(0,9)
    ticks = [r'$\dfrac{1}{32}$',r'$\dfrac{1}{16}$',r'$\dfrac{1}{8}$',r'$\dfrac{1}{4}$',r'$\dfrac{1}{2}$','1','2','4','8']

    ax[0][0].plot(x,isw, marker = 'o', markersize = 4, linestyle = 'dashed', color = 'dodgerblue', linewidth = 2)
    ax[0][0].errorbar(x, isw , yerr = isw_error, fmt = 'o', color='dodgerblue', ecolor='black', elinewidth=2, capsize=2);
    ax[0][0].spines[['right', 'top']].set_visible(False)
    ax[0][0].plot(x,rsw, marker = 'o', markersize = 4, color = 'dodgerblue', linewidth = 2)
    ax[0][0].errorbar(x, rsw , yerr = rsw_error, fmt = 'o', color='dodgerblue', ecolor='black', elinewidth=2, capsize=2);
    ax[0][0].spines[['right', 'top']].set_visible(False)
    ax[0][0].set_ylabel(r'$W/m^2$',fontsize=20)
    ax[0][0].set_title('Incoming SW',fontsize=24)
    ax[0][0].spines.left.set_position(('outward', 10))
    ax[0][0].spines.bottom.set_position(('outward', 10))
    #ax[0][0].set_xscale('log', base=2)
    ax[0][0].xaxis.set_ticks(x)
    ax[0][0].set_xticklabels([x for x in ticks])
    ax[0][0].set_ylim(220, 310)

    lgd_clear, = ax[0][1].plot(x, clrsky, marker = 'o', markersize = 4, linestyle = 'dashed', color = 'crimson', linewidth = 2, label = 'Clear sky')
    ax[0][1].errorbar(x, clrsky , yerr = clrsky_error, fmt = 'o', color='crimson', ecolor='black', elinewidth=2, capsize=2);
    ax[0][1].spines[['right', 'top']].set_visible(False)
    lgd_all, = ax[0][1].plot(x,allsky, marker = 'o', markersize = 4, color = 'crimson', linewidth = 2, label = 'All sky')
    ax[0][1].errorbar(x, allsky , yerr = allsky_error, fmt = 'o', color='crimson', ecolor='black', elinewidth=2, capsize=2);
    ax[0][1].spines[['right', 'top']].set_visible(False)
    ax[0][1].set_title('Outgoing LW',fontsize=24)
    ax[0][1].spines.left.set_position(('outward', 10))
    ax[0][1].spines.bottom.set_position(('outward', 10))
    #ax[0][1].set_xscale('log', base=2)
    ax[0][1].xaxis.set_ticks(x)
    ax[0][1].set_xticklabels([x for x in ticks])
    ax[0][1].set_ylim(-310, -220)
    ax[0][1].invert_yaxis()

    ax[1][0].plot(x, rsw - isw, marker = 'o', markersize = 4, linestyle = 'dotted', color = 'dodgerblue', linewidth = 2)
    ax[1][0].errorbar(x, rsw - isw , yerr = SW_cloud_error, fmt = 'o', color='dodgerblue', ecolor='black', elinewidth=2, capsize=2);
    ax[1][0].spines[['right', 'top']].set_visible(False)
    ax[1][0].invert_yaxis(); ax[1][0].set_ylabel(r'$W/m^2$',fontsize=20)
    ax[1][0].set_xlabel(r'$\Omega/\Omega_{e}$', size=20)
    ax[1][0].set_title('SW cloud radiative effect',fontsize=24)
    ax[1][0].spines.left.set_position(('outward', 10))
    ax[1][0].spines.bottom.set_position(('outward', 10))
    #ax[1][0].set_xscale('log', base=2)
    ax[1][0].xaxis.set_ticks(x)
    ax[1][0].set_xticklabels([x for x in ticks])
    ax[1][0].set_ylim(-90, -10)
    ax[1][0].invert_yaxis()

    lgd_cloud, = ax[1][1].plot(x,(allsky - clrsky), marker = 'o', markersize = 4, linestyle = 'dotted', color = 'crimson', linewidth = 2, label = 'cloud')
    ax[1][1].errorbar(x, (allsky - clrsky) , yerr = LW_cloud_error, fmt = 'o', color='crimson', ecolor='black', elinewidth=2, capsize=2);
    ax[1][1].spines[['right', 'top']].set_visible(False)
    ax[1][1].set_title('LW cloud radiative effect',fontsize=24)
    ax[1][1].spines.left.set_position(('outward', 10))
    ax[1][1].spines.bottom.set_position(('outward', 10))
    #ax[1][1].set_xscale('log', base=2)
    ax[1][1].xaxis.set_ticks(x)
    ax[1][1].set_xticklabels([x for x in ticks])
    ax[1][1].set_ylim(10, 90)
    ax[1][1].set_xlabel(r'$\Omega/\Omega_{e}$', size=20)

    ax[0][1].yaxis.set_tick_params(labelsize=18)
    ax[1][0].xaxis.set_tick_params(labelsize=18)
    ax[1][0].yaxis.set_tick_params(labelsize=18)
    ax[0][0].yaxis.set_tick_params(labelsize=18)
    ax[1][1].xaxis.set_tick_params(labelsize=18)
    ax[1][1].yaxis.set_tick_params(labelsize=18)

    #plt.legend(loc='best')
    #ax[1][1].legend(numpoints=1)

    plt.savefig('Radiation_TOA.pdf')
# %%
