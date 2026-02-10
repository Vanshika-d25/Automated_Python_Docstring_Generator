function FileUpload({ setFile }) {
  return (
    <div>
      <label className="form-label fw-semibold">
        📂 Upload Python File
      </label>
      <input
        type="file"
        className="form-control"
        accept=".py"
        onChange={(e) => setFile(e.target.files[0])}
      />
    </div>
  );
}
export default FileUpload;
