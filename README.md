## NodeCheck API Test Script

The following script has been created so that API users can check/test our API service immediately once they have signed up to our API service.

### How to obtain the script?

Download the script using curl (you may need to install the curl package first):

```
curl -O https://raw.githubusercontent.com/nodecheck/api-scripts/master/api.sh
```

once downloaded, the script can then be moved to a more convenient location:

```
mv api.sh /usr/local/bin/
chmod +x api.sh
```

### How to configure the script?

First you will need an API key.  Please contact one of the NodeCheck team to obtain access to our API via our Discord (link below).
Edit the script and change:

```
APIKEY=your-api-key-here
```

replace ```your-api-key-here``` with the API key obtained from us.

### How to run the script?

Once downloaded, and the script is executable, the script can be ran as follows:

```
api.sh
```
or if you did not put it in your search PATH, then the script needs to be invoked using one of the examples below, like this:

```
./api.sh
/path/to/api.sh
```

without any additional parameters a help screen will appear providing you with instructions on which commands are available for use with the test script.  The script also depends on jq being installed, and if jq is unavailable within your PATH it will ask you to download and install appropriately.  The script also provides a link to the official site for jq.  Alternatively, search and install jq prior to running the script.

### What commands are available?

This script is a test script, and so may not include all of the API commands available.  To find out what commands are available, run the script as explained above without parameters:

```
api.sh
```

or if not in your search path, then:

```
./api.sh
/path/to/api.sh
```

at present the command returns the following:

```
You need to provide an API command to run this script.
Examples:

./api.sh <main-command> <parameters>

Display available coins on our site:	./api.sh ticker
Display coinstats:			./api.sh coinstats <ticker>
Display apistats:			./api.sh apistats

Add MN to monitor:			./api.sh add <ticker> <payee> <txid>
Check MN status:			./api.sh status <payee> <txid>
Delete monitored MN:			./api.sh delete <payee> <txid>
```

### How do I uninstall the script?

Very simple.  Just delete the script that you downloaded from your system, so that it no longer exists on your server.

### Help and Assistance?

* Check our API page - https://nodecheck.io/site/api
* Support on our Discord - https://discordapp.com/invite/3VV5GkG

### Disclaimer

NodeCheck will not be held responsible for misuse of this script or any adverse affects.  The script is provided as-is, and works perfectly fine when being utilised in the correct manner intended when following the instructions correctly.  If you are unsure, please contact us for assistance.
