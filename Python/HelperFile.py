def read_file(file_name):
    file = open(file_name, 'r')
    return file


def read_and_split_text(file_name, split_on):
    file = read_file(file_name)
    content = file.read()
    return content.split(split_on), file
