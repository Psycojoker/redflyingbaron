from redbaron import RedBaron


class RedFlyingBaron(object):
    def __init__(self, files):
        self.files = dict(zip(files, map(RedBaron, map(lambda x: open(x, "r").read(), files))))
