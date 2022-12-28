import  socket
s=socket.socket()
print("socket is created")
port=40674
s.bind(('',port))
print("socket bind to %s" %(port))
s.listen(5)
print("socket is listening")
while True:
    c,adder=s.accept()
    print('got connection from',adder)
    print(c)
    c.send(b'tahnk you for connecting')
    c.close()