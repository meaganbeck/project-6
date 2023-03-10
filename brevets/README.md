Name: Meagan Beckstrand
Email: mbeckst2@uoregon.edu

This program takes in a singular input for brevet distance, and start time. These values are used to calculate the open and close time for various inputted control lengths.

Control location(km) 	Min Speed (km/hr)	Max Speed (km/hr)
0-200			15			34
200-400			15			32
400-600			15			30
600-1000		11.428			28
1000-13000		13.333			26

For the control location, each open and close time is calculated by adding the min/max speed for each bracket that it fills. A 350km control will fill the 0-200 bracket, which has a min time of 200/34 and a max time of 200/15, then add 150 km within the 200-400 bracket, or a min time of 150/32 and a max time of 150/15. This gives a total min of 10.57 hours and a max of 23.33 hours
