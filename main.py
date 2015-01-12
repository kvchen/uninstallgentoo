# !/usr/bin/env python
# coding: utf-8


# Uninstall Gentoo
# Copyright (C) 2015 Kevin Chen

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


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


# Import application-specific modules
import config


# Set save location for the logfile
file_name = "logs/monitor.log"
logging.basicConfig(filename=file_name, level=logging.INFO)


def main():
    parser = argparse.ArgumentParser(description="run uninstallgentoo")
    parser.add_argument("-d", "--debug", action="store_true", 
        help="run uninstallgentoo in debug mode")
    args = parser.parse_args()

    if args.debug:
        logging.warn("Starting program in debug mode")

    return


if __name__ == "__main__":
    main()


