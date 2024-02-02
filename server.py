"The application is just a terminal front end for the DHCP server non of the commands work it just prints (Processing ASK command...) "


def process_command(self, command):
        if command == "ASK":
            print("Processing ASK command...")
            ip_address = self.get_ip_address()
            print(f"Offer: Your IP address is {ip_address}")

            # Set the timer for the IP address
            self.set_timer(ip_address)

        elif command.startswith("RENEW"):
            ip_to_renew = command[len("RENEW"):].strip()
            print("COMMAND: " + command)
            if ip_to_renew in self.ip_timers:
                print(f"Renewing timer for IP address {ip_to_renew}")
                # Restart the timer for the specified IP address
                self.ip_timers[ip_to_renew]['start_time'] = time.time()
            else:
                print(f"IP address {ip_to_renew} not found.")

        elif command == "RELEASE":
            print("Processing RELEASE command...")
            # Implement the logic for the RELEASE command here

        elif command == "STATUS":
            print("Processing STATUS command...")
            # Implement the logic for the STATUS command here

commands = ["ASK", "RENEW", "RELEASE", "STATUS"]
  

def process_command(command):
    if command == "ASK":
        print("Processing ASK command...")
        # Implement the logic for the ASK command here

    elif command == "RENEW":
        print("Processing RENEW command...")
        # Implement the logic for the RENEW command here

    elif command == "RELEASE":
        print("Processing RELEASE command...")
        # Implement the logic for the RELEASE command here

    elif command == "STATUS":
        print("Processing STATUS command...")
        # Implement the logic for the STATUS command here


            

# Create an instance of the TerminalInterface and start the interface
if __name__ == "__main__":
    print("Welcome to the DHCP server. Type one of the following commands:")
    print(", ".join(commands))

    while True:
        user_input = input("Enter command: ").strip().upper()

        if user_input in commands:
            process_command(user_input)
        else:
            print("Invalid command. Please enter one of the following commands:", ", ".join(commands))
