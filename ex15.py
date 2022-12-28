from  scapy.all import  *
'''
a=IP(ttl=10)
#print(a)
#print(a.src)
print(a.show())
a.dst="192.168.1.1"
#print(a)
#print(a.src)
print(a.show())
print("===========================")
del (a.ttl)
print(a.show())
b=IP()
print(b.show)'''
'''
c=IP()/TCP()
print(c.show())
d= Ether()/IP()/TCP()
print(d.show())
e=IP()/TCP()/"GET / HTTP/1.0\r\n\r\n"
print(e.show())'''
'''
j=a=Ether()/IP(dst="www.slashdot.org")/TCP()/"GET /index.html HTTP/1.0 \n\n"
print(hexdump(j))
#print(a.show())'''
k=IP(dst='www.slashdot.org/31')
dst=Net('www.slashdot.org/31')
print([p for p in k])
print(k)