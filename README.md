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
red["./test_redflyingbaron.py"]  # access by path (look at how this file is given in the cli, yes, it's a lame example)
red["test_redflyingbaron.py"]  # access by filename
red["test_redflyingbaron"]  # access by filename without extension
red[1:]  # accept slices

red.display()  # display the containt of the files, usefull on slice
```

Todo
====

Next
----

* RedBaron wraper to abstract filesystem (use this to allow python files to be anywhere http://docs.pyfilesystem.org/en/latest/ but start with simple files for now)
* .save() (should work on RedFlyingBaron instance/slice or on RedBaron wrapped instances)
* .undo() .redo()
* .add(file_path) (in the futur accept stuff like "protocol://")
* .find() and .find_all() should be delegated to RedBaron instances
* .set_automatic_save() (or some better/other api) -> save at every modification (needs modifications of RedBaron to display hooks)
* allow to filter on filename (with and without extensions) red["f:models"]
* allow to filter using regex red[re.compile("stuff")] red["re:stuff"]
* allow to filter using a lambda red[lambda x: return True]

Futur
-----

* .edit(editor=None) (find editor in $EDITOR of env) launch a text editor on a tmp file containing the currently selected stuff, when editing is done, parse the result and replace the node on which .edit() was done with the result [should be in RedBaron insteand?]
* session management: automatically save redflyingbaron instance + undo/redo + files containt (not sure on this one) somewhere in .json, allow to list those and go back into a session
* Add more filesystem abstraction, allow some kind of syntaxe like "sftp://" "fuse://" on the Cli api
* history should be a tree like in vim/emacs
