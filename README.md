#Grandstream-HT801 automatically provisioning


#dependencies:
## psycopg2

## DHCP
In this example I use isc-dhcp-server on ubuntu 18.04 server

To catch the grandstream HT801 SIP and pass TFTP server ip information in the DHCP request we use option 66

## Conjobs
crontab -e 
<pre>*/5 * * * * /usr/bin/python3 /root/bin/build-ht801-configs.py</pre>
