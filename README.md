## NodeCheck API Test Script

The following script has been created so that API users can check/test our API service immediately once they have signed up to our API service.

# How to obtain the script?

Download the script using curl (you may need to install the curl package first):

```
curl -O https://raw.githubusercontent.com/nodecheck/api-scripts/master/api.sh
```

once downloaded, the script can then be moved to a more convenient location:

```
mv api.sh /usr/local/bin/
chmod +x api.sh
```

# How to run the script?

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

# What commands are available?

This script is a test script, and so covers only some basic functionality of our API.  It's not provided with all the API commands that we offer.  The commands the script will return via our API service are:

- ticker - this command lists all of the coins on our site (full name and ticker)
- coinstats - this command with the ticker for the coin of your choice will return the statistics from our platform for said coin.
- apistats - this command provides information relating to how many API calls you have made, and what your limit is.

### How do I uninstall the script?

Very simple.  First edit the crontab and remove the line that was added during installation.  Second, delete the script that you downloaded from your system, so that it no longer exists on your node.

### Help and Assistance?

* Check our FAQ - https://nodecheck.io/site/faq
* Support on our Discord - https://discordapp.com/invite/3VV5GkG

### Disclaimer

NodeCheck will not be held responsible for misuse of this script or any adverse affects.  The script is provided as-is, and works perfectly fine when being utilised in the correct manner intended when following the instructions correctly.  If you are unsure, please contact us for assistance.
