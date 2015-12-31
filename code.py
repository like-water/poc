import subprocess
'''
url=raw_input("input the url :")
commond_injection="yes|sqlmap -u "+url
p1=subprocess.Popen(commond_injection,shell=True,stdout=subprocess.PIPE)
(output,err)=p1.communicate()

print "*** Running sql -u "+url+" *** \n",output
'''
commond_check="dpkg -s sqlmap "
p2=subprocess.Popen(commond_check,shell=True,stdout=subprocess.PIPE)
(output,err)=p2.communicate()

f=open("status.txt",'w')
f.writelines(output)

f.close()
