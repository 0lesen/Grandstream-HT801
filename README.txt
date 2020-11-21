dependencies:
psycopg2

How to run crontab
Run crontab as root!:
crontab -e 
*/5 * * * * /usr/bin/python3 /root/bin/build-ht801-configs.py
