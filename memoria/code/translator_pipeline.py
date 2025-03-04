# 1. Generate a basic xml tree from the JSON definition 
if json_tree_path != "": 
    json_translator.translate(json_tree_path, xml_tree_path)

# 2. Generate a self-contained xml tree 
tree_generator.generate(xml_tree_path, action_path, self_contained_tree_path)

# 3. Using the self-contained tree, package the ROS 2 app
zip_file_path = app_generator.generate(self_contained_tree_path, app_name, template_path, action_path, tree_gardener_src)
