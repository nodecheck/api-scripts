#!/usr/bin/env python3
#
##################################
# NodeCheck python3 API script   #
# Copyright: 2019 - NodeCheck.io #
# Version: 1.1                   #
##################################

# Import required python stuff
from sys import argv
from pkgutil import find_loader

# Set API key and get command passed with script
apikey = "ZTmRw99r76TtHDxeEZvGwht3PB9khSrs"

# Check if apikey has been configured or not
if apikey == "":
    print("You haven't edited the script to set \"apikey\" value")
    exit(1)

if find_loader("requests"):
    import requests
else:
    print("Error: python3-requests is not installed!")
    print("Please install if you wish to use this script.")
    exit(1)

if find_loader("simplejson"):
    import simplejson as json
else:
    print("Error: python3-simplejson is not installed!")
    print("Please install if you wish to use this script.")
    exit(1)

# Check what commands passed and set variables accordingly. Mandatory is only
# first field, rest are optional depending on command being used. Print error,
# help if data provided is not how it should be
program_name = argv[0]
results = None

# Define functions
def apiconnect(cmdmain, subcmd1=None, subcmd2=None, subcmd3=None):
    headers = {'Content-type': 'application/json', 'User-Agent': 'NodeCheck API Script'}
    url = "https://nodecheck.io/api/"
    url += cmdmain
    if subcmd1 is None:
        data = {'access-token': apikey}
    elif subcmd2 is None:
        data = {'access-token': apikey, 'ticker': subcmd1}
    elif subcmd3 is None:
        data = {'access-token': apikey, 'payee': subcmd1, 'txid': subcmd2}
    else:
        data = {'access-token': apikey, 'ticker': subcmd1, 'payee': subcmd2, 'txid': subcmd3}
    returndata = requests.post(url, data=json.dumps(data), headers=headers)
    parsed = json.loads(returndata.text)
    return parsed

if len(argv) > 1:
    apicmd = argv[1]
    # Check what command was passed and check if additional parameters have
    # also been passed along with it, if none or wrong parameters then print
    # error/help message
    if apicmd == "ticker" or apicmd == "apistats":
        results = apiconnect(apicmd)
    elif apicmd == "coinstats":
        if len(argv) > 2:
            results = apiconnect(apicmd, argv[2])
        else:
            print("Additional parameter required!")
            print("Eg: " + program_name + " coinstats dash")
            exit(1)
    elif apicmd == "status" or apicmd == "delete":
        if len(argv) > 3:
            results = apiconnect(apicmd, argv[2], argv[3])
        else:
            print("Additional parameters required!")
            print("Eg: " + program_name + " status <payee> <txid>")
            exit(1)
    elif apicmd == "add":
        if len(argv) > 4:
            results = apiconnect(apicmd, argv[2], argv[3], argv[4])
        else:
            print("Additional parameters required!")
            print("Eg: " + program_name + " add <ticker> <payee> <txid>")
            exit()
    else:
        print("Incorrect parameter provided!")
        print("Please use one of: ticker, coinstats, apistats, add, status, delete")
        exit(1)
    if apicmd == "ticker":
        print(json.dumps(results, indent=2, sort_keys=True))
    else:
        print(json.dumps(results, indent=2))
else:
    print("An API command is required.")
    print("Please use one of: apistats, coinstats, ticker, add, status, delete")
