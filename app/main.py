import os


def move_file(command: str) -> None:
    _, src_path, dest_path = command.split()

    if dest_path.endswith("/"):
        dir_path = dest_path
        filename = os.path.basename(src_path)
        dest_file_path = os.path.join(dir_path, filename)
    else:
        dir_path = os.path.dirname(dest_path)
        dest_file_path = dest_path

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    # Lettura è scrittura di u schedariu
    with open(src_path, "r") as src_file:
        content = src_file.read()

    with open(dest_file_path, "w") as dest_file:
        dest_file.write(content)

    os.remove(src_path)
