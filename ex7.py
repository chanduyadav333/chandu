import  uuid
print(hex(uuid.getnode()))
print("the mac address in formatted way is : ",end="")
print(':'.join(['{:02x}'.format((uuid.getnode()>>ele)&0xff)
                for ele in range(0,8*6,8)][::-1]))