# marketo_assessment

### In This Subnet

1. Requires Python module "netaddr" to be installed<br>
    a. Use "pip install netaddr"<br>
2. Use python subnet.py --input_file=<input_file> --output_file=<output_file><br>
    a. Where input_file is the location of a file containing comma separated <br>
       hex IP address and subnet in CIDR notation, see below for example<br>
    b. Where output_file will eventually contain the IP address, subnet, and<br> 
       whether the IP address is in the given subnet<br>

input_file.txt
-----------------
0x62D2ED4B,98.210.237.192/26<br>
0x62d2edc1,98.210.237.192/26<br>

### Change of Phone Number

1. Run using "phone_number.sh <path to html files>"