import worktree

def test_nodes():
  node = worktree.Node('learn about potentially relavent stuff 100v 46.0/132.0h (0.00)')
  child = worktree.Node('test 10')
  node.children.append(child)
  node.calc_meta()
  assert node.line == 'learn about potentially relavent stuff'
  assert node.value == 100
  assert node.indiv_hours == 46
  assert node.cum_hours == 46 + 10
  assert node.value_per_hour == node.value / float(node.cum_hours)

  node = worktree.Node('     get sum of all children 3v 7/14h (0.4)')
  assert node.line == '     get sum of all children'
  assert node.value == 3

  node = worktree.Node('learn about AI 1')
  assert node.line == 'learn about AI'

  node = worktree.Node('            for cell in grid ...')
  assert node.line == '            for cell in grid ...'

  node = worktree.Node('https://alchemy-language-demo.mybluemix.net/')
  assert node.line == 'https://alchemy-language-demo.mybluemix.net/'
  assert node.value is None

  node = worktree.Node('    http://lambda-the-ultimate.org/node/4001')
  assert node.line == '    http://lambda-the-ultimate.org/node/4001'
  assert node.value is None
