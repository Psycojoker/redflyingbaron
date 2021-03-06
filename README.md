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

# for now, red is an overloaded OrderedDict that contains file paths as keys
# and the corresponding RedBaron instances as values.

red      # display the current files
red[0]   # access by index
red["./test_redflyingbaron.py"]  # access by path (look at how this file is given in the cli; yes, it's a lame example)
red["test_redflyingbaron.py"]    # access by filename
red["test_redflyingbaron"]       # access by filename without extension
red[1:]  # accept slices

red["f:./test_redflyingbaron.py"]  # custom slicing query, returns files that match this request
red["f:redflyingbaron.py"]         # think of using it on a django project and asking
red["f:redflyingbaron"]            # all "models" files

red[re.compile(r'[^_]+')]  # can use a regex (^ and $ are put arround the regex)
red["re:[^_]+"]            # regex for the lazy

red[lambda key, value: "red" in key]  # can use a callable

red.find("stuff")      # return the first matched stuff
red.find_all("stuff")  # return all the matched stuff of all the files
red("stuff")           # same

red.display()  # display the content of the files, useful with a slice

red[0].save()  # save modifications to disk
red.save()     # same but for all files of red (can be combined with slices)

red[0].reload()  # reread the content of the file
red.reload()     # same but for all files of red (can be combined with slices)

red.add("/path/to/file", "/path/to/another/file", "again.py")  # add more files
```

Todo
====

Next
----

* .undo() .redo() (needs modifications of RedBaron to display hooks)
* .set_automatic_save() (or some better/other api) -> save at every modification (needs modifications of RedBaron to display hooks)
* overload __del__ so it behaves like __getitem__
* allow to use globs in red[query]

Futur
-----

* .edit(editor=None) (find editor in $EDITOR of env) launch a text editor on a tmp file containing the currently selected stuff, when editing is done, parse the result and replace the node on which .edit() was done with the result (should be in RedBaron instead?)
* session management: automatically save redflyingbaron instance + undo/redo + files content (not sure on this one) somewhere in .json, allow to list those and go back into a session
* RedBaron wrapper to abstract the filesystem (use this to allow python files to be anywhere http://docs.pyfilesystem.org/en/latest/)
* Add more filesystem abstraction, allow some kind of syntaxe like "sftp://" "fuse://" on the Cli api
* history should be a tree like in vim/emacs
