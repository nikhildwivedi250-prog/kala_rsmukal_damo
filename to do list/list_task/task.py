def to_do_list():
    tasks = []

    while True:
        print("1. add task")
        print("2. remove task")
        print("3. show tasks")
        print("4. quit")
        choice = input("enter your choice")

        if choice == "1":
            task = input("enter task: ")
            tasks.append(task)
        elif choice == "2":
            task = input("enter task to remove")
            if task is tasks:
                tasks.remove(task)
            else:
                print("task not find")
        elif choice == "3":
            print("tasks: ")
            for task in tasks:
                print("- " + task)
        elif choice == "4":
            "break"
        else:
            print("invailed choice")

to_do_list()

