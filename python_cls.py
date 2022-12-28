'''import  sys
print(sys.version)
import socket
print(socket.gethostname())
h=socket.gethostname()
add=socket.gethostbyname(h)
print(add)'''
import  os
with open("ip_list.txt") as file:
    park=file.read()
    park=park.splitlines()
    print(" {park}  \n")
for ip in park:
    response = os.popen(f"ping {ip}").read()
    if("Request time out."or"unreachable") in response:
        print(response)
        f=open("info_output.txt","a")
        f.write(str(ip)+ 'link is down '+'\n')
        f.close()
    else:
        print(response)
        f = open("info_output.txt", "a")
        f.write(str(ip) + 'is up' + '\n')
        f.close()
with open("ip_otput.txt") as file:
    output=file.read()
    print(output)
with open("info_output.txt","w") as file:
    pass
