import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    src_path = parts[1]
    dest_path = parts[2]

    if dest_path.endswith("/"):
        dir_path = dest_path
        filename = os.path.basename(src_path)
        dest_file_path = os.path.join(dir_path, filename)
    else:
        dir_path = os.path.dirname(dest_path)
        dest_file_path = dest_path

    if dir_path:
        folders = dir_path.split("/")
        current_dir = ""
        for folder in folders:
            if folder:
                current_dir = os.path.join(current_dir, folder)
                if not os.path.exists(current_dir):
                    os.mkdir(current_dir)

    with open(src_path, "r") as src_file:
        content = src_file.read()

    with open(dest_file_path, "w") as dest_file:
        dest_file.write(content)

    os.remove(src_path)
