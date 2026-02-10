import React from "react";

function ResultView({ result }) {
  return (
    <div className="row g-3">
      <div className="col-md-6">
        <div className="card p-3 shadow-sm">
          <h5 className="fw-bold">📌 Detected Functions</h5>
          <pre>{result.functions.join("\n") || "No functions found"}</pre>
        </div>
      </div>

      <div className="col-md-6">
        <div className="card p-3 shadow-sm">
          <h5 className="fw-bold">🏷️ Detected Classes</h5>
          <pre>{result.classes.join("\n") || "No classes found"}</pre>
        </div>
      </div>

      <div className="col-md-6">
        <div className="card p-3 shadow-sm border-danger">
          <h5 className="fw-bold text-danger">❌ Missing Docstrings</h5>
          <pre>{result.undocumented.join("\n") || "All documented!"}</pre>
        </div>
      </div>

      <div className="col-md-6">
        <div className="card p-3 shadow-sm">
          <h5 className="fw-bold">📝 Generated Docstring Stubs</h5>
          <pre>{result.stubs.join("\n\n") || "No stubs generated"}</pre>
        </div>
      </div>
    </div>
  );
}

export default ResultView;
