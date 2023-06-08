#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    pkg_names = dir(hidden_4)
    for name in pkg_names:
        if not name.startswith('__'):
            print(name)
