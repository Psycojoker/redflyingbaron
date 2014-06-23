Quick & dirty doc
=================

There isn't that much here yet, I'm mostly playing arround.

In \*sh shell:

```bash
python redflyingbaron.py [list of python files]
```

In (I)Python shell:

```python
# assuming that you have run: python redflyingbaron.py redflyingbaron.py ./test_redflyingbaron.py

# for now, red is an overloaded OrderedDict that contains path to files as keys
# and RedBaron instance on those files as value

red  # display the current files
red[0]  # access by index
red["./test_redflyingbaron.py"]  # access by path
red["test_redflyingbaron.py"]  # access by filename
red["test_redflyingbaron"]  # access by filename without extension
red[1:]  # accept slices

red.display()  # display the containt of the files, usefull on slice
```
