# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 07:22:31 2022

@author: Jonas Beuchert
"""
import os
import numpy as np
import datetime as dt
import pymap3d as pm
import eph_util as ep
import coarse_time_navigation as ctn

# %% 1.) Read 11 ms
data_path = ""
ms_to_process = 11  # [ms]
# Name of data file (signal record)
file_name = os.path.join(data_path,
                         "GPSdata-DiscreteComponents-fs38_192-if9_55.bin")
# Data type used to store one sample
data_type = "int8"
# Decimation factor for resampling
decimation_factor = 7
# Intermediate, sampling, and code frequencies
intermediate_frequency = 9.548e6 / decimation_factor  # [Hz]
sampling_frequency = 38.192e6 / decimation_factor  # [Hz]
code_frequency_basis = 1.023e6  # [Hz]
# Number of chips in a code period
code_length = 1023
samples_per_code = round(
    sampling_frequency / (code_frequency_basis / code_length)
    )  # Find number of samples per spreading code
# Open raw data file
# Read 11-ms snapshot
data = np.fromfile(file_name, dtype=data_type,
                   count=decimation_factor * ms_to_process * samples_per_code)
# %% 2.) Resample
# Resample data in a crude way
data = data[:-1:decimation_factor]
# Change to 1-bit quantization
data = np.sign(data + 0.5)
# %% 3.) Acquisition
# Estimate code phases
acquired_sv, acquired_snr, acquired_doppler, acquired_codedelay, \
    acquired_fine_freq, _, _, _ \
    = ep.acquisition(longsignal=data,
                     IF=intermediate_frequency,
                     Fs=sampling_frequency,
                     freq_step=50,  # 500
                     ms_to_process=11,
                     prn_list=np.arange(start=1, stop=33),
                     # prn_list=np.array([3, 15, 18, 21, 22]),
                     expected_doppler=0.0,
                     max_doppler_err=5000.0,
                     code_phase_interp='quadratic',
                     fine_freq=False,  # True
                     gnss='gps',
                     l1c=False,
                     snr_threshold=18.0)
# Visible / acquired satellites, their Doppler shifts, and code phases
# doppler_shifts = - (acquired_fine_freq
#                     - intermediate_frequency)  # [Hz] (sign change!)
doppler_shifts = - acquired_doppler  # [Hz] (sign change!)
code_phases = (samples_per_code - acquired_codedelay) / sampling_frequency
# %% 4.) Ephemeris
# Time interval to search
t_min = dt.datetime(2005, 5, 7, 12, 0, 0)
t_max = dt.datetime(2005, 5, 7, 23, 59, 59)
# Load the ephemeris:
yyyy = t_min.year  # 4-digit year
ddd = t_min.timetuple().tm_yday  # Day of the year
yy = yyyy % 100  # 2-digit year
file_name = "brdc{:03d}0.{:02d}n".format(ddd, yy)
download_dir = ""  # Directory where unpacked ephemeris data is stored
file_path = os.path.join(download_dir, file_name)  # Path to ephemeris file
eph = ep.rinexe(file_path)  # Load ephemeris
# %% 5.) Cold snapshot
state, res, t = ctn.cold_snapshot(code_phases,
                                  doppler_shifts,
                                  np.datetime64(t_min),
                                  np.datetime64(t_max),
                                  eph,
                                  PRN=acquired_sv)
# Display results
lat_cold, lon_cold, h_cold = pm.ecef2geodetic(state[0], state[1], state[2])
latitude = 40.00806  # [deg]
longitude = -105.26267  # [deg]
ref_pos = np.array([-1.288159766699346e+06,
                    -4.720787585489457e+06,
                    4.079715377122427e+06])  # ECEF XYZ [m,m,m]
lat_ref, lon_ref, _ = pm.ecef2geodetic(ref_pos[0],
                                       ref_pos[1],
                                       ref_pos[2])  # Reference in geodetic coordinates [deg]
print()
print("Ground truth:")
print(f"Latitude: {latitude}°")
print(f"Longitude: {longitude}°")
print()
print("Standard GPS estimate:")
print(f"Latitude: {lat_ref}°")
print(f"Longitude: {lon_ref}°")
print()
print("Cold snapshot estimate:")
print(f"Latitude: {lat_cold}°")
print(f"Longitude: {lon_cold}°")
