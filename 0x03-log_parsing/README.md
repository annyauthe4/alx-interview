# Log Parser

This Python script reads standard input line by line, extracts structured log information, and computes key metrics such as total file size and counts of HTTP status codes.

## 📋 Description

The script parses log entries with the following format:
<code><IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size></code>

- If a line does not match the expected format, it is ignored.
- Metrics are printed:
  - Every 10 lines
  - On keyboard interruption (`CTRL + C`)
  - On program completion (EOF)

## 📊 Output Example
File size: 1132
200: 3
404: 1
500: 2

Only the following status codes are tracked (in ascending order if present):
200, 301, 400, 401, 403, 404, 405, 500

## 🧠 Features

- Skips malformed lines
- Handles keyboard interruption gracefully
- Aggregates:
  - Total file size
  - Valid HTTP status code counts
- Pycodestyle (PEP8) compliant

## 🚀 Usage

Make the script executable:

```bash
chmod +x log_parser.py

Then you can either:

Run the script and type/paste logs manually:
<code>./log_parser.py</code>

Pipe a log file to the script:
cat access.log | ./log_parser.py

<h1>🛠️ Requirements</h1>
<ul>
  <li>Python 3.x</li>
  <li>No external dependencies</li>
</ul>

## Example Input Line
<code>127.0.0.1 - [11/May/2025:13:55:36] "GET /projects/260 HTTP/1.1" 200 512</code>

<h1>Exit Codes</h1>
<ul>
  <li><code>0</code>: Normal termination</li>
  <li><code>KwyboardInterrupt</code>: Still prints metrics before exiting</li>
</ul>

<h1>Author</h1>
Otetumo Oluwaseun Ayodele - Github[https://github.com/annyauthe4]
