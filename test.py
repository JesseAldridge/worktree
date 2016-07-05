import tree_note_parse

def test_nodes():
  node = tree_note_parse.Node('     get sum of all children 3v 7/14h (0.4)')
  assert node.line == '     get sum of all children'
  assert node.value == 3

  node = tree_note_parse.Node('learn about AI 1')
  assert node.line == 'learn about AI'

  node = tree_note_parse.Node('            for cell in grid ...')
  assert node.line == '            for cell in grid ...'

  node = tree_note_parse.Node('https://alchemy-language-demo.mybluemix.net/')
  assert node.line == 'https://alchemy-language-demo.mybluemix.net/'
  assert node.value is None

  node = tree_note_parse.Node('    http://lambda-the-ultimate.org/node/4001')
  assert node.line == '    http://lambda-the-ultimate.org/node/4001'
  assert node.value is None
