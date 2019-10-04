#!/usr/bin/python3
import sys
sys.path.append("H:\\apps\\Python27\\lib\\site-packages")
import cgi




print("Content-type: text/html\n")
print("<title>Result</title>")
print("<body><center>")



sqlip = open("website.txt","r")
a = sqlip.read()
sqlip.close()
print(a)
print('<script type="text/javascript"> ')
print("location.href =%s;"%a)
print('</script>')
print('</center></body>')
