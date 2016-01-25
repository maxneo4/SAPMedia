import os
root_path = ''

def resolve_path(sub_path):
    return os.path.join(root_path, sub_path)
