import io

def read_file(file: str):
    file = io.open(file, 'r', encoding="utf8")
    file_contents = file.read()
    file.close()
    return file_contents