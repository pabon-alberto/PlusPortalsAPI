import time
import plusportals as pp

st_time = time.time() # Start tracking time for execution
client = pp.Client(False, "CCND", 'email', 11700, 'password')
client.printGrades(4)
end_time = time.time()

elapsed_time = end_time - st_time # Program is finished, stop tracking time.
round_elap = round(elapsed_time, 5)
print('\nExecution time:', round_elap, 'seconds\n') 