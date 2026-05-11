# tester

Local-only CLI that compiles and runs every exercise's canonical solution
through the production `codecompiler` service, then judges pass/fail.
Catches exercises that look fine to the static validator but break at
compile-time or test-runtime when fed their `.md`'s `--solutions--` block.

**Not wired into CI.** Run it manually before merging curriculum changes.

## Quick start (TL;DR)

If everything is set up already (see "First-time setup" below):

```sh
# 1. start codecompiler (one terminal)
cd /Users/ale/github/codecompiler
HTTP_SERVER_PORT=8080 go run ./cmd/httpserver

# 2. run the sweep (another terminal)
cd /path/to/codigo-questions/tester
dart run bin/tester.dart -p 'en/**/*.md' -t 1
```

The first dart submission takes ~6s (codecompiler initialises `dart_runner/`);
subsequent ones are ~1s. A full 255-exercise sweep runs in roughly 5 minutes.

## First-time setup

You need: Go ≥1.22, Dart, Python 3, Node, Kotlin, Swift, gcc/clang, and a
working `codecompiler` checkout with a populated `.env` (Firebase
credentials).

1. **Install missing language toolchains.** Codecompiler shells out to each.
   On macOS:

   ```sh
   brew install kotlin           # only one most likely missing
   # dart, python3, node, swift, gcc already present on dev macOS
   ```

   Verify all are on `$PATH`: `kotlinc -version`, `node -v`, `swift -v`,
   `python3 -V`, `dart --version`, `gcc -v`. If any is missing the
   corresponding exercises will report `RUNTIME-ERROR`.

2. **Get codecompiler working locally** (`/Users/ale/github/codecompiler`):

   - The Docker `make build` flow is currently broken on Apple Silicon
     (Dart's Debian repo doesn't have `arm64` packages). Don't bother —
     run it as a native Go binary instead.
   - codecompiler's hardcoded `/usr/bin/node` doesn't exist on macOS;
     `pkg/languages/javascript10.19.0.go::Path()` has been patched locally
     to return `"node"` (PATH-resolved). Keep that patch.
   - codecompiler reads `.env` from its CWD, so always start it from
     `/Users/ale/github/codecompiler`.

3. **Configure `tester/.env`.** Copy the template and paste in the Firebase
   API key from `codecompiler/.env`:

   ```sh
   cp tester/.env.template tester/.env
   # then edit FIREBASE_API_KEY
   ```

   Defaults for `CODECOMPILER_URL` and `FIREBASE_DATABASE_URL` are correct
   if codecompiler runs on `:8080` and writes to the production RTDB.

4. **Fetch tester deps:**

   ```sh
   cd tester
   dart pub get
   ```

## Common invocations

```sh
# Smoke-test one exercise
dart run bin/tester.dart -p en/dart/booleans/8.md

# All type-1 exercises in one language (incl. challenges)
dart run bin/tester.dart -p 'en/dart/**/*.md' -t 1

# All type-1 exercises across all languages (~5 min)
dart run bin/tester.dart -p 'en/**/*.md' -t 1

# Stop at first failure
dart run bin/tester.dart -p 'en/c/**/*.md' -t 1 --fail-fast

# JSON output for tooling
dart run bin/tester.dart -p 'en/**/*.md' -t 1 --report json > results.json
# progress lines go to stderr; JSON array is on stdout
```

## Flag reference

| Flag | Meaning |
|------|---------|
| `-p, --path <glob>` | Path or glob, relative to repo root. Default: `en/dart/**/*.md`. |
| `-l, --language <lang>` | Filter by frontmatter `language`. |
| `-t, --type <n>` | Filter by `exerciseType`. Only type 1 is executed. |
| `--fail-fast` | Stop on first failure. |
| `--timeout <sec>` | Per-exercise RTDB poll ceiling. Default 30; use 60 for slower exercises. |
| `--report json` | Emit JSON on stdout (progress still on stderr). |

## What the verdicts mean

| Verdict | Meaning |
|---------|---------|
| `PASS` | Exit 0, all asserts pass (or stdout matches `--output--`). |
| `FAIL` | One or more `--err-tN--` markers in stdout, or `--output--` mismatch. The exercise's canonical solution is wrong. |
| `COMPILE-ERROR` | Dart/Swift/Kotlin couldn't parse the composed code. The exercise is structurally broken (e.g., asks the user to write a bare statement at file top-level). |
| `RUNTIME-ERROR` | Non-zero exit code without test markers. Usually a missing include, undeclared identifier, or env-specific failure (e.g., Swift on macOS can't find `XCTest`). |
| `SKIP` | exerciseType ≠ 1, unsupported language, or file is `_theory.md`. |

## Scope

- **Only `exerciseType: 1` is executed.** Other types are pure structural
  checks already covered by `validator/lib/validator.dart`.
- **Only one locale per exercise.** Solutions/asserts are identical across
  the 12 locales — running each one twelve times yields no extra coverage.
- **Sequential.** codecompiler serialises submissions internally via a
  global mutex, so parallelism would only queue requests.

## Troubleshooting

| Symptom | Cause / fix |
|---------|-------------|
| `Submit failed: Connection refused (localhost:8080)` | codecompiler isn't running or crashed. Check `/tmp/cc.log` (or wherever you redirected its output). |
| `panic: unexpected error obtaining the Firebase Auth client` | codecompiler started from the wrong CWD (no `.env` found). Always `cd /Users/ale/github/codecompiler` first. |
| `FIREBASE_API_KEY is required` | Copy `tester/.env.template` to `tester/.env`. |
| `Submission timed out after 60s` | The exercise's solution loops forever, or codecompiler crashed mid-submission and the result never reached RTDB. Restart codecompiler. |
| `RUNTIME-ERROR` for every Swift exercise | `swift Main.swift` on macOS can't find `XCTest`. This is a host-environment limitation, not a curriculum bug. |
| `RUNTIME-ERROR` for every Kotlin exercise | `kotlinc` isn't installed. `brew install kotlin`. |
