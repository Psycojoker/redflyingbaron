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


def test_getitem_by_index():
    red = RedFlyingBaron.from_paths(["redflyingbaron.py", "test_redflyingbaron.py"])
    assert red[0].dumps() == RedBaron(open("redflyingbaron.py", "r").read()).dumps()


def test_getitem_slice():
    red = RedFlyingBaron.from_paths(["redflyingbaron.py", "test_redflyingbaron.py"])
    red = red[1:]
    assert red[0].dumps() == RedBaron(open("test_redflyingbaron.py", "r").read()).dumps()


def test_getitem_by_filename():
    red = RedFlyingBaron.from_paths(["./redflyingbaron.py", "./test_redflyingbaron.py"])
    assert red["redflyingbaron.py"].dumps() == RedBaron(open("redflyingbaron.py", "r").read()).dumps()
    assert red["test_redflyingbaron.py"].dumps() == RedBaron(open("test_redflyingbaron.py", "r").read()).dumps()


def test_getitem_by_filename_without_extension():
    red = RedFlyingBaron.from_paths(["./redflyingbaron.py", "./test_redflyingbaron.py"])
    assert red["redflyingbaron"].dumps() == RedBaron(open("redflyingbaron.py", "r").read()).dumps()
    assert red["test_redflyingbaron"].dumps() == RedBaron(open("test_redflyingbaron.py", "r").read()).dumps()


def test_display_exist():
    red = RedFlyingBaron.from_paths(["./redflyingbaron.py", "./test_redflyingbaron.py"])
    red.display()


def test_find_delegate():
    red = RedFlyingBaron.from_paths(["./redflyingbaron.py", "./test_redflyingbaron.py"])
    assert red.find("name") is red[0].find("name")
    assert red.find("def", name="test_find_delegate") is red[1].find("def", name="test_find_delegate")


def test_find_all_delegate():
    red = RedFlyingBaron.from_paths(["./redflyingbaron.py", "./test_redflyingbaron.py"])
    assert red.find_all("name") == red[0].find_all("name") + red[1].find_all("name")
    assert red("name") == red[0]("name") + red[1]("name")
