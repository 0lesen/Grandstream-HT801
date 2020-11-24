##Grandstream-HT801 automatically provisioning example==


##dependencies:
### psycopg2

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
Place the configuration script "build-ht801-configs.py" in <pre>/root/bin/</pre>

## Conjobs (as root) - generates the configurations every 5 minutes
crontab -e 
<pre>*/5 * * * * /usr/bin/python3 /root/bin/build-ht801-configs.py</pre>
