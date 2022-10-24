from genie.testbed import load
from genie.conf.base import Interface


def connect():
    testbed = load('yaml/testbed.yml')
    uut = testbed.devices['uut']
    uut.connect()

    add_interface = Interface(device=uut, name='Loopback11')
    add_interface.ipv4 = '1.1.1.11'
    add_interface.ipv4.netmask = '255.255.255.128'
    add_interface.shutdown = True

    print(add_interface.build_config(apply=False))
    # To apply on the device
    add_interface.build_config()
    #nxos_interface.build_unconfig()  # To remove configuration


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    connect()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
