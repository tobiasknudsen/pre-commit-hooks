pre-commit-hooks
================

My pre-commit-hooks

More info at [pre-commit.com](https://pre-commit.com/)

### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/tobiasknudsen/pre-commit-hooks
    rev: v0.1.0  # Use the ref you want to point at
    hooks:
    -   id: check-forbidden-strings
    # -   id: ...
```

### Hooks

#### `check-forbidden-strings`

Prevent commit if specific provided strings exists in the staged files.
    - Pass the forbidden strings in `args: [-string=do not commit, -s=local_testing_variable]`.
    - Supports regular expressions.
