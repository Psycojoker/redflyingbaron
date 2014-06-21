from collections import OrderedDict
from redbaron import RedBaron


test_files = [
"../baron/baron/baron.py",
"../baron/baron/conftest.py",
"../baron/baron/dumper.py",
"../baron/baron/formatting_grouper.py",
"../baron/baron/future.py",
"../baron/baron/grammator.py",
"../baron/baron/grammator_control_structures.py",
"../baron/baron/grammator_data_structures.py",
"../baron/baron/grammator_imports.py",
"../baron/baron/grammator_operators.py",
"../baron/baron/grammator_primitives.py",
"../baron/baron/grouper.py",
"../baron/baron/helpers.py",
"../baron/baron/indentation_marker.py",
"../baron/baron/inner_formatting_grouper.py",
"../baron/baron/parser.py",
"../baron/baron/path.py",
"../baron/baron/render.py",
"../baron/baron/spliter.py",
"../baron/baron/token.py",
"../baron/baron/tokenizer.py",
]


class RedFlyingBaron(OrderedDict):
    @classmethod
    def from_paths(class_, files, verbose=False):
        def load_file(path):
            if verbose:
                print("Loading %s..." % path)
            return RedBaron(open(path, "r").read())
        return class_(dict(zip(files, map(load_file, files))))

    def __repr__(self):
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


def main():
    red = RedFlyingBaron.from_paths(test_files[:5], verbose=True)
    from ipdb import set_trace; set_trace()


if __name__ == '__main__':
    main()
