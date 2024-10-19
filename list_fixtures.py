# list_fixtures.py
import ast
import os

# Traverse all .py files in the 'features' directory
for dirname, _, filenames in os.walk('features'):
    for filename in filenames:
        if filename.endswith('.py'):
            with open(os.path.join(dirname, filename)) as file:
                # Parse the Python source code
                root = ast.parse(file.read())

                for node in ast.walk(root):
                    # Check if it's a function definition
                    if isinstance(node, ast.FunctionDef):
                        for decorator in node.decorator_list:
                            # Check if the decorator is 'fixture' or 'use_fixture'
                            if isinstance(decorator, ast.Name) and decorator.id in ['fixture', 'use_fixture']:
                                print(f'In file {filename}, fixture: {node.name}')
