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


def main():
    RedFlyingBaron.from_paths(test_files, verbose=True)


if __name__ == '__main__':
    main()
