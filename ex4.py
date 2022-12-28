from netmiko import ConnectHandler
csr={
    "device_type":"cisco_ios",
    "ip":"sandbox-iosxe-latest-1.cisco.com",
    "port": 22,
    "username": "developer",
    "password":"C1sco12345"
}
net_connect=ConnectHandler(**csr)
output=net_connect.send_command('show ip int brief')
print(output)
output1=net_connect.send_command('show run')
print(output1)
output_runhost=net_connect.send_command('show run | i host')
print(output_runhost)
