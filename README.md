## Grandstream-HT801 automatically provisioning example


## DHCP
In this example I use isc-dhcp-server software (apt install isc-dhcp-server) on ubuntu 18.04 server

To catch the grandstream HT801 SIP and pass TFTP server ip information in the DHCP request we use option 66
In the dhcpd.conf file:
<pre>
class "GRANDSTREAM HT801"{
  match if option vendor-class-identifier = "HT8XX dslforum.org";
  option tftp-server-name "40.40.40.40/ht801";
}
</pre>

## TFTP server
In this example I use Ubuntu 18.04 with "tftpd-hpa" software (apt install tftpd-hpa)
TFTP structure:
<pre>
tftpboot
 |
 --> frimware
 |    |
 |    --> ht810
 |          |
 |          --> ht801fw.bin
 |
 --> ht801
      |
      --> cfgcxxxxxxxxxxx.xml
</pre>

## Configuration script
The script is a simple python3 script that makes files based on tempalte with data from a database
In this example I connect to a postgres databases and select the data from  
Place the configuration script **build-ht801-configs.py** in <pre>/root/bin/</pre>

### Dependencies for the configuration script to work
<pre>
pip3 install -r requirements.txt
</pre>

## Database table and colums
In this example I use mySQL database on Ubuntu 18.04

Create table called **sipfriends**

In the table we need at least (**mac, gateway, tftp_server_ip, device_type, username, secret, admin_password**) colums

Colums explained:
**mac** - Used to validate client mac address

**gateway** - Point to the sip gateway

**tftp_server_ip** - Point to the tftp server

**device_type** - Specify the type/model of device

**username** - User telefone number

**secret** - User password for validating the user

**admin_password** - Password for remote access


## Conjobs (as root) - generates the configurations every 5 minutes
crontab -e 
<pre>*/5 * * * * /usr/bin/python3 /root/bin/build-ht801-configs.py</pre>
