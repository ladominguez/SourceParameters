import glob
import os
from obspy.core.utcdatetime import UTCDateTime
import numpy as np
import json

def residuals(d_obs, d_model):
	return np.mean(np.power(d_obs-d_model,2))

def variance_reduction(d_obs, d_model):
	#d_avg = np.mean(d_obs)
	#d_obs = d_obs - d_avg
	#d_model = d_model - d_avg
	return (1.-np.sum(np.power(d_obs - d_model,2))/np.sum(np.power(d_obs,2)))*100.

def coeff_r2(d_obs, d_model):
	d_avg   = np.mean(d_obs)
	tot_var = np.sum(np.power(d_obs - d_avg,2))
	res     = np.sum(np.power(d_obs - d_model,2))
	return (1.-res/tot_var)*100


def clean_directory(dir,type_resp):
    #previous = glob.glob(os.path.join(dir, "*" + type_resp  + "*.png"))
    previous = glob.glob(os.path.join(dir, "*.png")) # Clean all
    for png_file in previous:
        os.remove(png_file)


def G(r, azimuth):
    # Escribe tu código aquí
    return None    




def Q(f, azimuth):
# Escribe tu código aquí
    return None


def M0_func(Mw):
    return np.power(10, Mw*1.5+9.1)

def Mw_log(M0_log):
    return (2./3.)*(M0_log - 9.1)

def stress_drop(freq_cut, kappa, vel_wave, Moment):
    #print('kappa: ', kappa)
    #print('beta', vel_wave)
    return (7./16)*Moment*(freq_cut/(kappa*vel_wave))**3


def rms(data):
    return np.sqrt(np.mean(np.power(data, 2)))

def brune_spectrum(f,M0,fc, resp_type):
    if resp_type == "DISP":
        Sb = M0/(1+(f/fc)**2)
    elif resp_type == "VEL":
        Sb = M0*(2*np.pi*f)/(1+(f/fc)**2)
    elif resp_type == "ACC":
        Sb = M0*(2*np.pi*f)**2/(1+(f/fc)**2)
    else:
        None
    return Sb

def fit_curve(fdata, Bdata, resp_type):
    B0 = np.round(np.log10(np.mean(Bdata)))
    Bt = np.linspace(np.round(np.log10(np.mean(Bd)))-1, np.round(np.log10(np.mean(Bd)))+1, 21)
    ft = np.linspace(0.5,14,15)
    return None

#def brune_log(f, log_M0, fc):
#    if resp_type == "DISP":
#        Sb_log = log_M0-np.log10((1+(f/fc)**2))
#    elif resp_type == "VEL":
#        Sb_log = log_M0+np.log10(2*np.pi*f)-np.log10(1+(f/fc)**2)
#    elif resp_type == "ACC":
#        Sb_log = log_M0+2*np.log10(2*np.pi*f)-np.log10(1+(f/fc)**2)
#    else:
#        None
#    return Sb_log

# def brune_1p(f, fc):
#    if resp_type == "DISP":
#        Sb_log = -np.log10((1+(f/fc)**2))
#    elif resp_type == "VEL":
#        Sb_log = np.log10(2*np.pi*f)-np.log10(1+(f/fc)**2)
#    elif resp_type == "ACC":
#        Sb_log = 2*np.log10(2*np.pi*f)-np.log10(1+(f/fc)**2)
#    else:
#        None
#    return Sb_log
