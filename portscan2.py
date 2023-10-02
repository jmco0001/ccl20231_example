import nmap

def scan_network(target):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-F')  # Fast scan

    for host in nm.all_hosts():
        print(f"Host: {host}")
        print(f"State: {nm[host].state()}")

        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")

            ports = nm[host][proto].keys()
            for port in ports:
                state = nm[host][proto][port]['state']
                service = nm[host][proto][port]['name']
                print(f"Port: {port} - State: {state} - Service: {service}")

def main():
    target = input("Enter the target or network to scan (e.g., 192.168.1.0/24): ")
    scan_network(target)

if __name__ == "__main__":
    main()

