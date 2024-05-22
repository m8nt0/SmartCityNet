#!/bin/bash

# Test if SSH port is open
if iptables -L | grep -q 'tcp dpt:ssh'; then
  echo "SSH rule is present"
else
  echo "SSH rule is missing"
fi

# Test if default DROP policy is set
if iptables -L INPUT -v -n | grep -q 'Chain INPUT (policy DROP)'; then
  echo "Default policy for INPUT is DROP"
else
  echo "Default policy for INPUT is not DROP"
fi
