#!/bin/bash
echo "Starting the application..."

# Remove self
rm -f /entrypoint.sh

export SECRET=$(python -c "import secrets; print(secrets.randbelow(10**16))" | tr -d '\n')

sed -i "s/REDACTED/$SECRET/g" /home/IAtinga/IAtinga/config.py

export SECRET_PATH=$(uuidgen)
mkdir -p /root/$SECRET_PATH && mv /root/flag.txt /root/$SECRET_PATH/flag.txt

# Start supervisord and services
/usr/bin/supervisord -c /etc/supervisord.conf
