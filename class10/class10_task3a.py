from concurrent.futures import ThreadPoolExecutor, wait
from my_devices import all_devices
from my_functions import ssh_command2
from datetime import datetime

def main():
    start_time = datetime.now()
    max_threads = 4
    future_list = []

    pool = ThreadPoolExecutor(max_workers=max_threads)

    for device in all_devices:
        thread = pool.submit(ssh_command2, device)
        future_list.append(thread)

    jobs = wait(future_list)

    print(jobs)

    for output in future_list:
        print(f"### Show Version for {output.result()}")

    print(f"Total time to execute is {str(datetime.now() - start_time)}")


if __name__ == "__main__":
    main()
