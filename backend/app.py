from flask import Flask, request, jsonify
from analyzer.ast_parser import analyze_code
from analyzer.pep257_checker import check_pep257

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    style = request.form.get("style", "google")

    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    source_code = file.read().decode("utf-8")

    try:
        analysis_result = analyze_code(source_code, style)
        pep_report = check_pep257(source_code)

        analysis_result["pep257_report"] = pep_report
        return jsonify(analysis_result)

    except SyntaxError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
