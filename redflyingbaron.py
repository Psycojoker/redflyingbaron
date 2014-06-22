import sys
from collections import OrderedDict

from IPython.terminal.embed import InteractiveShellEmbed

from redbaron import RedBaron


class RedFlyingBaron(OrderedDict):
    @classmethod
    def from_paths(class_, files, verbose=False):
        to_return = class_()
        for path in files:
            if verbose:
                print("Loading %s..." % path)
            to_return[path] = RedBaron(open(path, "r").read())
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
