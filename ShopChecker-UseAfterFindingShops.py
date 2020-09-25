import time
import webbrowser

filepath = 'taken.txt'

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print(line.strip())
       webbrowser.open(line.strip())
       line = fp.readline()
       cnt += 1
       time.sleep(0.1)#i like to spam control w and check them all out fast, maybe adding a bit more of a delay and checking them as they open might be for you
       
delete = input(f"Do you want me to clear the file {filepath} now that I've opened all the tabs?\nType yes to clear,otherwise just press enter and I'll close!\n>")
if delete.lower() == "yes":
    f = open(filepath, "w")
        
