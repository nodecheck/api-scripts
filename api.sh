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
  if [ $APIKEY == "your-api-key-here" ]
  then
    echo ""
    echo "You haven't added your API key to this script!"
    echo "Please edit the beginning of this script:"
    echo ""
    echo "APIKEY=your-api-key-here"
    echo ""
  else
    if [ -z "$APICMD" ]
    then
      echo ""
      echo "You need to provide an API command to run this script."
      echo "Examples:"
      echo ""
      echo "./api.sh <main-command> <parameters>"
      echo ""
      echo "Display available coins on our site:	./api.sh ticker"
      echo "Display coinstats:			./api.sh coinstats <ticker>"
      echo "Display apistats:			./api.sh apistats"
      echo ""
      echo "Add MN to monitor:			./api.sh add <ticker> <payee> <txid>"
      echo "Check MN status:			./api.sh status <payee> <txid>"
      echo "Delete monitored MN:			./api.sh delete <payee> <txid>"
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
      elif [ $APICMD == "add" ]
      then
        TICKER=$2
        PAYEE=$3
        TXID=$4
        curl -s -H "Content-Type:application/json" -d "{\"access-token\":\"$APIKEY\",\"ticker\":\"$TICKER\",\"payee\":\"$PAYEE\",\"txid\":\"$TXID\"}" https://nodecheck.io/api/$APICMD | $JQCMD
      elif [ $APICMD == "status" ]
      then
        PAYEE=$2
        TXID=$3
        curl -s -H "Content-Type:application/json" -d "{\"access-token\":\"$APIKEY\",\"payee\":\"$PAYEE\",\"txid\":\"$TXID\"}" https://nodecheck.io/api/$APICMD | $JQCMD
      elif [ $APICMD == "delete" ]
      then
        PAYEE=$2
        TXID=$3
        curl -s -H "Content-Type:application/json" -d "{\"access-token\":\"$APIKEY\",\"payee\":\"$PAYEE\",\"txid\":\"$TXID\"}" https://nodecheck.io/api/$APICMD | $JQCMD
      fi
    fi
  fi
fi
