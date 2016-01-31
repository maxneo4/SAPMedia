import os
root_path = ''


def set_root_path_from(main_file):
    global root_path
    root_path = os.path.dirname(os.path.realpath(main_file))


def resolve_path(sub_path):
    return os.path.join(root_path, sub_path)

