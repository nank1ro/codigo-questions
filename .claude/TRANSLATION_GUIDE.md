# Translation Guide for Codigo Exercises

This guide documents the process and lessons learned for translating exercises to new languages. Use this as a reference when adding new locales (e.g., `fr`, `de`, `pt`, etc.).

## Overview

Translate all exercises from `en/` to a new locale folder (e.g., `{locale}/`, `fr/`).

## Setup
1. Add `'{locale}'` to the `locales` list in these 3 files:
   - `validator/lib/validator.dart`
   - `json_creator/lib/json_creator.dart`
   - `theory_creator/lib/theory_creator.dart`
   - e.g., change `['en', 'it', 'es']` → `['en', 'it', 'es', 'de']`
2. Copy `en/` to `{locale}/` (e.g., `cp -r en/ fr/`)
3. Use parallel Haiku agents (one per folder) for translation

## Scope

### Languages to Translate (6 total)
- C (251 exercises)
- Dart (103 exercises)
- JavaScript (291 exercises)
- Kotlin (301 exercises)
- Python (318 exercises)
- Swift (306 exercises)

### Exercise Types
| Type | Count | Translation Scope |
|------|-------|-------------------|
| Type 1 (Run Code) | 193 | description, instructions, assertion comments |
| Type 2 (Fill Spaces) | 842 | description, instructions, text answers (PRESERVE trailing spaces!) |
| Type 3 (Multiple Choice) | 503 | instructions (question text), text answer options |
| Type 4 (Sort Code) | 32 | instructions only |

### What Gets Translated
- `--description--` section
- `--instructions--` section
- `--answers--` section (text portions only, not code)
- Comments/descriptions within `--asserts--`
- `data.json` files (`title` and `description` fields)

### What Stays in English
- All code inside backticks or code blocks
- Frontmatter fields: `language`, `exerciseType`, `difficulty`
- Challenge `title` frontmatter **must be translated** (e.g., `Leap Year` → `Año bisiesto`). Exception: proper names/acronyms that don't translate (`ATM`, `FizzBuzz`, `Hello World!`)
- `--seed--` code (except comments if any)
- `--solutions--` code
- `--output--` values
- `--before-seed--`, `--before-asserts--`, `--after-asserts--` code

## Implementation Strategy

### Step 1: Setup
```bash
cp -r en/ {locale}/
```

### Step 2: Batch Translation with Haiku Agents (Per Folder)

**IMPORTANT: Token Limit Lesson Learned**
- Haiku agents have limited context (~30k tokens)
- Do NOT assign entire languages to a single agent - they will hit token limits
- Instead, spawn **one agent per argument folder** (e.g., `{locale}/python/variabl{locale}/`)
- Each folder typically has 10-25 files, which fits within agent limits

**Recommended Approach:**
1. Spawn agents per folder, not per language
2. Run multiple folder agents in parallel (up to 10-15 at a time)
3. After each batch completes, check progress and spawn agents for remaining folders
4. Repeat until all folders are translated

**Example agent spawn pattern:**
```
Agent 1: {locale}/python/variabl{locale}/ (24 files)
Agent 2: {locale}/python/output/ (10 files)
Agent 3: {locale}/javascript/arrays/ (14 files)
... etc
```

Each agent will:
- Process all exercises in its assigned folder
- Skip files that already contain target language text
- Skip `_theory.md` files (auto-generated)
- Preserve trailing spaces in Type 2 answers

### Step 3: Validation
Run validator after each batch:
```bash
cd validator && dart test lib/validator.dart --chain-stack-traces --fail-fast
```

## Progress Tracking

Optionally track progress in `{locale}/.translation-progress.json`.

## Critical Rules for Agents

1. **PRESERVE LEADING/TRAILING SPACES** in Type 2 answers - critical for exercise completion
   - Example: `- if ` must stay as `- if ` (with trailing space)
   - Example: ` - elif ` must stay as ` - elif ` (with leading and trailing space)
2. Keep ALL code in backticks or code blocks untranslated
3. Skip `_theory.md` files (auto-generated)
4. Translate `data.json` files (`title` and `description` fields for argument folders; `name` field for challenge folders)
   - Challenge `name` in `data.json` MUST match the `title` frontmatter in the corresponding `.md` file exactly
   - Use the canonical Spanish challenge names table below (see "Canonical Challenge Names")
