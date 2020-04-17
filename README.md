# Build a Subnet Calculator

In this tutorial, we'll build an IP subnet calculator using Python.

### What you'll Learn

* Creating Python scripts

* Creating and assigning values to variables

* Reading input from the CLI

* Working with Strings and String Methods

* Importing and using modules

* String Formatting

### What you'll Build

![](./subnet_calc.jpg)

## Initial Script

```python
#! /usr/bin/env python
"""
This script is a part of a tutorial to build a Python subnet Calculator.

The script accepts string inputs in the following formats:
`192.168.1.0/24` or `192.168.2.0/255.255.255.0`

Example Usage:

    $ python subnet_calc.py 192.168.1.0/26

Output:
    IP Subnet Calculator
    Subnet: 192.168.0.0/26

    Network:   192.168.0.0/24 (Private Internet)
    Netmask:   255.255.255.0 = 24
    Wildcard:  0.0.0.255

    Broadcast: 192.168.0.255
    HostMin:   192.168.0.1
    HostMax:   192.168.0.254
    Hosts/Net: 254
"""


def main():
    """
    Execution of the script starts here
    """

    # Uncomment the line below the print() welcome message
    # welcome_message = "IP Subnet Calculator"
    # print(welcome_message)



if __name__ == "__main__":
    main()

```

## Build Steps
