tasks = []

def add_task (title):
    tasks.append({"title": title, "done": False})
    print(f'added: {title}')

if __name__ == "__main__":
    add_task("buy milk")
    print(tasks)