#!/usr/bin/python3
import psycopg2
import psycopg2.extras
from string import Template
import os
import glob
import syslog
import sys

# Database information
db_user = "admin"
db_password = "password"
db_database = "sipfriends"
db_host = "10.10.10.10"
db_port = "5432"

# TFTP paths
tftp_path = '/var/lib/tftpboot/'
current_files = '/var/lib/tftpboot/ht801/*'
files = glob.glob(current_files)

# Remove old configuration files
for f in files:
    os.remove(f)

try:
   connection = psycopg2.connect(user=db_user, password=db_password, host=db_host, port=db_port, database=db_database)
   cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
   postgres_select_query = """ SELECT * FROM sipfriends WHERE device_type = 'HT801'"""
   cursor.execute(postgres_select_query)
   res = cursor.fetchall()

   for user in res:
       template_file_path = 'root/bin/ht801_template.txt'
       template_file = open(template_file_path, 'r')
       src = Template( template_file.read() )
       b={ 'mac':user["mac"], 'gateway':user["gateway"], 'tftp_server':user["tftp_server"], 'username':user["username"], 'secret':user["secret"], 'admin_password':user["admin_password"]}
       result = src.substitute(b)
       config_file_path = tftp_path + 'ht801/' + 'cfg' + user["mac"] + '.xml'
       config_file = open(config_file_path,'w+')
       config_file.write(result)
       config_file.close()
       print ('Generating configuration for cpe type:', user["device_type"], '- mac:', user["mac"], '- number:', user["username"])

except Exception as error :
    print("ERROR:", error)
    syslog.openlog()
    syslog.syslog("ERROR: %s" % error)
    syslog.closelog()
    sys.exit(0)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
