Karely Rodriguez 
Programming Assignment 1 

Virtual Machines:
VM1 - Virtual Box Ubuntu 
VM2 - Chameleon Ubuntu
VM3 - Chameleon Ubuntu

HOW TO RUN PROGRAM 

--VM2 Terminal 1 commands--
rm -fr /tmp/zookeeper/ /tmp/kafka* 
bin/zookeeper-server-start.sh config/zookeeper.properties

--VM2 Terminal 2 commands--
bin/kafka-server-start.sh config/server.properties

--VM3 1 Terminal 1 commands--
sudo systemctl start  couchdb.service
rm -fr /tmp/zookeeper/ /tmp/kafka*  
bin/kafka-server-start.sh config/server.properties

--VM2 Terminal 3 commands--
python3 consumer.py

--VM1 Terminal 1 commands -- program prompts user to enter a topic number 1 refers to weather data--
python3 producer.py
1
--VM1 Terminal 2 commands -- 2 refers to air quality data--
python3 producer.py
2
--VM1 Terminal 3 commands -- 3 refers to covid data--
python3 producer.py
3

--see data dump on web brower--
http://127.0.0.1:5984/_utils/


