import socket

def scan_port(host, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for the connection attempt (adjust as needed)
        s.settimeout(2)
        
        # Attempt to connect to the target host and port
        s.connect((host, port))
        
        # If the connection was successful, the port is open
        print(f"Port {port} is open")
        
        # Close the socket
        s.close()
    except (socket.timeout, ConnectionRefusedError):
        # If there's a timeout or connection refused error, the port is closed
        print(f"Port {port} is closed")

def main():
    # Specify the target host and a range of ports to scan
    target_host = input("Enter the target host: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    
    # Loop through the range of ports and scan each one
    for port in range(start_port, end_port + 1):
        scan_port(target_host, port)

if __name__ == "__main__":
    main()

