from genie.testbed import load
from pprint import pprint


def connect():
    testbed = load('yaml/testbed.yml')
    device = testbed.devices['dist-rtr01']
    device.connect()
    interfaces = device.parse('show ip ospf neighbor')
    pprint(interfaces["interfaces"])

    device = testbed.devices['dist-sw01']
    device.connect()
    mac = device.parse('show mac address-table')
    pprint(mac)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    connect()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
