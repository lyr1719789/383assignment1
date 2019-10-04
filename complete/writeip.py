a=input("my google sql ip:")
modified= open('ip.txt',"w")
modified.write(a)
modified.close()


b=input("my phpmyadmin site")
website= open('help/cgi-bin/website.txt',"w")
website.write("'"+b+"'")
website.close()
