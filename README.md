# MACLookup Tool
For a given MAC address  retrieve company name

# Pre-requisite 
Assuming you have Python 3.x installed on your system

python --version
Python 3.6.4

python MacLookup.py --help
usage: MacLookup.py [-h] -mac MACADDRESS

optional arguments:
  -h, --help            show this help message and exit
  -mac MACADDRESS, --macaddress MACADDRESS
                        Mac address
                        
# Sample snippet 
usage : python MacLookup.py --macaddress 44:38:39:ff:ef:57 
output : MAC address belongs to Cumulus Networks, Inc
