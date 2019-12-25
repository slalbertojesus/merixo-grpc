#!/bin/bash

BOLD=$(tput bold)
CLEAR=$(tput sgr0)

echo -e "${BOLD}ROOT CA.key${CLEAR}"
openssl genrsa -aes256 -out Root.CA.key 4096

echo -e "${BOLD}ROOT CA.pem${CLEAR}"
openssl req -x509 -new -nodes -key Root.CA.key -sha256 -days 1825 -out Root.CA.pem

echo -e "${BOLD}Server.key${CLEAR}"
openssl genrsa -out server.key 4096

echo -e "${BOLD}Server.csr${CLEAR}"
openssl req -new -key server.key -out server.csr

echo -e "${BOLD}Server cert this one fails${CLEAR}"
openssl x509 -req -in server.csr -CA Root.CA.pem -CAkey Root.CA.key -CAcreateserial -out server.crt -days 1825 -sha256

echo -e "${BOLD}Client.key${CLEAR}"
openssl genrsa -out client.key 4096

echo -e "${BOLD}Client.scr${CLEAR}"
openssl req -new -key client.key -out client.csr

echo -e "${BOLD}Client.crt${CLEAR}"
openssl x509 -req -in client.csr -CA Root.CA.pem -CAkey Root.CA.key -CAcreateserial -out client.crt -days 1825 -sha256

	echo "Done!"
