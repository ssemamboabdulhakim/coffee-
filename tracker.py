tasks = []

def add_task (title):
    tasks.append({"title": title, "done": False})
    print(f'added: {title}')

if __name__ == "__main__":
    add_task("buy milk")
    print(tasks)

def complete_task(title):
    for task in tasks :
        if task('title') == title:
            task ['done'] = True
            print(f'completed:{title}') 
            return
        raise ValueError(f'task not found{title}')        