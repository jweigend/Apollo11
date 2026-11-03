"""Lunar landing simulation flown by the real Luminary 099 guidance software.

The package couples a 6-degree-of-freedom model of the Apollo 11 Lunar
Module (mass, descent engine, RCS jets, IMU) to the emulated AGC: the
vehicle feeds PIPA and CDU pulses to the computer, the computer flies the
vehicle through its channels (engine on/off, throttle, trim gimbal, RCS).
"""
