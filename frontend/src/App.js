import React, { useState } from "react";

import FileUpload from "./components/FileUpload";
import StyleSelector from "./components/StyleSelector";
import ResultView from "./components/ResultView";
import ReportCard from "./components/ReportCard";

function App() {
  const [file, setFile] = useState(null);
  const [style, setStyle] = useState("google");
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    if (!file) return alert("Please select a Python file");

    const formData = new FormData();
    formData.append("file", file);
    formData.append("style", style);

    try {
      const res = await fetch("http://localhost:5000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      setResult(data);
    } catch (err) {
      alert("Backend not running!");
    }
  };

  return (
    <div className="container my-4">

      <div className="text-center p-4 mb-4 bg-primary text-white rounded shadow">
        <h1 className="fw-bold">🐍 Automated Python Docstring Generator</h1>
        <p className="mb-0">
          Generate standardized Python docstrings using AST analysis,
          with Google, NumPy, and reST styles + PEP-257 validation.
        </p>
      </div>

      <div className="card p-3 mb-4 shadow-sm">
        <div className="row g-3 align-items-center">

          <div className="col-md-4">
            <StyleSelector style={style} setStyle={setStyle} />
          </div>

          <div className="col-md-5">
            <FileUpload setFile={setFile} />
          </div>

          <div className="col-md-3 text-end">
            <button className="btn btn-success w-100" onClick={handleUpload}>
              🚀 Generate Docstrings
            </button>
          </div>

        </div>
      </div>

      {result && (
        <>
          <ResultView result={result} />

          <div className="card p-3 mt-4 shadow">
            <ReportCard
              stats={result.stats}
              pepReport={result.pep257_report}
            />
          </div>
        </>
      )}

      <div className="text-center mt-5 text-muted">
        <small>
          © 2026 | Python Documentation Automation Tool  
          <br />
          Built with Flask, React, AST & PEP-257
        </small>
      </div>

    </div>
  );
}

export default App;
