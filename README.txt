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