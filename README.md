# Reproducible Debugging Task Set

Three small broken programs. Each folder has the bug and a verified fix. `check.py` proves the buggy version fails the check and the fixed version passes.

## Run

```bash
python3 check.py
```

## Tasks

| Folder | Bug |
| --- | --- |
| `tasks/off-by-one` | The loop stops one item early. |
| `tasks/missing-key` | A missing key raises instead of returning nothing. |
| `tasks/wrong-mean` | The mean divides by one more than the count. |
