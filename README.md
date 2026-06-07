# Key Logger Recorder v1.0

An internal activity recording and auditing utility built in Python. This application demonstrates secure software engineering workflows by logging interface interactions within a sandboxed environment using defensive structural patterns.

## 🚀 Key Features & Architecture

- **Singleton Logger Pattern:** Implements a single, thread-safe access point for file system logging to eliminate file write conflicts.
- **Data Minimization & Sanitization:** Automatically parses text inputs using regular expressions to strip out and mask sensitive numeric sequences before writing to disk.
- **Least Privilege Access:** Binds strictly to localized UI event triggers, respecting modern operating system boundaries and process isolation rules.

## 🛠️ Project Structure

```text
key-logger-recorder/
│
├── .gitignore          # Prevents tracking of local log output
├── README.md           # Documentation and architecture breakdown
├── requirements.txt    # Project dependency specification
└── src/
    └── key_logger_recorder.py  # Application source code
