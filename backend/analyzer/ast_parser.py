import ast
from analyzer.stub_generator import generate_stub
from analyzer.report_generator import generate_stats

def analyze_code(source_code, style="google"):
    tree = ast.parse(source_code)

    functions = []
    classes = []
    documented = []
    undocumented = []
    stubs = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

            if ast.get_docstring(node):
                documented.append(f"Function: {node.name}")
            else:
                undocumented.append(f"Function: {node.name}")
                stubs.append(f"{node.name}:\n{generate_stub(node, style)}")

        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

            if ast.get_docstring(node):
                documented.append(f"Class: {node.name}")
            else:
                undocumented.append(f"Class: {node.name}")
                stubs.append(f"{node.name}:\n{generate_stub(node, style, is_class=True)}")

    stats = generate_stats(functions, classes, documented, undocumented)

    return {
        "functions": functions,
        "classes": classes,
        "documented": documented,
        "undocumented": undocumented,
        "stubs": stubs,
        "stats": stats
    }
