import requests
import os
import argparse
import re

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument( '-mac', '--macaddress', type=str,
                         default='Default', help='Mac address',required='True')
    return parser.parse_args()

if __name__ == '__main__':
        mac_address = vars( parse_args() )
        if re.match( "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac_address['macaddress'].lower() ):
            env_var = os.environ
            API_KEY = env_var['API_KEY']
            api_url = 'https://api.macaddress.io/v1'
            response = requests.get(url= api_url + '?output=json&search=' + mac_address['macaddress'],headers= {'X-Authentication-Token': API_KEY} )
            company_name = response.json()['vendorDetails']['companyName']
            virtual_machine = response.json()['macAddressDetails']['virtualMachine']
            if company_name:
                print (f'MAC address belongs to {company_name} and virtual machine is {virtual_machine}')
            else:
                print (f'MAC address does not have a Company Name')
        else :
            print (f'Supplied input is invalid MAC Address!')
            exit()




