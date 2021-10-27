from concurrent.futures import ThreadPoolExecutor, as_completed
from my_devices import all_devices
from my_functions import ssh_command2
from datetime import datetime

start_time = datetime.now()
thread_list = []
pool = ThreadPoolExecutor(2)

for device in all_devices:
    thread = pool.submit(ssh_command2, device)
    thread_list.append(thread)

# Return results from thread as soon as they are completed
as_completed(thread_list)

for thread in thread_list:
    print(thread.result())

print(f"Total time to execute {str(datetime.now() - start_time)}")
