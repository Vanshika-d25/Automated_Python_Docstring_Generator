import ast

def detect_raises(node):
    return any(isinstance(n, ast.Raise) for n in ast.walk(node))

def detect_yields(node):
    return any(isinstance(n, ast.Yield) for n in ast.walk(node))

def get_class_attributes(node):
    attrs = []
    for n in node.body:
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    attrs.append(t.id)
    return attrs


def generate_stub(node, style="google", is_class=False):
    args = []

    if hasattr(node, "args"):
        for arg in node.args.args:
            if arg.arg != "self":
                args.append(arg.arg)

    if style == "google":
        stub = '"""\nTODO: Add description.\n\n'
        if args:
            stub += "Args:\n"
            for a in args:
                stub += f"    {a}: Description.\n"

        if detect_raises(node):
            stub += "\nRaises:\n    ExceptionType: Description.\n"

        if detect_yields(node):
            stub += "\nYields:\n    Description.\n"

        if is_class:
            attrs = get_class_attributes(node)
            if attrs:
                stub += "\nAttributes:\n"
                for a in attrs:
                    stub += f"    {a}: Description.\n"

        stub += "\nReturns:\n    Description.\n\"\"\""

    elif style == "numpy":
        stub = '"""\nTODO: Add description.\n\nParameters\n----------\n'
        for a in args:
            stub += f"{a} : type\n    Description.\n"

        if detect_raises(node):
            stub += "\nRaises\n------\nExceptionType\n"

        if detect_yields(node):
            stub += "\nYields\n------\nDescription\n"

        stub += "\nReturns\n-------\nDescription\n\"\"\""

    else:  # reST
        stub = '"""\nTODO: Add description.\n\n'
        for a in args:
            stub += f":param {a}: Description\n"
        stub += ":return: Description\n"

        if detect_raises(node):
            stub += ":raises ExceptionType: Description\n"

        if detect_yields(node):
            stub += ":yields: Description\n"

        stub += '"""'

    return stub
