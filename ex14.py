'''import scapy.all as scapy

request=scapy.ARP()
print(request.summary())
print(request.show())'''
from scapy.all import  *
'''
ip=IP()
print(ip)
print(ip.show())
my_frame=Ether() / ICMP()
print(my_frame)
print("============================")
print(my_frame.show())'''
'''
from scapy.all import *
s=IP(dst='google.com')/ICMP()
print(s.show())'''
