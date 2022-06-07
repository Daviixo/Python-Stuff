import platform
import subprocess

def main(host, packets):

    print("You are currently using: " + str(platform.system))

    parameter = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', parameter, packets, host]
    response = subprocess.call(command)

    if response == 0:
        return True
    else:
        return False
        

if __name__ == "__main__":

    host = input("Type in the website you would like to ping:\n")
    packets = input("How many packets would you like to send?\n")

    main(host,packets)