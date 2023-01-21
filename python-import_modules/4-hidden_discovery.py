#!/usr/bin/python3
# Executing module as script
if __name__ == "__name__":

    # importing module
    import hidden_4

    # show the names in the hidden_4 module
    names = dir(hidden_4)

    for name in names:
        if name[:2] != "__":
            print(name)
