from re import sub                                                  # for regex
from requests import get                                            # for GET request


# Declare the Variables
IOU = []                                                                    # The list that will contain all the mac addresses and vendors
URL = 'https://gitlab.com/wireshark/wireshark/-/raw/master/manuf'           # This is the Wireshark OUI repository that they download them from IEEE

# Generate an IOU list
def VendorList(URL):
    # GET request, convert the data to UTF-8 and split the lines
    GetRequest = get(URL).content.decode('utf-8').splitlines(True)
    # loop to parse the output
    atlast = False
    for line in GetRequest:
        if line.startswith('00:00:01'):
            atlast = True
        if atlast:
            clean = line.strip('\n').split('\t')
            print(clean[0], clean[1])
            IOU.append(clean[0:2])
    return IOU

# A class that will allow us to match a MAC address to a Vendor
class VendorLookup():
    """
    This script is going to generate the OUI list from:
    https://gitlab.com/wireshark/wireshark/-/raw/master/manuf
    
    Everything runs on RAM there is no call on an API.
    """  
    def __init__(self, macaddr):
        self.macaddr = macaddr

    # Match MAC to a Vendor
    def Vendor(self):
        try:
            RemoveSymbols = sub('\W', '', self.macaddr[0:8].upper())
            for i in range(len(RemoveSymbols)):
                if re.match(r'[g-zG-Z]', RemoveSymbols[i]):
                    Company = 'Non HEX MAC'
            CleanMac = RemoveSymbols[0] + RemoveSymbols[1] + ':' + RemoveSymbols[2] + RemoveSymbols[3] + ':' + RemoveSymbols[4] + RemoveSymbols[5]
            for line in IOU:
                if line[0].startswith(CleanMac):
                    Company = line[1]
            return Company
        except Exception as UnboundLocalError:
            Company = 'N/A'
        return Company

# If not imported
if __name__ == '__main__':
    macaddr = input('Enter the MAC Address: ')
    IOU = VendorList(URL)
    vendor = VendorLookup(macaddr)
    print(vendor.Vendor())
