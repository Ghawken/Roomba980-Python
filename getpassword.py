#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "1.0"
'''
Python 2.7
Quick Program to get blid and password from roomba 980

Nick Waterton 5th May 2017: V 1.0: Initial Release
'''

from roomba import password

if __name__ == '__main__':
    import argparse
    #-------- Command Line -----------------
    parser = argparse.ArgumentParser(description='Forward MQTT data from Roomba 980 to local MQTT broker')
    parser.add_argument('-f','--configfile', action='store',type=str, default="./config.ini", help='config file name, default: ./config.ini)')
    parser.add_argument('-R','--roombaIP', action='store',type=str, default=None, help='ipaddress of Roomba 980 (default: None)')
    arg = parser.parse_args()
    
    if arg.roombaIP is None:
        password(file=arg.configfile)
    else:
        password(arg.roombaIP,file=arg.configfile)
