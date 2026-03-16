# Daily Exercise Generation Pipeline

## Context

Automated daily pipeline that generates new exercises for a language+argument, validates them, translates to all 12 locales, and opens a PR. Designed to be re-run daily.

**Priority:** Dart first, then C, then others.

## Architecture: Pipeline Steps

```
Orchestrator (Opus - main conversation)
  |
  ├─ 1. Read state, pick next language+argument
  ├─ 2. Senior Developer (Sonnet, worktree)  → writes en/ exercises
  ├─ 3. Validator (run locally)              → validates en/ exercises, fix if needed
  ├─ 4. Translator (Haiku ×3, parallel)      → translates to 11 locales
  ├─ 5. Validator again (run locally)         → re-validates all locales
  ├─ 6. Run theory_creator & json_creator    → auto-generate _theory.md + curriculum.json
  └─ 7. Commit, push, open PR
```

## Daily State File

**Path:** `/Users/ale/.claude/projects/-Users-ale-github-codigo-questions/memory/pipeline_state.md`

Tracks completed work so each daily run picks the next argument. Updated after each successful run.

## Priority Queue (Dart first)

Only pick arguments that already have an SVG in `assets/arguments/` OR that the user has provided an SVG for. Current Dart max order is 5.

### Dart arguments queue:
1. `dart/booleans` (order: 6)
2. `dart/arithmeticOperators` (order: 7)
3. `dart/assignmentOperators` (order: 8)
4. `dart/comparisonLogicalOperators` (order: 9)
5. `dart/conditionalStatements` (order: 10)
6. `dart/whileLoops` (order: 11)
7. `dart/forLoops` (order: 12)
8. `dart/lists` (order: 13)
9. `dart/functions` (order: 14)
10. `dart/classes` (order: 15)

All of these have existing SVG assets.

### Dart challenges queue (after arguments are done):
Dart has 12 challenges, Python/JS have 22. These 10 are missing from Dart (all have SVG assets in `assets/challenges/`):
1. `multiples_of_3_or_5` (difficulty: 1)
2. `even_fibonacci_numbers` (difficulty: 1)
3. `largest_prime_factor` (difficulty: 2)
4. `largest_palindrome_product` (difficulty: 2)
5. `smallest_multiple` (difficulty: 2)
6. `sum_square_difference` (difficulty: 1)
7. `10001st_prime` (difficulty: 2)
8. `largest_product_in_a_series` (difficulty: 2)
9. `special_pythagorean_triplet` (difficulty: 2)
10. `summation_of_primes` (difficulty: 2)

Challenges are type 1 only, have `difficulty` (1-3) and `title` in frontmatter, use `--seed--` (function stub), `--asserts--`, `--before-asserts--`, `--after-asserts--`, and `--solutions--`. They test knowledge rather than teach. SVGs are in `assets/challenges/`. Registered in `{locale}/{language}/challenges/data.json`.

### Then C queue, then other languages...

## Exercise Count Per Argument

Varies by argument complexity. Use reference from the same argument in other languages:
- Simple topics (booleans, comments): ~12-15 exercises
- Medium topics (operators, loops): ~15-22 exercises
- Complex topics (conditionalStatements, classes): ~20-25+ exercises

The Senior Developer agent should match the exercise count of the same argument in other languages.

## Step-by-Step Daily Execution

### Step 1: Read state, pick next language+argument
- Read `pipeline_state.md` to find next pending item
- Check SVG exists in `assets/arguments/{argument}.svg`
- Look at exercise count for this argument in other languages as reference

### Step 2: Create worktree
- `git worktree add /tmp/codigo-{language}-{argument} -b feat/{language}-{argument}`

### Step 3: Senior Developer Agent (Sonnet, worktree)
- **Model:** Sonnet
- **Mode:** bypassPermissions

**For arguments (teaching exercises):**
- **Writes:**
  - `en/{language}/{argument}/1.md` through `en/{language}/{argument}/N.md`
  - Updates `en/{language}/data.json` with new argument entry
- **Type distribution:** ~45% type 1, ~25% type 2, ~15% type 3, ~15% type 4
- **Inspiration:** Same argument in other languages + exercism.org + roadmap.sh
- **Must follow:**
  - Templates from `translations/en/templates/{language}_{1,2,3,4}.md`
  - Existing exercise style from `en/{language}/` existing exercises
  - Dart type 1: uses `package:dart_runner/main.dart` + `package:test/test.dart` harness
  - Type 2: `[/]` placeholders with distractor answers
  - Type 4: multiple `--solutions--` blocks for alternative valid orderings
  - First ~5 exercises should have `--description--` sections for theory generation
  - Exercises progress from basic to advanced

