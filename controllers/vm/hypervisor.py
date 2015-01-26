""" Handles interfacing with virtual machines. """

import virtualbox
import logging

vbox = virtualbox.VirtualBox()


class Hypervisor(object):
    """Controls all virtual machines spawned by the program. Responsible for 
    creating, maintaining, and removing VMs as required.
    """
    def __init__(self):
        return


class VirtualMachine(object):
    """Acts as a wrapper for a VirtualBox virtual machine. Provides methods
    needed for an internal representation of a VM.
    """
    def __init__(self):
        return

    def on(self):
        return

    def off(self):
        return

    def reboot(self):
        return