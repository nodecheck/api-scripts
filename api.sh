#!/bin/bash
#

#######################################
# Place to put your API key           #
#######################################
APIKEY=your-api-key-here

################################
# API command that we will run #
################################
APICMD=$1

#######################################################
# Command to check if jq is installed and in the path #
# for example: /usr/bin or /usr/local/bin             #
#######################################################
JQCMD=`which jq`

# Check if JQ is installed, if not display message
if [ -z "$JQCMD" ]
then
  echo ""
  echo "JQ is a requirement for this script to run successfully."
  echo "Download JQ here: https://stedolan.github.io/jq/download/"
  echo ""
  echo "Please follow instructions from the above webpage link to ensure jq"
  echo "is installed and executable. It can be installed using your distros"
  echo "package manager, or by manual install."
  echo ""
  echo "Once downloaded, please make sure jq is in /usr/bin or /usr/local/bin"
  echo "This message will disappear once JQ is correctly installed and in one"
  echo "of the above locations."
  echo ""
else
  # Check if API command was passed to the script, if not, give instructions
  if [ -z "$APICMD" ]
  then
    echo ""
    echo "You need to provide an API command to run this script."
    echo "Examples:"
    echo ""
    echo "Display available coins on our site:"
    echo "		./api.sh ticker"
    echo "Display coinstats (requires second parameter - ticker of coin):"
    echo "		./api.sh coinstats dash"
    echo "Display apistats - used API calls and API limit:"
    echo "		./api.sh apistats"
    echo ""
  else
    if [ $APICMD == "ticker" ]
    then
      curl -s -H "Content-Type:application/json" -d "{\"access-token\":\"$APIKEY\"}" https://nodecheck.io/api/$APICMD | $JQCMD
    elif [ $APICMD == "coinstats" ]
    then
      TICKER=$2
      curl -s -H "Content-Type:application/json" -d "{\"access-token\":\"$APIKEY\",\"ticker\":\"$TICKER\"}" https://nodecheck.io/api/$APICMD | $JQCMD
    elif [ $APICMD == "apistats" ]
    then
      curl -s -H "Content-Type:application/json" -d "{\"access-token\":\"$APIKEY\"}" https://nodecheck.io/api/$APICMD | $JQCMD
    fi
  fi
fi
