from recontool.whois_lookup import get_whois
from recontool.banner_grabber import grab_banner
from recontool.dns_lookup import resolve_domain
from recontool.port_scanner import scan_ports

def print_whois(domain):
    print("\n[ WHOIS Lookup ]")
    result = get_whois(domain)
    if "error" in result:
        print("Error:", result["error"])
    else:
        for key, value in result.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")

def print_dns(domain):
    print("\n[ DNS Resolution ]")
    ip = resolve_domain(domain)
    if ip:
        print(f"{domain} resolves to {ip}")
    else:
        print("Could not resolve domain.")
    return ip

def print_ports(ip):
    print("\n[ Port Scan ]")
    open_ports = scan_ports(ip)
    if open_ports:
        for port in open_ports:
            banner = grab_banner(ip, port)
            print(f"Port {port} is OPEN - Banner: {banner}")
    else:
        print("No open common ports found.")

def menu():
    while True:
        print("\n====== ReconTool - Menu ======")
        print("1. WHOIS Lookup")
        print("2. DNS Resolution")
        print("3. Port Scan + Banner Grabber")
        print("4. Full Scan")
        print("5. Exit")
        option = input("Select an option: ")

        if option == "5":
            print("Exiting ReconTool...")
            break
        elif option not in ("1", "2", "3", "4"):
            break

        domain = input("Enter target domain (Ex: google.com): ").strip()

        if option == "1":
            print_whois(domain)
        elif option == "2":
            print_dns(domain)
        elif option == "3":
            ip = print_dns(domain)
            if ip:
                print_ports(ip)
        elif option == "4":
            print_whois(domain)
            ip = print_dns(domain)
            if ip: 
                print_ports(ip)
        else: 
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()