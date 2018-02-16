 import os 
 import ftplib 
 import datetime 
 
 ts = datetime.datetime.now().replace(microsecond=0).isoformat() 
 ts = ts.replace(':','-') 
 fname = 'D' + str(ts) + '.jpg' 
 #print fname 
 fpath = '/home/pi/home_auto/' 
 
 #Take a picture 
 cmd = "raspistill -vf -w 640 -h 480 -q 75 -o " + fpath + fname 
 try: 
 os.system(cmd) 
 except: 
 print 'problem taking pic' 
 
 #Upload picture to webserver 
 session = ftplib.FTP('files.000webhost.com','homeiot007','matrix123') 
 
 try: 
 x = session.login() 
 
 except Exception, e: 
 if '530' in str(e): 
 pass 
 else: 
 print str(e) 
 
 #print session.getwelcome() 
 session.cwd('/public_html/wp-content/uploads/motion/capture/') 
 #print session.retrlines('LIST') 
 #fpath = "/home/pi/home_auto/" 
 #fname = "pic.jpg" 
 f_loc = fpath + fname 
 try: 
 session.storbinary("STOR " + fname, open(f_loc, "rb"), 1024) 
 except Exception, e: 
 print "upload failed ", str(e) 
 print 'picture upload succesful' 
 session.quit() 

