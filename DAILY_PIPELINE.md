# Daily Exercise Generation Pipeline

## Context

Automated daily pipeline that generates new exercises for a language+argument, validates them, translates to all 12 locales, and opens a PR. Designed to be re-run daily. Can process multiple arguments/challenges in parallel.

## Architecture: Pipeline Steps

```
Orchestrator (Opus - main conversation)
  |
  ├─ 1. Read state, pick next language+argument(s)
  ├─ 2. Senior Developer (Sonnet, worktree)  → writes en/ exercises
  ├─ 3. Validator (run locally)              → validates en/ exercises, fix if needed
  ├─ 4. Translator (Sonnet ×3, parallel)     → translates to 11 locales
  ├─ 5. Verify translations (diff check)     → catch files written to wrong dir
  ├─ 6. Validator again (run locally)         → re-validates all locales
  ├─ 7. Run theory_creator & json_creator    → auto-generate _theory.md + curriculum.json
  └─ 8. Commit, push, open PR
```

Multiple arguments can run the full pipeline in parallel (each in its own worktree).

## Daily State File

**Path:** `/Users/ale/.claude/projects/-Users-ale-github-codigo-questions/memory/pipeline_state.md`

Tracks completed work so each daily run picks the next pending item.

## Icon Assets

**Available icons:** `/Users/ale/Downloads/icon/*.svg`
**Already used:** `/Users/ale/Downloads/icon/FATTE/`

When adding a new argument/challenge that doesn't have an SVG in `assets/`, pick the most appropriate icon from `/Users/ale/Downloads/icon/` and copy it to `assets/arguments/{name}.svg` or `assets/challenges/{name}.svg`.

## Progress Tracker

### COMPLETED:
- **Dart:** 15 arguments + 22 challenges (COMPLETE)
- **All 6 languages:** 22 challenges each (COMPLETE)

### Remaining Gaps by Language:

#### Kotlin (11 args → needs ~4-5 more):
1. `kotlin/assignmentOperators` - SVG exists
2. `kotlin/functions` - SVG exists
3. `kotlin/classes` - SVG exists
4. `kotlin/arrays` or `kotlin/maps` - SVG exists for arrays
5. `kotlin/strings` - SVG exists

#### JavaScript (14 args → needs ~1-2 more):
1. `javascript/strings` - SVG exists

#### C (12 args → could add):
1. `c/strings` - SVG exists (char arrays, strlen, strcmp, etc.)

#### Swift (15 args - already complete, could add more niche topics)

#### Python (15 args - already complete, could add more niche topics)

## Project Euler Challenges (Standard Set)

All 6 languages now share the same 22 challenges. The 10 Project Euler challenges are:

| # | Challenge | Difficulty | Description |
|---|-----------|-----------|-------------|
| 1 | `multiples_of_3_or_5` | 1 | Sum of multiples of 3 or 5 below N |
| 2 | `even_fibonacci_numbers` | 1 | Sum of even Fibonacci terms ≤ N |
| 3 | `largest_prime_factor` | 2 | Largest prime factor of N |
| 4 | `largest_palindrome_product` | 2 | Largest palindrome from product of two N-digit numbers |
| 5 | `smallest_multiple` | 2 | Smallest number divisible by all 1..N |
| 6 | `sum_square_difference` | 1 | Difference between square of sum and sum of squares |
| 7 | `10001st_prime` | 2 | Nth prime number |
| 8 | `largest_product_in_a_series` | 2 | N adjacent digits with greatest product in 1000-digit number |
| 9 | `special_pythagorean_triplet` | 2 | Product abc where a²+b²=c² and a+b+c=N |
| 10 | `summation_of_primes` | 2 | Sum of all primes below N |

### Language-specific challenge harness patterns:

| Language | Before-seed | Assert pattern | After-asserts |
|----------|------------|----------------|---------------|
| Dart | (none, uses --before-asserts--) | `expect(fn(x), y, reason: '--err-tN--')` | Timeout wrapper |
| C | CException framework + try_catch | `try_catch(fn(x) == y)` | printf summary + return 0 |
| Python | unittest.TestCase | `self.assertEqual(fn(x), y, "--err-tN--")` | unittest.main() |
| JavaScript | tryCatch helper | `tryCatch(fn(x) === y)` | console.log summary |
| Kotlin | tryCatch helper + fun main() | `tryCatch(fn(x) == y)` | println summary |
| Swift | XCTest + CodigoTests | `XCTAssertEqual(fn(x), y, "--err-tN--")` | allTests + XCTMain |

## Exercise Count Per Argument

Varies by argument complexity. Use reference from the same argument in other languages:
- Simple topics (booleans, comments): ~12-15 exercises
- Medium topics (operators, loops): ~15-22 exercises
- Complex topics (conditionalStatements, classes): ~20-25+ exercises

