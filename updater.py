import os, time, distro

update_freq = 604800

os.system("export DEBIAN_FRONTEND=noninteractive") ## Suppresses the urgue to take up the screen and mess up my program
while True :
    log_message = ""
    try :
        log_message += str(time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime()) + ": Running `sudo apt update`.\n") 
        os.system("sudo apt update")
        log_message += str(time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime()) + ": Ran `sudo apt update` successfully.\n") 
    except Exception as error :
        log_message += str(time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime()) + f": Ran `sudo apt update` with error message {error}.\n") 

    try : 
        log_message += str(time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime()) + ": Running `sudo apt upgrade -y`.\n") 
        os.system("sudo apt upgrade -y")
        log_message += str(time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime()) + ": Ran `sudo apt upgrade -y` successfully.\n") 
    except Exception as error : 
        log_message += str(time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime()) + f": Ran `sudo apt upgrade -y` with error message {error}.\n") 

    try :
        with open("logs.txt", 'a') as logfile :
            logfile.write(log_message)
    except : 
        with open("logs.txt", 'w') as logfile :
            logfile.write(log_message)

    time.sleep(update_freq) ## This command will run every week, but you can change the value of the variable to change the update frequency. And this is very jank