# Core Service Exercise 
Please read the following instructions before starting to implement your exercise, you don't want to miss any important instruction.

# Usage
Run the following files separately for each exercise respectively using python3:
1. OutRain.py
2. OutOfDrives.py


### OutRain
Write a program that checks your location according to your IP, then checks the current weather at your location and prints the result in the following format: 
`The weather in <city>, <country> is XX degrees.`

* Degrees should be shown in Celsius.
* You can get the location according to the IP via this service: http://ipinfo.io/ 
* You can fetch the weather information for a given location via this service: https://openweathermap.org/current

Example output:

~~~
The weather in Haifa, IL is 26 degrees.
~~~

### OutOfDrives

Write a program that reads an input from the file `input.txt`, and prints the drive/s information of all those who are in an Offline state, in a human readable manner.  

In the input file, each line displays information for a single drive in an array. 
The information is given in a CSV format, where the second value is the state of the drive (Offline/Online).

Example output: 
~~~
Found (2) offline drives: 

name: SP4
	size: 4764771 MB
	free: 2333948 MB
	path: /dev/sdk
	log: 0 MB
	port: 5660
	guid: db53cc9f02524622005b30b0eb0947e3
	clusterUuid: -8650609094877646407--116798096584060989
	disks: /dev/sdk /dev/sdl /dev/sdm
	dare: 0
name: SP5
	size: 4764971 MB
	free: 3333948 MB
	path: /dev/sdz
	log: 122 MB
	port: 5660
	guid: db53cc9f02524622005b331231245151
	clusterUuid: -8650609094877646402--116798096584060981
	disks: /dev/sdr /dev/sdk /dev/sdx
	dare: 1
~~~