## Step-by-Step Daily Execution

### Step 1: Read state, pick next language+argument
- Read `pipeline_state.md` to find next pending item
- Check SVG exists in `assets/arguments/{argument}.svg` or copy from `/Users/ale/Downloads/icon/`
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
- **Must follow:**
  - Templates from `translations/en/templates/{language}_{1,2,3,4}.md`
  - Existing exercise style from `en/{language}/` existing exercises
  - Type 2: `[/]` placeholders with distractor answers, `- ` prefixed
  - Type 3: answers and solutions `- ` prefixed, solution EXACTLY matches one answer
  - Type 4: multiple `--solutions--` blocks for alternative valid orderings
  - First ~5 exercises should have `--description--` sections for theory generation
  - Exercises progress from basic to advanced

**For challenges (Project Euler / coding challenges):**
- **Writes:** `en/{language}/challenges/{challenge_name}.md`
- **Updates:** `en/{language}/challenges/data.json`
- Always exerciseType 1 with `difficulty` (1-3) and `title` in frontmatter
- Include `--seed--` (function stub), `--description--`, `--instructions--`, `--asserts--`, `--solutions--`
- Use language-specific test harness (see table above)
- Reference the same challenge in Python/JS for the problem definition
- Can batch multiple challenges per PR

### Step 4: Validate English exercises
- `cd validator && dart pub get && dart test lib/validator.dart --chain-stack-traces --fail-fast`
- On failure: fix the exercise file, retry (max 3 attempts)
- **IMPORTANT:** Always validate en/ before translating

### Step 5: Translator Agents (Sonnet ×3, parallel, same worktree)
- **Model:** Sonnet (not Haiku — Haiku skips exercises)
- **Split into 3 parallel agents:**
  - Agent 1: de, es, fr, it
  - Agent 2: pt, hi, ja, ko
  - Agent 3: pl, ru, zh
- **Translation rules:**
  - Translate: `--description--`, `--instructions--`, assert descriptions, prose in `--output--`
  - DO NOT translate: frontmatter, code syntax, variable names, test code, `--err-tN--` markers, section headers
  - **CRITICAL:** Translate COMPLETE sentences — no English words like "The", "A", "In" left
  - Type 3: translate choices AND ensure `--solutions--` matches translated correct answer exactly
  - data.json: translate `title`/`description`/`name` only
- **IMPORTANT:** Do NOT create `_theory.md` files

### Step 6: Verify translations
- **Diff check:** Compare every translated file against English — if identical, it wasn't translated
```bash
for i in $(seq 1 N); do for locale in de es fr it hi ja ko pl pt ru zh; do
  if diff -q en/{lang}/{arg}/$i.md $locale/{lang}/{arg}/$i.md > /dev/null 2>&1; then
    echo "UNTRANSLATED: $locale/$i.md"; fi; done; done
```
- **Check main for stray files:** `git status` on main — translator agents sometimes write to main repo instead of worktree. If found, stash → checkout branch → pop → commit.

### Step 7: Re-validate after translation
- Same validator run, now checking all locales

### Step 8: Auto-generate derived files
- **theory_creator:** `cd theory_creator && dart pub get && dart run lib/theory_creator.dart`
- **json_creator:** `cd json_creator && dart pub get && dart run lib/json_creator.dart`

### Step 9: Commit, push, open PR
- Branch: `feat/{language}-{argument}` or `feat/{language}-challenges`
- Commit all changes
- Push and open PR
- Update `pipeline_state.md`

## Critical Files

| File | Purpose |
|------|---------|
| `en/{language}/data.json` | Argument registry per language |
| `en/{language}/challenges/data.json` | Challenge registry per language |
| `translations/en/templates/{language}_{1,2,3,4}.md` | Exercise format templates |
| `validator/lib/validator.dart` | Validation rules |
| `validator/lib/constants.dart` | Language-specific test harness boilerplate |
| `assets/arguments/*.svg` | Required SVG for each argument |
| `assets/challenges/*.svg` | Required SVG for each challenge |
| `/Users/ale/Downloads/icon/*.svg` | Available icons for new arguments |
| `theory_creator/lib/theory_creator.dart` | Auto-generates `_theory.md` |
| `json_creator/lib/json_creator.dart` | Auto-generates `curriculum.json` |

## Verification Checklist
1. Validator passes on en/ exercises (before translation)
2. Diff check: 0 files identical to English
3. `git status` on main: no stray files
4. Validator passes on all locales (after translation)
5. `theory_creator` and `json_creator` run successfully
6. data.json updated in all 12 locales
7. SVG asset exists
8. PR CI passes
