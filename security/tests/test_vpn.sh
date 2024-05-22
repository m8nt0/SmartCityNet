#!/bin/bash

# Test if OpenVPN server configuration file exists
if [ -f "/etc/openvpn/server.conf" ]; then
  echo "OpenVPN server configuration file exists"
else
  echo "OpenVPN server configuration file is missing"
fi

# Test if OpenVPN client configuration file exists
if [ -f "/etc/openvpn/client.conf" ]; then
  echo "OpenVPN client configuration file exists"
else
  echo "OpenVPN client configuration file is missing"
fi
