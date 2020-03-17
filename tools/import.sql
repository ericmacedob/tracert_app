LOAD DATA INFILE 'testing.csv'
INTO TABLE tracert_app
fields terminated by ","
lines terminated by "\n"
(hostname,longitude,rtt,hop_num,latitude,ip_address);