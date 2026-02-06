def generate_stats(functions, classes, documented, undocumented):
    total = len(functions) + len(classes)
    coverage = (len(documented) / total * 100) if total else 0

    return {
        "total_functions": len(functions),
        "total_classes": len(classes),
        "documented": len(documented),
        "undocumented": len(undocumented),
        "coverage_percent": round(coverage, 2)
    }
