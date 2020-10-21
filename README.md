# Description of wifi_sensor

ROS package to use the RSSI of a wifi card as a sensor. 
Measurements are pulished to the `/wifi` topic.


## Notes
You must make the permissions on the file wifi_sensor.py executable.

You have to do these things so that you can use the wifi as a sensor in ros.

1. mkdir wifi_ws
2. cd mkdir wifi_ws
3. mkdir src
4. cd src
5. git clone https://github.com/bryantaoli/wifi_sensor
6. cd ..
7. catkin_make
8. sudo su
9. pip install pywifi
10. In another terminal, you should start a roscore.
11. rosrun wifi_sensor wifi_sensor.py

