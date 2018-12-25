import progressbar
import time
 
bar = progressbar.ProgressBar().start() 
 
for t in range(101):
    bar.update(t) 
    time.sleep(0.01)
bar.finish() 
print ("finished =)")