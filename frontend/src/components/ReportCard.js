import React from "react";

function ReportCard({ stats, pepReport }) {
  return (
    <div>
      <h5 className="fw-bold mb-3">📊 Coverage & Compliance Report</h5>

      <div className="row text-center mb-3">
        <div className="col">
          <div className="border rounded p-2">
            <strong>{stats.total_functions}</strong>
            <br />Functions
          </div>
        </div>

        <div className="col">
          <div className="border rounded p-2">
            <strong>{stats.total_classes}</strong>
            <br />Classes
          </div>
        </div>

        <div className="col">
          <div className="border rounded p-2">
            <strong>{stats.coverage_percent}%</strong>
            <br />Coverage
          </div>
        </div>
      </div>

      <h6 className="fw-semibold">PEP-257 Validation Report</h6>
      <pre>{pepReport}</pre>
    </div>
  );
}

export default ReportCard;
