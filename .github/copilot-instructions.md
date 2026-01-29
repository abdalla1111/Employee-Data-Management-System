# Copilot / AI Agent Instructions

Purpose: Help AI coding agents quickly understand and edit this small Python CLI app.

- **Big picture:** single-file CLI app implemented as `EmployeeManager` (see [Class.py](Class.py#L1)). It stores employee records in-memory (a dict keyed by `ID`) and persists to `employees.csv` using the `csv` stdlib.
- **Main entry:** top-level `if __name__ == "__main__"` loop in [Class.py](Class.py#L80-L118). The runnable UI is a simple text menu implemented in that loop.

- **Data model & persistence:** CSV file `employees.csv` at repo root. Headers are `['ID','Name','Position','Salary','Email']` (see `save_data()` in [Class.py](Class.py#L20-L30)). `load_data()` uses `csv.DictReader` and sets `self.employees[row['ID']] = row` (values will be strings).
  - Important: when adding new records the code stores `Salary` as a `float` (see `add_employee()`), but `load_data()` returns strings. Be careful with type conversions when changing code that assumes numeric salary.

- **Common code patterns to follow:**
  - Mutate `self.employees` then call `save_data()` to persist changes (example: `self.employees[emp_id] = new_emp; self.save_data()` in `add_employee()`).
  - Keep CSV header order consistent with `save_data()` to avoid field mismatch.
  - Minimal validation: salary checked with `float()` in `add_employee()`; otherwise inputs are accepted as-is.

- **Where to make changes:**
  - Core logic: edit [Class.py](Class.py) (the notebook contains same code). Prefer small, local edits around `add_employee`, `update_employee`, `delete_employee`, `load_data`, and `save_data`.

- **Run / dev commands (Windows, repository root):**
  - Activate venv (PowerShell): `venv\Scripts\Activate.ps1`
  - Run script: `python Class.py`
  - Run as notebook: open the included notebook and execute cells (the code mirrors `Class.py`).

- **Tests & CI:** none found. No test runner or build steps; run manual smoke tests by exercising the menu and verifying `employees.csv` updates.

- **Conventions & constraints:**
  - No external dependencies — only Python standard library (`csv`).
  - File paths are repo-root relative; `employees.csv` expected in working directory.
  - Keep changes minimal and maintain backwards compatibility for the CSV layout.

- **Integration points / side effects:**
  - `employees.csv` is the single persistence artifact. Agents must not assume a DB or external service.
  - The app mutates the CSV on each change; concurrent edits may cause data loss.

- **Suggested quick edits examples:**
  - To normalize salary types on load, update `load_data()` to cast `row['Salary']` to `float` if possible.
  - To add email validation, modify `add_employee()` before inserting into `self.employees`.

If anything here is unclear or you'd like different focus (e.g., converting to a package layout or adding tests), tell me which area and I'll update this file.
