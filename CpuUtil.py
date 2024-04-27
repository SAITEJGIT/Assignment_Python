# Need to import psutil module to monitor cpu parameters
import psutil
# creating an infinite loop
try:
    while True:
# cpu_percent is a preeifned method that returns the cpu usage and upon giving interval it denotes the freequency of updates.
            CPUpercentage = psutil.cpu_percent(interval=1)
            print(f"Monitoring Cpu Usage......{CPUpercentage}%")
            if(85 < CPUpercentage < 90):
                print("Alert! CPU usage exceeds threshold: 85%")
            elif(CPUpercentage>90):
                    print("Alert! CPU usage exceeds threshold: 90%")
# this except block is used to interrupt the above process, so if a ctrl+c is sent from the keyboard below piece of code gets executed
except KeyboardInterrupt:
      print("Exiting.....")

