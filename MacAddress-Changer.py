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
    return mac_addresses


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

# Fetching the current Mac Address!
present_MacAddress = get_present_MacAddress(values.interface)
if present_MacAddress:
    print("Current Mac Address: {}".format(present_MacAddress[0]))
else:
    print("[-] Sorry! Could not found MAC Address!")

# Calling the Function to Change the Mac Address
try:
    MacChanger(values.interface, values.macAddress)
except Exception:
    print(Exception)
finally:
    # Checking the result that whether the output get changed or not!
    present_MacAddress = get_present_MacAddress(values.interface)
    if present_MacAddress:
        print("New Mac Address: {}".format(present_MacAddress[0]))
    else:
        print("[-] Sorry! Can not change Mac Address!")
