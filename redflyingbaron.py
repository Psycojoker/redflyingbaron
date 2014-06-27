import re
import sys
from collections import OrderedDict

from IPython.terminal.embed import InteractiveShellEmbed

from redbaron import RedBaron


class FSRedBaron(RedBaron):
    def __init__(self, path):
        super(FSRedBaron, self).__init__(open(path, "r").read())
        self.path = path

    def save(self):
        data = self.dumps()  # this way we only open the file if .dumps() is successful, avoiding destroying the file
        open(self.path, "w").write(data)

    def reload(self):
        super(FSRedBaron, self).__init__(open(self.path, "r").read())


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

        if callable(key):
            for k, value in self.items():
                if key(k, value):
                    key = k
                    break

        if isinstance(key, basestring) and key.startswith("f:"):
            key = key[2:]

            if isinstance(key, basestring) and key.startswith("re:"):
                key = self._string_to_regex(key)

            return self.__class__([x for x in self.items() if self._compare_keys(request=key, mine=x[0])])

        if isinstance(key, (basestring, re._pattern_type)) and key not in self.keys():
            if isinstance(key, basestring) and key.startswith("re:"):
                key = self._string_to_regex(key)

            for i in self.keys():
                if self._compare_keys(request=key, mine=i):
                    key = i
                    break

        return super(RedFlyingBaron, self).__getitem__(key)

    def _string_to_regex(self, key):
        if isinstance(key, basestring) and key.startswith("re:"):
            key = key[3:]
            if not key.startswith("^"):
                key = "^" + key
            if not key.endswith("$"):
                key += "$"
            key = re.compile(key)

        return key

    def _compare_keys(self, request, mine):
        def test(r, m):
            if isinstance(r, re._pattern_type):
                return r.match(m)
            else:
                return r == m

        if test(request, mine):
            return True

        if test(mine.split("/")[-1], request):
            return True

        if test(mine.split("/")[-1].split(".")[0], request):
            return True

        return False

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


    def reload(self):
        for i in self.values():
            i.reload()


    def add(self, *args):
        for i in args:
            self[i] = FSRedBaron(i)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    red = RedFlyingBaron.from_paths(args, verbose=True)
    shell = InteractiveShellEmbed(banner1="", banner2="")
    shell.push(["red", "RedFlyingBaron"])
    print "\nRedFlyingBaron instance is available under the name 'red':"
    print red
    shell.set_next_input("red")
    shell()


if __name__ == '__main__':
    main(sys.argv[1:])
