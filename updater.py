import os, time, distro

update_freq = 604800

if distro != "Ubuntu" :  ## If not Ubuntu, this could technically work for any Debian based system, but I just hardcoded Ubuntu because it is the distro I use for my servers
    exit()

try :
    log_message = time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime() + ": Running `sudo apt update`.\n") 
    os.system("sudo apt update")
    log_message += time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime() + ": Ran `sudo apt update` successfully.\n") 
except Exception as error :
    log_message += time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime() + f": Ran `sudo apt update` with error message {error}.\n") 

try : 
    log_message += time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime() + ": Running `sudo apt upgrade -y`.\n") 
    os.system("sudo apt upgrade -y")
    log_message += time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime() + ": Ran `sudo apt upgrade -y` successfully.\n") 
except Exception as error : 
    log_message += time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime() + f": Ran `sudo apt upgrade -y` with error message {error}.\n") 

try :
    with open("logs.txt", 'a') as logfile :
        logfile.write(log_message)
except : 
    with open("logs.txt", 'w') as logfile :
        logfile.write(log_message)

time.sleep(update_freq) ## This command will run every week, but you can change the value of the variable to change the update frequency. And this is very jank