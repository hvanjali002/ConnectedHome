 import serial 
 import time 
 import requests 
 import os 
 
 ser = serial.Serial('/dev/rfcomm0', 2000000, timeout=0) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens. 
 ser.flushInput() 
 ser.flushOutput() 
 while True: 
 time.sleep(8) 
 ser.flushInput() 
 time.sleep(2) 
 try: 
 data_raw = ser.readline() #read one line of raw data 
 data_raw = data_raw.strip() #To remove \n\r from raw data 
 print data_raw 
 #continue 
 
 raw_list = data_raw.split(',') 
 d = dict(s.split(':') for s in raw_list) 
 if d['ch'] and d['ts'] and d['ls'] and d['ms']: 
 #temp = int(int(d['ts'])/100) 
 temp = int(d['ts']) 
 light = int(d['ls']) 
 motion = int(d['ms']) 
 board = str(d['ch']) 
 
 if motion == 1: 
 fpath = '/home/pi/home_auto/' 
 fname = 'cam.py' 
 
 #Call the script which takes the picture 
 cmd = "python " + fpath + fname 
 try: 
 os.system(cmd) 
 except: 
 print 'problem with cam.py script' 
 
 #print temp 
 url = 'http://homeiot007.000webhostapp.com/monitor/' 
 payload = {'ch': board,'ts': temp, 'ls': light, 'ms': motion} 
 
 try: 
 r = requests.get(url, params=payload) 
 print r.status_code 
 except: 
 print 'Problem uploading data' 
 else: 
 continue 
 
 except: 
 pass 

