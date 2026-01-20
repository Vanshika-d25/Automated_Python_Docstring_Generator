from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

def generate_stub(node):
    args = []
    if hasattr(node, "args"):
        for arg in node.args.args:
            if arg.arg != "self":
                args.append(arg.arg)

    stub = '"""\nTODO: Add description.\n\n'
    if args:
        stub += "Args:\n"
        for a in args:
            stub += f"    {a}: Description.\n"

    stub += "\nReturns:\n    Description.\n\"\"\""
    return stub

def analyze_code(source_code):
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
                stubs.append(f"{node.name}:\n{generate_stub(node)}")

        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)
            if ast.get_docstring(node):
                documented.append(f"Class: {node.name}")
            else:
                undocumented.append(f"Class: {node.name}")
                stubs.append(f"{node.name}:\n{generate_stub(node)}")

    return {
        "functions": functions,
        "classes": classes,
        "documented": documented,
        "undocumented": undocumented,
        "stubs": stubs,
        "stats": {
            "total_functions": len(functions),
            "total_classes": len(classes),
            "total_objects": len(functions) + len(classes)
        }
    }

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    source_code = file.read().decode("utf-8")

    try:
        result = analyze_code(source_code)
        return jsonify(result)
    except SyntaxError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
