import threading
import my_functions
from datetime import datetime
from my_devices import all_devices



if __name__ == "__main__":
    start_time = datetime.now()

    for device in all_devices:
        args = device.pop("optional_args")
        my_thread = threading.Thread(target=my_functions.ssh_command, args=(device,"show version"))
        my_thread.start()

        main_thread = threading.currentThread()

        for some_thread in threading.enumerate():
            if some_thread != main_thread:
                print(some_thread)
                some_thread.join()

    print(f"\n#### Elapsed time: {str(datetime.now() - start_time)}")

