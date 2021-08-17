#!/usr/bin/env python3
import shutil
import psutil
import socket
import os, sys
import emails

#Report an error if available disk space is lower than 20%
def check_disk_usage(disk="/"):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    if free < 20:
        return emails.generate_error_report("Error - Available disk space is less than 20%")

#Report an error if CPU usage is over 80%
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    if usage > 80:
        return emails.generate_error_report("Error - CPU usage is over 80%")

#Report an error if available memory is less than 500MB
def check_available_memory():
    memory = psutil.virtual_memory() #gets system memory stats (expressed in bytes)
    available_memory = memory.available / 1024**2 #convert bytes to MB
    if available_memory < 500:
        return emails.generate_error_report("Error - Available memory is less than 500MB")

#Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
def Local_Host_Check():
    localhost = socket.gethostbyname("localhost")
    if localhost != "127.0.0.1":
        return emails.generate_error_report("Error - localhost cannot be resolved to 127.0.0.1")
    
    
    
if __name__ == "__main__":
    check_disk_usage()
    check_cpu_usage()
    check_available_memory()
    Local_Host_Check()
