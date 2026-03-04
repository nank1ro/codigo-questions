# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains coding exercises for the [Codigo App](https://codigo.bestofcode.dev). Exercises are written in Markdown with frontmatter metadata and parsed by a custom Dart-based parser. The content is served via Firebase Storage to the mobile app.

## Repository Structure

```
codigo-questions/
├── en/                    # English exercises
│   ├── {language}/        # Programming language (c, dart, javascript, kotlin, python, swift)
│   │   ├── {argument}/    # Topic/category (e.g., variables, functions)
│   │   │   ├── 1.md       # Individual exercises (numbered)
│   │   │   ├── _theory.md # Auto-generated theory content
│   │   │   └── data.json  # Topic metadata
│   │   └── challenges/    # Coding challenges (requires difficulty & title)
├── it/                    # Italian exercises (mirrors en/ structure)
├── assets/                # SVG assets for arguments/challenges
│   ├── arguments/
│   └── challenges/
├── cli/                   # Dart CLI for testing run-code exercises
├── parser/                # Dart package for parsing exercise MD files
├── validator/             # Dart package for validating exercises
├── json_creator/          # Generates curriculum.json
├── theory_creator/        # Generates _theory.md files
├── translations/          # Exercise templates by type and language
└── curriculum.json        # Auto-generated curriculum manifest
```

## Exercise Types

Exercises use a frontmatter header with `language` and `exerciseType`:

| Code | Type | Description |
|------|------|-------------|
| 1 | Run Code | User writes code that is executed |
| 2 | Fill Empty Spaces | User fills `[/]` placeholders in code |
| 3 | Choose Answer | User selects from multiple choice answers |
| 4 | Sort Items | User orders code snippets correctly |

## Supported Languages

- `c` (C)
- `dart`
- `javascript`
- `kotlin`
- `python`
- `swift`

## Exercise Structure

Exercises are Markdown files with frontmatter and section tags:

```yaml
---
language: python
exerciseType: 1
difficulty: 1  # Only for challenges (1-3)
title: ...     # Only for challenges
---

# --description--
Theory/explanation text

# --instructions--
What the user should do

# --seed--
Starting code provided to user (for type 2,3,4). In type 2, use [/] as placeholder tokens.

# --answers--
Available answer tokens (type 2: token pool; type 3: multiple choice; type 4: code blocks to sort)

# --before-seed--
Code prepended to solution (for type 1)

# --solutions--
```python
# Solution code (type 4 can have multiple --solutions-- blocks for alternative orderings)
```

# --asserts--
Test assertions with unit tests

```python
assert x == 1
```

# --before-asserts--
Code before unit tests

# --after-asserts--
Code after unit tests

# --output--
Expected stdout output (alternative to asserts)
```

### Section usage by type

| Section | Type 1 | Type 2 | Type 3 | Type 4 |
|---------|--------|--------|--------|--------|
| `--description--` | optional | optional | optional | optional |
| `--instructions--` | required | required | required | required |
| `--seed--` | — | required (use `[/]` per token) | — | — |
| `--answers--` | — | required (token pool) | required (choices) | required (code blocks) |
| `--before-seed--` | optional | — | — | — |
| `--solutions--` | required | required | required | required (multiple = alt orderings) |
| `--asserts--` | required* | — | — | — |
| `--before-asserts--` | optional | — | — | — |
| `--after-asserts--` | optional | — | — | — |
| `--output--` | required* | optional | — | optional |

\* Type 1 requires either `--asserts--` or `--output--`.

## Development Commands

### Run Validator (from validator/ directory)
```sh
# From validator/ directory
dart test lib/validator.dart --chain-stack-traces --fail-fast
```

### Test Run-Code Exercise Locally
```sh
# From repo root
dart run cli/src/cli.dart -p ./en/python/variables/1.md
```

The CLI composes the full executable code (before-seed + solution + after-seed + before-asserts + asserts + after-asserts) and copies it to clipboard for testing in an online IDE like https://ide.judge0.com/.

### Generate curriculum.json
```sh
cd json_creator && dart pub get && dart run lib/json_creator.dart
```

### Generate _theory.md files
```sh
cd theory_creator && dart pub get && dart run lib/theory_creator.dart
```

### Analyze Dart Code
```sh
# In any Dart package directory
dart analyze
```

## Adding New Exercises

1. Use templates from `translations/{lang}/templates/{language}_{type}.md`
2. Place exercise in `{locale}/{language}/{argument}/{number}.md`
3. Number exercises sequentially (1.md, 2.md, 3.md...)
4. For challenges, place in `{locale}/{language}/challenges/{name}.md`
5. Add entry to `data.json` in the argument folder if it's a new argument

### data.json format (argument folder)

Each key is the argument folder name; entries must have `order`, `title`, and `description`:

```json
{
    "variables": {
        "order": 1,
        "title": "Variables",
        "description": "Learn how to store values in a variable"
    }
}
```

6. Add a corresponding SVG asset to `assets/arguments/{argument}.svg` (or `assets/challenges/{name}.svg`)

## Validation Rules

Key validations performed by the GitHub workflow:

- Frontmatter language must match directory structure
- Exercise type must be 1-4
- Challenges require `difficulty` (1-3) and `title`
- Type 1 exercises must have asserts or output
- All exercises must have at least one solution
- Solutions must be valid (type-specific validation)
- Each argument/challenge must have corresponding SVG asset in `assets/`
- Arguments must be declared in parent `data.json`

## GitHub Workflows

- `validate_and_build.yml`: Runs on PR/push to main. Validates exercises, auto-generates curriculum.json and _theory.md files.
- `firebase_storage.yml`: Deploys content to Firebase Storage on push to main.

## Key Packages

- **parser** (`parser/`): Parses exercise Markdown files into `ExerciseModel` using frontmatter and custom tags
- **validator** (`validator/`): Validates exercises against structural rules
- **cli** (`cli/`): Composes executable code from type 1 exercises for local testing
