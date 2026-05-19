def write_text_to_file(file_path, text):
    with open(file_path, "w", encoding = "utf-8") as file:
        file.write(text)

def append_text_to_file(file_path, text):
    with open(file_path, "a", encoding = "utf-8") as file:
        file.write(text)

def read_text_from_file(file_path):
    try:
        with open(file_path, "r", encoding = "utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None