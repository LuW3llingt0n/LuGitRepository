import os
import sys
import napalm
from pprint import pprint

def connect():
    """
    driver = napalm.get_network_driver("ios")
    device = driver(hostname='10.10.20.175', username='cisco', password='cisco')
    device.open()
    #pprint(device.get_facts())
    #device.load_merge_candidate(config='inter loop 12 \ndescr Napalm_Int')
    #device.load_replace_candidate(config='inter loop 12 \ndescr Napalm_Int') #Replace does not work with IOS
    device.load_merge_candidate(filename='napalm_configs.conf')
    device.commit_config()
    """
    driver2 = napalm.get_network_driver("nxos")
    device = driver2(hostname='10.10.20.177', username='cisco', password='cisco')
    device.open()
    mact = device.get_mac_address_table()
    #print(type(mact))
    if '00:00:0C:07:AC:0A' in mact:
        print("MAC found")
    else:
        print('fail')
    """
    for key in mact:
        print(key)
    findmac = mact.index('101')
    print(mact(findmac))
    
    // get facts and print hostname
    nxswitch = device.get_facts()
    #print(type(nxswitch))
    print(nxswitch.get('hostname'))
    
    for key, value in nxswitch.items():
        print(key, ':', value)
    //apply config
    device.load_merge_candidate(config='inter loop 12 \ndescr Napalm_Int v2')
    device.compare_config()
    device.commit_config()
    """

if __name__ == '__main__':
    connect()
