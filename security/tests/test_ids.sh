#!/bin/bash

# Test if Snort configuration file exists
if [ -f "/etc/snort/snort.conf" ]; then
  echo "Snort configuration file exists"
else
  echo "Snort configuration file is missing"
fi

# Test if Snort rules file exists
if [ -f "/etc/snort/rules/snort_rules.rules" ]; then
  echo "Snort rules file exists"
else
  echo "Snort rules file is missing"
fi
