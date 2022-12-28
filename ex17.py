import psutil
import time
update_delay=1
def get_size(bytes):
    for unit in ['','K','M','G','T','P']:
        if bytes < 1024:
            return  f"{bytes:.2f}{unit}B"
        bytes/=1024
        io=psutil.net_io_counters()
        bytes_sent,bytes_recv=io.bytes_sent,io.bytes_recv
while True:
    time.sleep(update_delay)
    io_2=psutil.net_io_counters()
    us,ds=io_2.bytes_sent,io_2.bytes_recv
    print(f"UPload: {get_size(io_2.bytes_sent)} "
          f"downmload: {get_size(io_2.bytes_recv)} "
          f"upload speed: {get_size(us/update_delay)}/s "
          f"download speed: {get_size(ds/update_delay)}/s  ",end="\r")
    bytes_sent,bytes_recv=io_2.bytes_sent,io_2.bytes_recv