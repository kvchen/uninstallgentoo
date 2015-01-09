# !/usr/bin/env python
# coding: utf-8

"""
Uninstall Gentoo!

Handles automation of starting and controlling the interactive livestream.
"""

__author__ = "kvchen"
__repository__ = "https://github.com/kvchen/uninstallgentoo"
__status__ = "development"



# Import default helper modules
import argparse
import logging
import os



# Set save location for the logfile
file_name = "logs/monitor.log"
logging.basicConfig(filename=file_name, level=logging.INFO)



def main():
    parser = argparse.ArgumentParser(description="run Twitch Installs Arch")
    parser.add_argument("-d", "--debug", action="store_true", 
    	help="run uninstallgentoo in debug mode")
    args = parser.parse_args()


    return


if __name__ == "__main__":
    main()