import platform
import socket
import os
import sys
print(f"Machine type: " , platform.machine())
print(f"CPU architecture: ", platform.architecture())

socket.setdefaulttimeout(50)
print(f"CPU Architecture: " , {socket.getdefaulttimeout()})
print(f"OS Type: " , {os.name})
print(f"OS system: " , {platform.system()})


print(f"Current PID: {os.getpid()}" )

file_name = "fdpractice.txt"
file_handler = os.open(file_name,os.O_RDWR | os.O_CREAT)
print(f"[PID: {os.getpid()}] Opened the file handle: {file_handler}\n")
file_object_TextIO = os.fdopen(file_handler, "w+")
file_object_TextIO.write("Some string to write in the file")
file_object_TextIO.flush()

print(f"\n\n[PID: {os.getpid()}] Forking Now...\n")
pid = os.fork()
#pid = 0

if pid == 0:
    print(f"[Child PID: {os.getpid()}], [Parent PID:  {os.getppid()}]\n")
    os.lseek(file_handler, 0 ,0)
    print(f"[Child PID: {os.getpid()}], [File Content:  {os.read(file_handler, 100).decode()}]\n")
    os.close(file_handler)
    sys.exit(0)
else:
    print(f"[Parent PID: {os.getpid()}], [Child PID:  {pid}]\n")
    print("Wait for child!!")
    os.wait()
    print("Child finished!!")

    file_object_TextIO.close()

sys.exit(0)