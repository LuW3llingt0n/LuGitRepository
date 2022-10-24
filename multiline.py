from netmiko import ConnectHandler


def connect():
    # Use a breakpoint in the code line below to debug your script.
    net_connect = ConnectHandler(
        device_type="cisco_xe",
        host="10.10.20.175",
        username='cisco',
        password='cisco',
    )

    cmd_list = ["interface loopback10", "description Netmiko Interface", "no shut"]
    # output = net_connect.send_command("show ip int brief")
    output1 = net_connect.send_config_set(cmd_list)
    print(output1)
    net_connect.disconnect()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    connect()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
