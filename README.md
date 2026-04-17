# AUTOMATION_PROJECTS
all automation projects including n8n assistant and cutting edge automations

## Running tests

To run the unit tests for the `hello_world.py` script, execute:

```bash
cd /Users/gauravujjain/Projects/Repo
python3 -m unittest Test/test_hello_world.py
```

If you prefer `pytest`, create or activate a local virtual environment and run:

```bash
cd /Users/gauravujjain/Projects/Repo
python3 -m venv .venv
. .venv/bin/activate
pytest -q
```

The project keeps test files in the `Test/` folder with names matching the source files as `test_<original_file_name>.py`.

The local virtual environment directory `.venv/` is already ignored by this repository and should not be committed.
