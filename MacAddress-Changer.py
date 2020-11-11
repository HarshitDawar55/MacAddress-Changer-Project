import optparse

# Initializing the Parser
parser = optparse.OptionParser()
parser.add_option("--interface",
                  "-i",
                  dest = "interface",
                  help = "Enter the Interface for which the Mac Address has to be changed")

parser.add_option("--mac_Address",
                  "-m",
                  dest = "macAddress",
                  help = "Enter the New Mac Address to be assigned to the Interface")

values, variables = parser.parse_args()



