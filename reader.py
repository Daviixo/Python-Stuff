import promptlib

def check_if_exists(search_id, read_file):

    search_id = search_id.replace(" ","")

    check_file = open(read_file, 'r')

    flag = 0
    index = 0

    for line in check_file:
        index += 1

        if search_id in line:
            flag = 1
            break

    if flag == 0:
        result = 'String ' + str(search_id) + ' was NOT found! :c'
        return result
    else:
        result = 'String ' + str(search_id) + ' was found in line ' + str(index) + '! :D'
        return result


def get_path():

    prompter = promptlib.Files()
    files_path = prompter.file()
    print(dir, '\n', files_path)

    return files_path

def main():
    print("""

    WELCOME!    

    """)

    session_id = input("What are you searching for?\n")
    files_path = get_path()
    response = check_if_exists(session_id,files_path)
    print(response)


if __name__ == '__main__':
    main()