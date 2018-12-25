import os
import subprocess
import time
import progressbar

print ("Start : %s" % time.ctime())


f = open ("bash.sh", "w")
f.write ("#! /bin/bash\nfor i in 1 2 3 4 5\ndo echo $i >> output.txt\ndone\ncat output.txt")
f.close()
os.chmod(r"bash.sh", 0o777)
subprocess.call (['./bash.sh'])

print("Удаляю файлы...")
bar = progressbar.ProgressBar().start()

os.remove("bash.sh")
t=50
bar.update(t)
time.sleep(3)
os.remove("output.txt")
t=90
bar.update(t)
time.sleep(3)
bar.finish()
print ("Выполнено : %s" % time.ctime())