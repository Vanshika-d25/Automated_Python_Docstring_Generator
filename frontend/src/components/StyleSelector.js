import React from "react";

function StyleSelector({ style, setStyle }) {
  return (
    <div className="style-box">
      <label>Docstring Style: </label>
      <select value={style} onChange={(e) => setStyle(e.target.value)}>
        <option value="google">Google</option>
        <option value="numpy">NumPy</option>
        <option value="rest">reST</option>
      </select>
    </div>
  );
}

export default StyleSelector;
