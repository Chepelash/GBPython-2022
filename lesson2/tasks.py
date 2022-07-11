def task1():
    pass


def task2():
    pass


def main():
    task_list = [task1, task2]
    for task in task_list:
        print(f"{task.__name__}...")
        task()
        print("Done")


if __name__ == "__main__":
    main()
