import sys
from collections import OrderedDict

from IPython.terminal.embed import InteractiveShellEmbed

from redbaron import RedBaron


class FSRedBaron(RedBaron):
    def __init__(self, path):
        super(FSRedBaron, self).__init__(open(path, "r").read())
        self.path = path

    def save(self):
        open(self.path, "w").write(self.dumps())


class RedFlyingBaron(OrderedDict):
    @classmethod
    def from_paths(class_, files, verbose=False):
        to_return = class_()
        for path in files:
            if verbose:
                print("Loading %s..." % path)
            to_return[path] = FSRedBaron(path)
        return to_return

    def __repr__(self):
        if not self.keys():
            return "Empty RedFlyingBaron instance"
        return "\n".join(["%s -> %s" % (num, path) for (num, path) in enumerate(self.keys())])

    def __getitem__(self, key):
        if isinstance(key, int):
            key = self.keys()[key]

        if isinstance(key, slice):
            return self.__class__(self.items()[key])

        if isinstance(key, basestring) and key not in self.keys():
            for i in self.keys():
                if i.split("/")[-1] == key:
                    key = i
                    break

                if i.split("/")[-1].split(".")[0] == key:
                    key = i
                    break

        return super(RedFlyingBaron, self).__getitem__(key)

    def display(self):
        for i in self.keys():
            print "==============================================================================="
            print i
            print "==============================================================================="
            print self[i]

    def find(self, identifier, *args, **kwargs):
        for i in self.values():
            result = i.find(identifier, *args, **kwargs)
            if result is not None:
                return result

        return None

    def find_all(self, identifier, *args, **kwargs):
        result = []
        for i in self.values():
            result += i.find_all(identifier, *args, **kwargs)

        return result

    __call__ = find_all

    def save(self):
        for i in self.values():
            i.save()


def main(args):
    red = RedFlyingBaron.from_paths(args, verbose=True)
    shell = InteractiveShellEmbed(banner1="", banner2="")
    shell.push(["red", "RedFlyingBaron"])
    print "\nRedFlyingBaron instance is available under the name 'red':"
    print red
    shell.set_next_input("red")
    shell()


if __name__ == '__main__':
    main(sys.argv[1:])
