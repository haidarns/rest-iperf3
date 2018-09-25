import subprocess, time

targethost = '127.0.0.1'
p = subprocess.Popen(['echo', 'hello'])

def changeBW(newBW):
   global p
   p.kill()
   p = subprocess.Popen(['iperf3', '-c', targethost, '-u', '-b', newBW, '-t', '100'], stdout=subprocess.PIPE)

changeBW('5M')
time.sleep(5)

time1 = time.time()
changeBW('7M')
print time.time()-time1

time.sleep(5)
p.kill()
