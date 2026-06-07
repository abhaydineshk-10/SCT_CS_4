import os
import re
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox

class AuditLogger:
    _instance = None

    def __new__(cls, log_filename="system_audit.log"):
        if cls._instance is None:
            cls._instance = super(AuditLogger, cls).__new__(cls)
            cls._instance.log_file = log_filename
            cls._instance._initialize_log()
        return cls._instance

    def _initialize_log(self):
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w", encoding="utf-8") as f:
                f.write(f"=== ENTERPRISE AUDIT LOG GENERATED: {datetime.now()} ===\n")
                f.write("Timestamp (UTC)     | Event Type    | Sanitized Payload\n")
                f.write("-" * 70 + "\n")

    def _sanitize_input(self, text: str) -> str:
        sanitized = re.sub(r'\d{4,}', '[MASKED_NUMERIC_DATA]', text)
        return sanitized.strip()

    def write_log(self, event_type: str, payload: str):
        clean_payload = self._sanitize_input(payload)
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(f"{timestamp} | {event_type:<13} | {clean_payload}\n")
        except IOError as e:
            print(f"Logging Error: Security access restriction on file. {e}")

class AuditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enterprise Activity Auditor v1.0")
        self.root.geometry("450x300")
        
        self.logger = AuditLogger()

        self.label = ttk.Label(root, text="Enter Project Notes / Activity Logs:", font=("Arial", 11))
        self.label.pack(pady=10)

        self.text_area = tk.Text(root, height=6, width=50)
        self.text_area.pack(pady=5)
        
        self.text_area.bind("<KeyRelease>", self.handle_local_keystroke)

        self.submit_btn = ttk.Button(root, text="Commit Session to Log", command=self.commit_session)
        self.submit_btn.pack(pady=15)

    def handle_local_keystroke(self, event):
        self.logger.write_log("KEY_INTERACT", f"User modified buffer. Active key symbol: {event.keysym}")

    def commit_session(self):
        user_content = self.text_area.get("1.0", tk.END).strip()
        
        if user_content:
            self.logger.write_log("SESSION_FLUSH", user_content)
            messagebox.showinfo("Success", "Session payload sanitized and safely appended to system_audit.log")
            self.text_area.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Warning", "Cannot commit empty session buffer.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AuditorApp(root)
    root.mainloop()