from  netmiko import ConnectHandler
with open('devices.txt') as router:
    for IP in router:
        Router={
            "device_type": "cisco_ios",
            "ip": "sandbox-iosxe-latest-1.cisco.com",
            "username": "developer",
            "password": "C1sco12345"
        }
        net_connect = ConnectHandler(**Router)
        print('Connecting to'+IP)
        print('-'*79)
        output = net_connect.send_command('show ip int brief')
        print(output)
        print()
        print('-'*79)

net_connect.disconnect()