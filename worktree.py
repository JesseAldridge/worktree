# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import re, os

'''
Read file containing tree of indented strings following a simple format.
Parse out metadata from each line.
Do some processing on this tree and write the nodes back out with updated metadata.
'''

with open(os.path.expanduser('~/Dropbox/worktree.txt')) as f:
  text = f.read()


class Node:
  def __init__(self, line):
    self.line = line
    self.children = []
    self.indiv_hours, self.cum_hours = 0, 0
    self.value = None

    # Parse out existing metadata in either full or shorthand formats.

    def full_meta():
      self.value, self.indiv_hours, self.cum_hours, _ = [
        float(re.sub('[^0-9\.]', '', s)) for s in match.group(1).replace('/', ' ').split()]

    def short_meta():
      self.value, self.indiv_hours = [
        float(re.sub('[^0-9\.]', '', s)) for s in match.group(1).split()]

    def simple_hours():
      self.value = 0
      self.indiv_hours = float(match.group(1))
      self.cum_hours = self.indiv_hours

    float_regex = '[0-9]+(?:\.?[0-9]*)'
    for meta_regex, parse in (
      (' ({f}v {f}/{f}h \({f}\))$', full_meta),
      (' ({f}v {f}h)$', short_meta),
      (' ({f})$', simple_hours)):
      meta_regex = meta_regex.format(f=float_regex)
      match = re.search(meta_regex, line)
      if match:
        parse()
        self.line = re.sub(meta_regex, '', line)
        break

  def calc_meta(self):
    " cumulative hours = individual hours + cumulative hours of children "

    cum_hours = self.indiv_hours
    for child in self.children:
      child.calc_meta()
      if child.value is not None:
        cum_hours += child.cum_hours
    self.cum_hours = cum_hours
    self.value_per_hour = 0
    if self.value is not None:
      if self.cum_hours == 0:
        self.value_per_hour = self.value
      else:
        self.value_per_hour = self.value / self.cum_hours
    self.children.sort(key=lambda node: -node.value_per_hour)

  def render_lines(self):
    " Include metadata with line. "

    full_line = self.line
    if self.value is not None:
      full_line = '{} {}v {}/{}h ({:.2f})'.format(
        self.line, self.value, self.indiv_hours, self.cum_hours, self.value_per_hour)
    full_line = re.sub('^( *)- ', '\g<1>', full_line)
    yield full_line
    for child in self.children:
      for line in child.render_lines():
        yield line


def build_tree(root_line, line_iter):
  ' Convert indented lines of text to Nodes. '

  try:
    root = Node(root_line)
  except:
    print 'error on line:', root_line
    raise
  try:
    next_line = line_iter.next()
  except StopIteration:
    return root, None
  while next_line is not None and indent(next_line) > indent(root_line):
    child, next_line = build_tree(next_line, line_iter)
    root.children.append(child)
  return root, next_line

def indent(line):
  return (len(line) - len(line.lstrip())) / 2


def main():
  ' Convert text into Nodes.  Store top level nodes.  Process tree. '

  line_iter = iter(line.rstrip() for line in text.splitlines() if line.rstrip())
  top_nodes = []
  next_line = line_iter.next()
  while next_line is not None:
    child, next_line = build_tree(next_line, line_iter)
    top_nodes.append(child)
  for node in top_nodes:
    node.calc_meta()

  with open(os.path.expanduser('~/Dropbox/worktree.txt'), 'w') as f:
    for node in top_nodes:
      for line in node.render_lines():
        f.write(line + '\n')


if __name__ == '__main__':
  main()
