WorkTree is a place for you to dump your mind and track your time.

See test.txt an example tree file.  It's just indented plain text.

Here is an example string with full metadata:
  "     get sum of all children 3v 7/14h (0.5)"
                                ^  ^  ^    ^
                                |  |  |    |
                            value  |  |    value / cumulative hours
                                   |  |
                    individual hours  cumulative hours

Definitions:
  value -- An arbitrary integer indicating how much is this task is worth relative to other things
           you could be working on.
  individual hours -- How many hours have you spent working on this task?
  cumulative hours -- How many hours have you spent working on this task including all of its
                      child tasks?
  value / cumulative hours -- If this number is high you're doing things right.

You can also use the following shorthand to declare metadata:
  "     get sum of all children 3v 7h"
                                ^  ^
                                |  |
                            value  individual hours

Or:
  "     get sum of all children 7"
                                ^
                                |
                                individual hours

Metadata is parsed and updated every time you run worktree.py

Usage Tips:

I use Sublime Text to view and edit my worktree.txt file.
The first thing I do upon opening the file is fold everything, like so:
  Edit -> Code Folding -> Fold All (Cmd K, Cmd 1)
  I then click on the node I want to expand, then do (Cmd K, Cmd 2), and so forth.
  Note these fold commands only fold expanded nodes, they won't expand collapsed ones.
  Note also that these commands won't fold a child node if the cursor is currently on that node.

I keep worktree.txt in my Dropbox so I always have a backup.
I have a symlink called `wt` to worktree.py in my path, so I can just run `wt` in my terminal
to regenerate the metadata.
