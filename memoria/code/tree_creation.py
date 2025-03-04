# Init tree
root = construct_behaviour_tree_from_xml(xml_doc)
tree = py_trees_ros.trees.BehaviourTree(root=root unicode_tree_debug=False)

# Setup tree
try:
    tree.setup(timeout=timeout)
except py_trees_ros.exceptions.TimedOutError as e:
    tree.shutdown()
    return None

return tree
