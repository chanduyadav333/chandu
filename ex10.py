import ifaddr
adapetrs=ifaddr.get_adapters(include_unconfigured=True)
for adapetr in adapetrs:
    print("ips of network adapter "+adapetr.nice_name)
    if adapetr.ips:
        for ip in adapetr.ips:
            print("   %s/%s" %(ip.ip,ip.network_prefix))
    else:
         print("no ip")