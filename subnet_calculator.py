#! /usr/bin/env python
"""
This script is a part of a tutorial to build a Python subnet Calculator.

The script accepts string inputs in the following formats:
`192.168.1.0/24` or `192.168.2.0/255.255.255.0`

Example Usage:

    $ python subnet_calc.py 192.168.1.0/26

Output:
    IP Subnet Calculator
    Subnet: 192.168.0.0/24

    Network:   192.168.0.0/24 (Private Internet)
    Netmask:   255.255.255.0 = 24
    Wildcard:  0.0.0.255

    Broadcast: 192.168.0.255
    HostMin:   192.168.0.1
    HostMax:   192.168.0.254
    Hosts/Net: 254
"""
import ipaddress


def main():
    """
    Execution of the script starts here
    """

    # Uncomment the line below the print() welcome message
    # print("IP Subnet Calculator")



if __name__ == "__main__":
    main()
