class Task:
    def __init__(self, name = None, description = None):
        self.name = name
        self.description = description
    
    def __str__(self):
        return str(self.name) + ' ' + str(self.description)

class Program:
    def __init__(self): 
        self.task_list = []
        try:
            with open('task3.txt', 'r') as f:
                for line in f: 
                    l = line.split(';')
                    name, description = l[0], l[1] 
                    task = Task(name, description)
                    self.task_list.append(task)
        except FileNotFoundError:
            pass

    def create_task(self):
        while True:
            name = input('Enter task name between 1 to 15 characters: ')
            if len(name) == 0 or len(name) > 15:
                print('Task name should be between 1 and 15 characters')
                continue
            break
        while True:
            description = input('Enter task description less than 255 characters: ')
            if len(description) > 255:
                print('Task description should be less than 255 characters')
                continue
            break
        task = Task(name, description)
        self.task_list.append(task)

        with open('task3.txt', 'a') as f:
            f.write(name + ';') 
            f.write(description + '\n')

    def list_task(self):
        if len(self.task_list) == 0:
            print('\nThere are no tasks. Redirecting back to main menu.')
        for i in range(len(self.task_list)):
            print(i+1, self.task_list[i])

    def remove_task(self):
        while True:
            if len(self.task_list) == 0:
                print('\nThere are no tasks to delete. Redirecting back to main menu.')
                break
            task_index = int(input('Enter the task index to delete the task: '))
            try: 
                self.task_list[task_index - 1]
            except:
                print('Invalid task index. Redirecting back to main menu')
                break
            del self.task_list[task_index-1]

            with open('task3.txt', 'w') as f:
                for item in self.task_list:
                    f.write(str(item) + '\n') # str(item) -> def__str__(self)
            break

    def update_task(self):
        while True:
            if len(self.task_list) == 0:
                print('\nThere are no tasks to update. Redirecting back to main menu.')
                break
            update_index = int(input('Enter the index of the task to update: '))
            try: 
                self.task_list[update_index-1]
            except:
                print('Invalid task index. Redirecting back to main menu')
                break
            name = input('Enter updated task name between 1 to 15 characters: ')
            if len(name) == 0 or len(name) > 15:
                print('Task name should be between 1 and 15 characters')
                continue
            description = input('Enter updated task description less than 255 characters: ')
            if len(description) > 255:
                print('Task name should be less than 255 characters')
                continue
            self.task_list[update_index-1] = name + ';' + description

            with open('task3.txt', 'w') as f:
                for item in self.task_list:
                    f.write(str(item) + '\n')

            break

a = Program()
while True:
    print('\n1. Create a new task\n2. List all tasks\n3. Remove a task\n4. Update task\n5. Exit')
    user_input = int(input('\nChoose an option: '))
    if user_input == 1:
        a.create_task()
    elif user_input == 2:
        a.list_task()
    elif user_input == 3:
        a.remove_task()
    elif user_input == 4:
        a.update_task()
    elif user_input == 5:
        break

