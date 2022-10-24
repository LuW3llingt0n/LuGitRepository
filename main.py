from netmiko import ConnectHandler
from genie.conf import Genie

def connect():
    # Use a breakpoint in the code line below to debug your script.
    net_connect = ConnectHandler(
        device_type="cisco_xe",
        host="10.10.20.175",
        username='cisco',
        password='cisco',
    )
    # output = net_connect.send_command("show ip int brief")
    output1 = net_connect.send_command("show ip int brief")
    print(output1)
    output2 = net_connect.send_command_timing("show ip int brief", use_genie=True)
    print(output2)
    net_connect.disconnect()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    connect()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
