<h1> UTF-8 Validation</h1>
UTF-8 (Unicode Transformation Format - 8-bit) is:
<ul>
    <li>A variable-length encoding for Unicode.</li>
    <li>Backward-compatible with ASCII.</li>
    <li>Efficient: it uses 1 to 4 bytes to encode characters.</li>
</ul>

<h1>UTF-8 Encoding Rules</h1>
<ul>
    <li>1-byte: Starts with <code>0</code></li>
    <li>2-byte: Starts with <code>110</code>, followed by one <code>10</code> continuation byte</li>
    <li>3-byte: Starts with <code>1110</code>, followed by two <code>10</code> continuation bytes</li>
    <li>4-byte: Starts with <code>11110</code>, followed by three <code>10</code> continuation bytes</li>
</ul>
