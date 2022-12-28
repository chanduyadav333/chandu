import  psutil
network_state=psutil.net_io_counters(pernic=False)
bytes_sent=getattr(network_state,'bytes_sent')
bytes_recv=getattr(network_state,'bytes_recv')
print("Bytes Sent = {0} | Bytes received = {1}".format(bytes_sent,bytes_recv))