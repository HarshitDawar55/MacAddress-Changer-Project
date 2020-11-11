import optparse

# Initializing the Parser!
parser = optparse.OptionParser()

# Initializing the arguments to parse!
parser.add_option("--interface",
                  "-i",
                  dest = "interface",
                  help = "Enter the Interface for which the Mac Address has to be changed")

parser.add_option("--mac_Address",
                  "-m",
                  dest = "macAddress",
                  help = "Enter the New Mac Address to be assigned to the Interface")

# Parsing the Command Line Arguments!
values, _ = parser.parse_args()

# Conditions to validate the values while running the script!
if not values.interface:
    parser.error("Please Enter the Interface!")
if not values.macAddress:
    parser.error("Please Enter the New MacAddress!")

print("No Error Now!")


