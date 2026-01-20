import React, { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    if (!file) return alert("Please select a Python file");

    const formData = new FormData();
    formData.append("file", file);

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
    <div className="container">
      <div className="header">
        <h1>🐍 Automated Python Docstring Generator</h1>
        <p>Milestone-1 | AST-Based Docstring Analysis</p>
      </div>

      <div className="upload-box">
        <input
          type="file"
          accept=".py"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button onClick={handleUpload}>Generate</button>
      </div>

      {result && (
        <div className="grid">
          <div className="card">
            <h3>📌 Functions</h3>
            <pre>{result.functions.join("\n") || "None"}</pre>
          </div>

          <div className="card">
            <h3>🏷️ Classes</h3>
            <pre>{result.classes.join("\n") || "None"}</pre>
          </div>

          <div className="card">
            <h3>❌ Missing Docstrings</h3>
            <pre>{result.undocumented.join("\n") || "None"}</pre>
          </div>

          <div className="card" style={{ gridColumn: "1 / -1" }}>
            <h3>📝 Generated Docstring Stubs</h3>
            <pre>{result.stubs.join("\n\n") || "No stubs generated"}</pre>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
