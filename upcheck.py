import nmap

target = "10.10.10.83"

nm = nmap.PortScanner()  # Constructing object nm
nm.scan(hosts=target, arguments='-sn -Pn -PE')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
for x, status in hosts_list:
    print('{0}:{1}'.x)
