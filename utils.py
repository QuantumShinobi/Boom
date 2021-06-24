

def check_if_present(username: str, todo: str):

    file = open('./users.txt', 'r')
    if username in file.readlines():
        if todo.lower() == "add":
            file.close()
            return False
    else:
        w_file = open('./users.txt', 'w')
        w_file.write(username)
        w_file.close()
        return True
