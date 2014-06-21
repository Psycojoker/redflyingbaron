from redbaron import RedBaron
from redflyingbaron import RedFlyingBaron


def test_empty():
    RedFlyingBaron()


def test_from_path():
    red = RedFlyingBaron.from_paths(["redflyingbaron.py"])
    assert red.keys() == ["redflyingbaron.py"]
    assert red["redflyingbaron.py"].dumps() == RedBaron(open("redflyingbaron.py", "r").read()).dumps()


def test_from_path_verbose():
    RedFlyingBaron.from_paths(["redflyingbaron.py"], verbose=True)