5. In `--asserts--` section: translate only the text description before the code block, NOT the code itself
6. Preserve exact markdown formatting and structure
7. **DO NOT translate programming keywords in `--answers--`** - C/Python/etc keywords like `if`, `else`, `true`, `false` must stay in English
8. **For Type 3 (Multiple Choice): Solutions MUST match translated answers EXACTLY**
   - If you translate the answers to target language, the solution must also be the target language version
   - Example: If answer is "El primero es una cadena", solution must be "- [Translated answer text]" (not English)
9. **For Type 2 (Fill Spaces): Copy `--answers--` section EXACTLY from English file**
   - The answers contain code tokens that cannot be translated
   - Trailing spaces are critical for the validator to work

## Verification

After all translations complete:
```bash
cd validator && dart test lib/validator.dart --chain-stack-traces --fail-fast
```

## Files to Modify

- Copy `en/` to `{locale}/`
- Translate all `.md` exercise files in `{locale}/{language}/{argument}/` (excluding `_theory.md`)
- Translate all `data.json` files in `{locale}/{language}/`

## Execution Order

1. Add `'{locale}'` to `locales` in `validator/lib/validator.dart`, `json_creator/lib/json_creator.dart`, `theory_creator/lib/theory_creator.dart`
2. Copy `en/` folder to `{locale}/`
3. Spawn Haiku agents per folder (not per language) - run 10-15 in parallel
4. Check progress after batch completes
5. Spawn new agents for any remaining untranslated folders
6. Repeat steps 4-5 until 100% translated
7. Run validator to verify all translations
8. Fix any validation errors if found

## Lessons Learned

### Token Limits
- **Problem**: Assigning an entire language (250-300 files) to a single Haiku agent causes it to hit context limits before finishing
- **Solution**: Spawn agents per argument folder (10-25 files each) instead of per language
- **Detection**: Check agent output file sizes - if they're small (129B), agent completed (possibly prematurely)
- **Recovery**: Re-check translation progress, spawn new agents for remaining files

### Auto-Recovery Protocol (IMPORTANT)
When agents complete (output file = 129B), Claude should AUTOMATICALLY:
1. Check translation progress immediately
2. Identify remaining untranslated fil{locale}/folders
3. Spawn new targeted agents without waiting for user prompt
4. Continue this cycle until 100% completion

**DO NOT** wait for user to ask "check progress" or "spawn more agents" - this should be self-managing.

The workflow is:
```
spawn agents → wait for completion → check 129B → check remaining → spawn more → repeat
```

This loop should continue autonomously until all files are translated.

### Automatic Agent Monitoring & Respawn System

**Active Monitoring Loop:**
Every 3-5 minutes, run this check automatically:
```bash
# Check if agents completed (129B = done)
for agent_id in $AGENT_IDS; do
  size=$(stat -f%z "/private/tmp/claude-501/.../tasks/$agent_id.output" 2>/dev/null)
  if [ "$size" = "129" ]; then
    echo "Agent $agent_id completed"
  fi
done

# Check translation progress
for lang in c dart javascript kotlin python swift; do
  total=$(find {locale}/$lang -name "*.md" ! -name "_theory.md" | wc -l)
  translated=$(find {locale}/$lang -name "*.md" ! -name "_theory.md" -exec grep -l "{locale}-specific-pattern" {} \; | wc -l)
  remaining=$((total - translated))
  echo "$lang: $remaining remaining"
done
```

**Automatic Respawn Rules:**
1. When ALL current agents show 129B output → immediately check remaining files
2. If remaining files > 0 → spawn new agents for incomplete folders
3. Prioritize largest folders first (conditionalStatements, whileLoops, etc.)
4. Spawn 10-15 agents per batch to maximize parallelism
5. Each agent handles ~10-20 files max to avoid token limits

**Agent ID Tracking:**
Keep track of current agent IDs to monitor:
```
CURRENT_AGENTS="agent1 agent2 agent3..."
```

**Completion Criteria:**
- Total translated = 1570 files
- All 6 languages at 100%
- Then run validator to verify

### Progress Checking
Use this command to check translation status:
```bash
for lang in c dart javascript kotlin python swift; do
  total=$(find {locale}/$lang -name "*.md" ! -name "_theory.md" | wc -l)
  translated=$(find {locale}/$lang -name "*.md" ! -name "_theory.md" -exec grep -l "{locale}-specific-pattern" {} \; | wc -l)
  echo "$lang: $translated/$total"
done
```

### Batch System for Large Translation Tasks

When translating large numbers of files:

1. **First Pass**: Spawn agents per folder (10-15 agents in parallel)
2. **Monitor**: Wait for agents to complete, check progress
3. **Second Pass**: Identify remaining untranslated files per folder
4. **Targeted Cleanup**: Spawn new agents specifically for folders with remaining files
5. **Repeat** until 100% complete

