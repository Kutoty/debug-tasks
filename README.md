# Reproducible Debugging Task Set

Three broken programs. Each folder has the bug and the fix. `check.py` proves the bug fails and the fix passes.

## Run

```bash
python3 check.py
docker build -t debug-tasks .
docker run --rm debug-tasks
```

GitHub Actions runs the checker and the Docker build on every push.
