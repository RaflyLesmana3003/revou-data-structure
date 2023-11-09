from bigtree import BinaryNode, print_tree

root = BinaryNode("aguss", level="1", umur="20")

child_1 = BinaryNode("aguss 1", level="112", umur="23")
child_2 = BinaryNode("aguss 2",  level="31", umur="41")
child_3 = BinaryNode("aguss 3", level="41", umur="12")
child_4 = BinaryNode("aguss 4", level="213", umur="42")
child_5 = BinaryNode("aguss 5", level="213", umur="14")
child_6 = BinaryNode("aguss 6", umur="53")

root.children = [child_1, child_2]
child_3.parent = child_2
child_4.parent = child_2
child_5.parent = child_1
child_6.parent = child_5

# root.show()

print_tree(root,all_attrs=True)