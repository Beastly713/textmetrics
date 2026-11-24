# TextMetrics — CLI Text Analyzer

A lightweight Python command-line application that analyzes text and
computes basic textual statistics.

This project demonstrates distributed version control using Git and
GitHub, with particular emphasis on branching, committing, remote
synchronization, merging, and intentional merge conflict resolution.

## Features

- **Word Count:** Counts whitespace-separated words in the input text.
- **Character Count:** Counts characters, including spaces and newlines.
- **Line Count:** Counts the number of lines in the input text.
- **JSON Output:** Displays analysis results in a structured format.
- **Unit Testing:** Validates individual metrics and edge cases.

## Technology Stack

- Python 3.10+
- Git
- GitHub
- Python Standard Library (`argparse`, `json`, `unittest`)

No external dependencies are required.

## Project Structure

```text
textmetrics/
├── analyzer.py       # Core text analysis and CLI implementation
├── test_analyzer.py  # Automated unit tests
├── README.md         # Project documentation
└── .gitignore        # Git exclusion rules
```

## Usage

Clone the repository:

```bash
git clone https://github.com/beastly713/textmetrics.git
cd textmetrics
```

Run the application:

```bash
python3 analyzer.py "Hello GitHub"
```

Output:

```json
{
  "words": 2,
  "characters": 12,
  "lines": 1
}
```

For multiline text:

```bash
python3 analyzer.py $'Hello GitHub\nLearning Git'
```

Output:

```json
{
  "words": 4,
  "characters": 25,
  "lines": 2
}
```

## Git Branching Strategy

| Branch | Purpose |
|---|---|
| `main` | Stable application and final integrated implementation |
| `feature/character-count` | Independent development of character counting |
| `feature/line-count` | Independent development of line counting |

Both feature branches were created from the same version of `main`
to demonstrate isolated feature development.

## Version Control Workflow

1. Initialized a local Git repository using `git init`.
2. Implemented and committed the initial word-count functionality.
3. Connected the local repository to a GitHub remote.
4. Demonstrated remote synchronization using `git push` and `git pull`.
5. Created two independent feature branches.
6. Implemented and committed the respective features.
7. Merged the character-count branch into `main`.
8. Attempted to merge the line-count branch, triggering a merge conflict.
9. Inspected and manually resolved the conflicting implementations.
10. Committed and pushed the resolved implementation.
11. Added unit tests to validate the final application.

## Intentional Merge Conflict

### Cause

Both feature branches independently modified the same return statement
inside the `analyze_text()` function in `analyzer.py`.

The original implementation was:

```python
return {"words": len(text.split())}
```

The character-count branch modified it to:

```python
return {"words": len(text.split()), "characters": len(text)}
```

The line-count branch modified it to:

```python
return {"words": len(text.split()), "lines": len(text.splitlines())}
```

After successfully merging `feature/character-count` into `main`,
the following command triggered a content merge conflict:

```bash
git merge --no-ff feature/line-count
```

Git could not automatically reconcile the overlapping changes made
to the same line of code.

### Conflict Inspection

The conflicting changes were investigated using:

```bash
git status
git diff
git diff --name-only --diff-filter=U
```

### Manual Conflict Resolution

Instead of accepting either branch's implementation and discarding
the other, both functionalities were manually integrated using the
VS Code three-way merge editor.

The resolved implementation is:

```python
def analyze_text(text: str) -> dict[str, int]:
    return {
        "words": len(text.split()),
        "characters": len(text),
        "lines": len(text.splitlines()),
    }
```

The resolved file was staged, inspected, committed, and pushed:

```bash
git add analyzer.py
git diff --cached
git diff --cached --check
git status
git commit -m "merge: resolve conflict and integrate all text metrics"
git push origin main
```

This resolution preserves the original functionality and both
independently developed features.

## Testing

Run the automated unit tests:

```bash
python3 -m unittest -v
```

The test suite covers:

| Test | Purpose |
|---|---|
| `test_word_count` | Validates word counting |
| `test_character_count` | Validates character counting |
| `test_line_count` | Validates multiline text analysis |
| `test_empty_text` | Validates empty input handling |
| `test_combined_metrics` | Validates all metrics together |

## Git History

The branching and merging history can be visualized using:

```bash
git log --oneline --graph --all --decorate
```

The `--no-ff` merge option was used to preserve explicit merge commits
and make the branching history visible.


## Conclusion

TextMetrics demonstrates a complete Git-based development workflow,
from repository initialization to feature development, intentional
merge conflict creation, manual resolution, testing, and remote
synchronization.

The final implementation integrates all three text analysis metrics
while preserving the development history of both feature branches.