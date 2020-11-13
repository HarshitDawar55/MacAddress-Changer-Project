import optparse
import re
import subprocess


def MacChanger(interface, MA):
    print("[+] Changing the MacAddress of the Interface {} to {}".format(interface, MA))
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", MA])
    subprocess.call(["ifconfig", interface, "up"])


def get_present_MacAddress(interface):
    ifconfig_output = subprocess.check_output(["ifconfig", values.interface])
    mac_addresses = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_output)

    if mac_addresses:
        print("Current Mac Address: {}".format(mac_addresses[0]))
    else:
        print("[-] Sorry! Could not found MAC Address!")


# Initializing the Parser!
parser = optparse.OptionParser()

# Initializing the arguments to parse!
parser.add_option("--interface",
                  "-i",
                  dest="interface",
                  help="Enter the Interface for which the Mac Address has to be changed")

parser.add_option("--mac_Address",
                  "-m",
                  dest="macAddress",
                  help="Enter the New Mac Address to be assigned to the Interface")

# Parsing the Command Line Arguments!
values, _ = parser.parse_args()

# Conditions to validate the values while running the script!
if not values.interface:
    parser.error("Please Enter the Interface!")
if not values.macAddress:
    parser.error("Please Enter the New MacAddress!")

# Calling the Function to Change the Mac Address
MacChanger(values.interface, values.macAddress)

# Checking the result that whether the output get changed or not!
