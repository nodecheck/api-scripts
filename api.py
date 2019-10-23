#!/usr/bin/env python3
#
##################################
# NodeCheck python3 API script   #
# Copyright: 2019 - NodeCheck.io #
# Version: 1.0                   #
##################################

# Import required python stuff
from sys import argv
import requests
import simplejson as json

# Set API key and get command passed with script
apikey="your-api-key-here"

# DO NOT EDIT BELOW THIS LINE

# Check if apikey has been configured or not
if apikey == "your-api-key-here":
    print("You haven't added your API key to this script!")
    print("Please edit the beginning of this script:\n")
    print("apikey=your-api-key-here")
    exit(1)

# Check what commands passed and set variables accordingly. Mandatory is only
# first field, rest are optional depending on command being used. Print error,
# help if data provided is not how it should be
program_name=argv[0]
apicmd=None
headers = {'Content-type': 'application/json', 'User-Agent': 'NodeCheck API Script'}
url = "https://nodecheck.io/api/"

if len(argv) > 1:
    apicmd=argv[1]
    # Check what command was passed and check if additional parameters have
    # also been passed along with it, if none or wrong parameters then print
    # error/help message
    if apicmd == "ticker" or apicmd == "apistats":
        url += apicmd
        data = {'access-token': apikey}
        results = requests.post(url, data=json.dumps(data), headers=headers)
    elif apicmd == "coinstats":
        if len(argv) > 2:
            apisubcmd1=argv[2]
            url += apicmd
            data = {'access-token': apikey, 'ticker': apisubcmd1}
            results = requests.post(url, data=json.dumps(data), headers=headers)
        else:
            print("Additional parameter required!")
            print("Eg: " + program_name + " coinstats dash")
            exit(1)
    elif apicmd == "status" or apicmd == "delete":
        if len(argv) > 3:
            apisubcmd1=argv[2]
            apisubcmd2=argv[3]
            url += apicmd
            data = {'access-token': apikey, 'payee': apisubcmd1, 'txid': apisubcmd2}
            results = requests.post(url, data=json.dumps(data), headers=headers)
        else:
            print("Additional parameters required!")
            print("Eg: " + program_name + " status <payee> <txid>")
            exit(1)
    elif apicmd == "add":
        if len(argv) > 4:
            apisubcmd1=argv[2]
            apisubcmd2=argv[3]
            apisubcmd3=argv[4]
            url += apicmd
            data = {'access-token': apikey, 'ticker': apisubcmd1, 'payee': apisubcmd2, 'txid': apisubcmd3}
            results = requests.post(url, data=json.dumps(data), headers=headers)
        else:
            print("Additional parameters required!")
            print("Eg: " + program_name + " add <ticker> <payee> <txid>")
            exit()
    else:
            print("Incorrect parameter provided!")
            print("Please use one of: ticker, coinstats, apistats, add, status, delete")
            exit(1)
    if apicmd == "ticker":
        parsed = json.loads(results.text)
        print(json.dumps(parsed, indent=2, sort_keys=True))
    else:
        parsed = json.loads(results.text)
        print(json.dumps(parsed, indent=2))
else:
    print("An API command is required.")
    print("Please use one of: apistats, coinstats, ticker, add, status, delete")