**For challenges (knowledge-testing exercises):**
- **Writes:** `en/{language}/challenges/{challenge_name}.md`
- **Updates:** `en/{language}/challenges/data.json` with entry: `{"difficulty": N, "name": "Title"}`
- Always exerciseType 1 with `difficulty` (1-3) and `title` in frontmatter
- Include `--seed--` with function stub, `--description--`, `--instructions--`, `--asserts--`, `--solutions--`
- Use same before-asserts/after-asserts harness as regular type 1
- Reference the same challenge in Python/JS for the problem definition
- Can batch multiple challenges in a single daily run (e.g., 3-5 challenges per PR)

### Step 4: Validate English exercises
- `cd validator && dart pub get && dart test lib/validator.dart --chain-stack-traces --fail-fast`
- On failure: fix the exercise file, retry (max 3 attempts)
- **IMPORTANT:** Always validate en/ before translating to catch errors early

### Step 5: Translator Agents (Haiku ×3, parallel, same worktree)
- **Model:** Haiku
- **Split into 3 parallel agents by locale groups:**
  - Agent 1: de, es, fr, it
  - Agent 2: pt, hi, ja, ko
  - Agent 3: pl, ru, zh
- **Creates:**
  - `{locale}/{language}/{argument}/*.md` for all 11 locales
  - Updates `{locale}/{language}/data.json` for each locale
- **Translation rules:**
  - Translate: `--description--`, `--instructions--`, assert descriptions, prose in `--output--`
  - DO NOT translate: frontmatter, code syntax, variable names, test code, `--err-tN--` markers, section headers
  - Italian special case: variable names in code MAY be translated (e.g., `number` -> `numero`)
  - Type 3: translate choices AND ensure `--solutions--` matches translated correct answer exactly
  - data.json: translate `title` and `description` only, keep key and order identical
- **IMPORTANT:** Do NOT create `_theory.md` files - these are auto-generated in Step 6

### Step 6: Re-validate after translation
- Same validator run as Step 4, now checking all locales
- Fix any issues (usually type 3 solution/answer mismatches in translations)

### Step 7: Auto-generate derived files
- **Run theory_creator:** `cd theory_creator && dart pub get && dart run lib/theory_creator.dart`
  - This auto-generates `_theory.md` files for all locales from exercise `--description--` sections
- **Run json_creator:** `cd json_creator && dart pub get && dart run lib/json_creator.dart`
  - This auto-generates `curriculum.json`

### Step 8: Commit, push, open PR
- Branch: `feat/{language}-{argument}` (e.g., `feat/dart-booleans`)
- Commit all changes (exercises + translations + auto-generated files)
- Push and open PR against main
- Update `pipeline_state.md` with completed entry

## Critical Files

| File | Purpose |
|------|---------|
| `en/dart/data.json` | Dart argument registry (current max order: 5) |
| `translations/en/templates/dart_{1,2,3,4}.md` | Exercise format templates |
| `validator/lib/validator.dart` | Validation rules |
| `validator/lib/constants.dart` | Language-specific boilerplate (Dart uses own harness) |
| `assets/arguments/*.svg` | Required SVG for each argument |
| `{locale}/{language}/data.json` | Must be updated for all 12 locales |
| `theory_creator/lib/theory_creator.dart` | Auto-generates `_theory.md` files |
| `json_creator/lib/json_creator.dart` | Auto-generates `curriculum.json` |

## Reusable Patterns
- Dart type 1 before-asserts: `import 'package:dart_runner/main.dart'; import 'package:test/test.dart'; void main() { group('MainTest -', () {`
- Dart type 1 after-asserts: `}, timeout: Timeout(const Duration(seconds: 1))); }`
- Assert format: `test('testN', () { expect(..., reason: '--err-tN--'); });`
- Type 2 seed: `[/]` tokens, answer pool includes distractors
- Type 4: multiple `--solutions--` blocks for alternative valid orderings

## Verification Checklist
1. Validator passes on en/ exercises (before translation)
2. Validator passes on all locales (after translation)
3. `theory_creator` and `json_creator` run successfully
4. PR CI passes (build_validate.yml)
5. Exercises follow sequential numbering (arguments) or correct naming (challenges)
6. data.json updated in all 12 locales
7. All exercise types represented in new arguments; challenges are type 1 only
8. SVG asset exists in `assets/arguments/` (for arguments) or `assets/challenges/` (for challenges)