**Why this works better:**
- Smaller batches = agents complete successfully within token limits
- Parallel execution = faster overall translation
- Progress checking between batches = early detection of issues
- Targeted cleanup passes = efficient use of agent resources

**Folder size guidelines:**
- <15 files: Single agent can handle
- 15-30 files: May need 2 passes
- >30 files: Split into multiple agents or expect multiple passes

### Solution/Answer Matching Issues (Type 3 Exercises)

**Problem**: When translating Type 3 (multiple choice) exercises, agents translated the answers but left the solution in English. The validator requires the solution to exactly match one of the answers.

**Solution**: For Type 3 exercises:
1. Translate the answers to target language
2. The `--solutions--` section must contain the EXACT target language translation of the correct answer
3. Example:
   ```markdown
   # --answers--
   - [Translated answer text]    ← Translated to target language
   - [Another translated answer]

   # --solutions--
   - [Translated answer text]    ← Must match answer EXACTLY
   ```

**Detection**: Run validator - errors like "The exercise cannot be completed successfully with the solutions provided" indicate this issue.

**Fix Command**: For each failing file, copy the correct target language answer to the solutions section.

### Type 2 Answer Preservation Issues

**Problem**: Type 2 (fill spaces) exercises have answers that are code tokens (like `if `, `else `, `==`). These were incorrectly translated to target language (e.g., `si`, `sino` in Spanish), breaking the exercises.

**Solution**: For Type 2 exercises:
1. **DO NOT translate the `--answers--` section** - copy it exactly from the English file
2. These are code tokens, not text to translate
3. Trailing spaces in answers are critical - they become part of the reconstructed code
4. Use this Python script to fix:
   ```python
   # Copy exact answers from English to target language
   import re
   with open(en_file, 'r') as f: en_content = f.read()
   with open(es_file, 'r') as f: es_content = f.read()
   en_answers = re.search(r'(# --answers--\n\n.*?)(\n\n# --solutions--|$)', en_content, re.DOTALL).group(1)
   es_content = re.sub(r'# --answers--\n\n.*?(\n\n# --solutions--|$)', en_answers + r'\1', es_content, flags=re.DOTALL)
   with open(es_file, 'w') as f: f.write(es_content)
   ```

**Detection**: Validator errors like "There are more answers than possibilities" or "Failed assertion: answersCount <= possibleAnswers.length" indicate translated code tokens.

## Canonical Challenge Names (Spanish)

The `title` in challenge `.md` frontmatter and the `name` in `challenges/data.json` **must match exactly**. Example table:

| Key | English | Spanish |
|-----|---------|---------|
| `100_doors` | 100 doors | 100 puertas |
| `10001st_prime` | 10001st prime | Número primo 10001 |
| `ackermann_function` | Ackermann function | Función de Ackermann |
| `addition` | Addition | Adición |
| `arithmetic_mean` | Arithmetic mean | Media aritmética |
| `atm` | ATM | ATM *(acronym, kept — known in Spanish)* |
| `even_fibonacci_numbers` | Even Fibonacci numbers | Números pares de Fibonacci |
| `fizz_buzz` | FizzBuzz | FizzBuzz *(proper name, kept)* |
| `hello_world` | Hello World! | ¡Hola Mundo! |
| `largest_palindrome_product` | Largest palindrome product | Mayor producto palíndromo |
| `largest_prime_factor` | Largest prime factor | Factor primo más grande |
| `largest_product_in_a_series` | Largest product in a series | Mayor producto de una serie |
| `leap_year` | Leap Year | Año bisiesto |
| `multiples_of_3_or_5` | Multiples of 3 or 5 | Múltiplos de 3 o 5 |
| `raindrops` | Raindrops | Gotas de lluvia |
| `roman_numeral_converter` | Roman Numeral Converter | Convertidor de números romanos |
| `smallest_multiple` | Smallest multiple | Múltiplo más pequeño |
| `special_pythagorean_triplet` | Special pythagorean triplet | Tripleta pitagórica especial |
| `sum_digits` | Sum of digits | Suma de dígitos |
| `sum_square_difference` | Sum square difference | Diferencia de suma cuadrada |
| `summation_of_primes` | Summation of primes | Suma de números primos |
| `two_for_one` | Two for one | Dos por uno |

### Acronym / Proper Name Rule
Keep untranslated if the term is **universally recognized as-is** in the target language:
- `ATM` → keep (used in Spanish-speaking countries)
- `FizzBuzz` → keep (programming challenge proper name)
- `Hello World!` → translate (e.g., `¡Hola Mundo!`)

When in doubt, translate.
