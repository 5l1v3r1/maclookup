# MACLookup Tool
For a given MAC address  retrieve company name and virtual machine details

```
- Program accepts a command line parameter of a MAC address
- Program queries the API for a result over the network
- Program outputs the Company Name associated with that MAC address 
```

Install required packages

```
Step 1. python setup.py install
```

Execute the script with MAC address as an argument 

```
Step 2. python MacLookup.py -mac 6c:96:cf:de:a1:fd 
```

# Pre-requisite 
Assuming you have Python 3.x installed on your system

```
python --version

Python 3.6.4
```

# CLI command to retrieve MAC address details

```
python MacLookup.py --help

usage: MacLookup.py [-h] -mac MACADDRESS

optional arguments:
  -h, --help            show this help message and exit
  -mac MACADDRESS, --macaddress MACADDRESS
                        Mac address
```

# Sample snippet 

```
python MacLookup.py --macaddress 44:38:39:ff:ef:57 

MAC address belongs to Cumulus Networks, Inc

```

# Using Ephemeral Docker Containers as CLI Applications

You can pull docker image to local system using below command

```
docker pull prajithnair/maclookup
```

Once you have the image locally available,execute below command to use utility

```
docker run --rm -it prajithnair/maclookup --mac 5a:32:d8:eb:23:8c

```
