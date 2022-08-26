#!/usr/bin/python3
if __name__ == "__main__":
<<<<<<< HEAD
    from sys import argv
    add = 0
    for s in argv[1:]:
        add += int(s)
    print("{:d}".format(add))
=======
    import hidden_4
    for s in dir(hidden_4):
        if s[:2] != "__":
            print("{:s}".format(s))
>>>>>>> 181fdb884e12878c3afd356f8bd7c222f7fa72fa
