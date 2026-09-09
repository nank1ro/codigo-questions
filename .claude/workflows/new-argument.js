export const meta = {
  name: 'new-argument',
  description: 'Author a new exercise argument (or challenge set) for one language, review it, translate to 11 locales, verify with validator+tester, open a PR',
  whenToUse: 'Pass args: [{language, argument, title, description, count, assetFrom?, notes?}, ...]. One item per topic; items run in parallel, each in its own worktree /tmp/codigo-new/<language>-<argument>. Requires codecompiler on localhost:8080 and tester/.env in the main checkout.',
  phases: [
    { title: 'Write', detail: 'author en exercises + data.json in a fresh worktree' },
    { title: 'Review', detail: 'independent content review (ambiguity, pedagogy, facts)' },
    { title: 'Fix', detail: 'apply confirmed findings' },
    { title: 'Translate', detail: '3 locale groups, Sonnet' },
    { title: 'Verify', detail: 'validator, tester, output/locale checks, regenerate' },
    { title: 'Ship', detail: 'commit, push, open PR' },
  ],
}

// ---------------------------------------------------------------------------
// Inputs. `args` is an array of topic specs (or one spec). All fields except
// notes/assetFrom are required.
//   language   c | dart | javascript | kotlin | python | swift
//   argument   folder name, must match assets/arguments/<argument>.svg (or set assetFrom
//              to an existing asset name to copy, e.g. assetFrom: 'dictionaries')
//   title      display title for data.json (e.g. "Maps")
//   description one-line description for data.json
//   count      number of exercises to write (12-25)
//   notes      optional extra guidance for the author (scope, must-cover concepts)
// ---------------------------------------------------------------------------
const SPECS = (Array.isArray(args) ? args : [args]).filter(Boolean)
if (!SPECS.length) throw new Error('new-argument: pass args as an array of {language, argument, title, description, count}')

const MAIN = '/Users/ale/.t3/worktrees/codigo-questions/t3code-3441c85c'
const LOCALE_GROUPS = [['de', 'es', 'fr', 'it'], ['pt', 'pl', 'ru', 'zh'], ['ja', 'ko', 'hi']]

const FORMAT_RULES = `
Exercise format: read CLAUDE.md in the worktree root. Key rules:
- Sections: '# --description--', '# --instructions--', '# --seed--', '# --answers--', '# --before-seed--', '# --after-seed--', '# --before-asserts--', '# --asserts--', '# --after-asserts--', '# --solutions--', '# --output--'.
- Type 1 (run code): use the language harness EXACTLY as in existing type-1 exercises of the same language (copy the '# --before-seed--' / '# --after-asserts--' blocks from a neighbour; see validator/lib/constants.dart). Dart type-1 uses --before-asserts--/--asserts--/--after-asserts-- with package:test and wraps user code that must expose values in a result() function (see en/dart/assignmentOperators/10.md). Kotlin type-1 puts user code inside fun main() via the before-seed; anything that must be top-level (classes with companion objects, objects) needs the harness main moved to '# --before-asserts--' (see en/kotlin/classes/7.md). Swift uses the tryCatch helper, never XCTest.
- Type 2 (fill spaces): '[/]' placeholders in the seed; '# --answers--' is a '- token' list with distractors; the instructions plus the stated '# --output--' must make exactly ONE token per slot valid (a distractor that also compiles and prints the same output is a defect).
- Type 3 (choose answer): '- text' answers; the '# --solutions--' entry must match one answer EXACTLY; only one answer may be defensible.
- Type 4 (sort items): one fenced block per row in '# --answers--'; '# --solutions--' holds ONE fenced block with the whole program (rows joined by newlines); extra fenced blocks in the same section are alternative valid orderings. If several top-level orderings are valid, either list them all or constrain the instructions ("define the function before main").
- '# --output--' for type 2/4 must be exactly what the solution prints.
- Every concept an exercise uses must be introduced in a '# --description--' of that exercise or an earlier one in the same folder (descriptions are concatenated into _theory.md, which only includes the leading run of consecutive exercises that have descriptions, so give the first ~5 exercises descriptions and any later exercise that introduces something new).
- Mix: roughly 45% type 1, 25% type 2, 15% type 3, 15% type 4; progress from basic to advanced; short, concrete instructions; code must compile and run on the production codecompiler versions: C = GCC 13.3.0 (C11/C17), Dart 3.13.3 (null safety), JavaScript = Node.js 26.8.1, Kotlin 2.4.20 on Java 17 (JVM 17 APIs only), Python 3.14.7, Swift 6.3.3 (Swift 6 language mode: strict concurrency, so avoid global mutable state accessed from closures that trip Sendable checks). Target exactly these versions (production is being upgraded to them); never use anything deprecated or removed there, and do not lean on features newer than these.`

const CHECKS = (s) => `
Checks (run from the worktree root; the production-version codecompiler Docker container must be running: 'docker start codecompiler-8081' (image codecompiler:main, built from the codecompiler repo main branch with GCC 13.3.0, Dart 3.13.3, Node 26.8.1, Kotlin 2.4.20/Java 17, Python 3.14.7, Swift 6.3.3) and tester/.env must contain CODECOMPILER_URL=http://localhost:8081/hereford_rpc; never test against a host-native server):
  cp ${MAIN}/tester/.env tester/.env
  for d in validator tester json_creator theory_creator; do (cd $d && dart pub get >/dev/null); done
  (cd validator && dart test lib/validator.dart --reporter=failures-only --chain-stack-traces --fail-fast 2>&1 | tail -20)
  (cd tester && dart run bin/tester.dart -p 'en/${s.language}/${s.argument}/*.md' -t 1 2>&1 | tail -40)
  scripts/check_outputs_docker.sh 'en/${s.language}/${s.argument}/*.md'   # runs check_outputs.py inside the codecompiler-8081 container so type-2/4 outputs use the production toolchains
  python3 scripts/check_locales.py WORKTREE`

const WRITE_SCHEMA = {
  type: 'object',
  properties: {
    worktree: { type: 'string' },
    files: { type: 'array', items: { type: 'string' } },
    typeMix: { type: 'string' },
    notes: { type: 'string' },
  },
  required: ['worktree', 'files', 'typeMix', 'notes'],
}
const FINDINGS_SCHEMA = {
  type: 'object',
  properties: {
    findings: { type: 'array', items: { type: 'object', properties: { file: { type: 'string' }, defect: { type: 'string' }, fix: { type: 'string' } }, required: ['file', 'defect', 'fix'] } },
  },
  required: ['findings'],
}
const REPORT_SCHEMA = {
  type: 'object',
  properties: {
    validator: { type: 'string', enum: ['pass', 'fail'] },
    tester: { type: 'string' },
    outputs: { type: 'string' },
    locales: { type: 'string' },
    fixesApplied: { type: 'array', items: { type: 'string' } },
    remainingProblems: { type: 'array', items: { type: 'string' } },
  },
  required: ['validator', 'tester', 'outputs', 'locales', 'fixesApplied', 'remainingProblems'],
}
const SHIP_SCHEMA = {
  type: 'object',
  properties: { branch: { type: 'string' }, commit: { type: 'string' }, prUrl: { type: 'string' }, notes: { type: 'string' } },
  required: ['branch', 'commit', 'prUrl', 'notes'],
}

const wt = (s) => `/tmp/codigo-new/${s.language}-${s.argument}`
const branch = (s) => `feat/${s.language}-${s.argument}`

function writePrompt(s) {
  return `You are a senior ${s.language} educator writing a new exercise argument for the Codigo app.

SETUP (exactly):
  cd ${MAIN} && git fetch -q origin && mkdir -p /tmp/codigo-new && git worktree add ${wt(s)} -b ${branch(s)} origin/main
  cd ${wt(s)}
Work ONLY inside ${wt(s)}. Do NOT commit, push, stash, checkout or touch other worktrees.

TOPIC: language=${s.language}, argument folder=en/${s.language}/${s.argument}/, title="${s.title}", description="${s.description}", exercises to write: ${s.count}.
${s.notes ? 'Author notes: ' + s.notes : ''}

Before writing, study: translations/en/templates/${s.language}_{1,2,3,4}.md; three existing arguments of this language (e.g. the most recent folders in en/${s.language}/) for tone, harness and difficulty curve; the same topic in another language if it exists (e.g. en/python/${s.argument}, en/swift/${s.argument}); and en/${s.language}/data.json for the order values.
${FORMAT_RULES}

Deliverables:
1. en/${s.language}/${s.argument}/1.md ... ${s.count}.md
2. en/${s.language}/data.json: add "${s.argument}": {"order": <max existing order + 1>, "title": "${s.title}", "description": "${s.description}"}
3. assets/arguments/${s.argument}.svg must exist. ${s.assetFrom ? `It does not: copy assets/arguments/${s.assetFrom}.svg to assets/arguments/${s.argument}.svg.` : 'It should already exist; if not, stop and say so in notes.'}
Do NOT create _theory.md (generated later).
${CHECKS(s)}
Iterate until validator passes, every type-1 exercise PASSes in the tester, check_outputs reports 0 failed, and check_locales reports only MISSING lines for the 11 other locales (they are translated later). Return worktree, the list of files, the type mix, and notes.`
}

function reviewPrompt(s) {
  return `You are an independent reviewer of new coding exercises. Read-only: do not modify files, do not run git commands that change state. Files: ${wt(s)}/en/${s.language}/${s.argument}/*.md (numbered, read in order) plus ${wt(s)}/CLAUDE.md for the format.

Report ONLY actual defects, each with file path, the defect, and a one-line fix:
- Factually wrong statements about ${s.language}.
- Type 3: more than one defensible answer, or the solution text does not exactly match an answer.
- Type 2: a distractor token would also make the code valid AND match the stated --output--; or the instructions do not determine the answer uniquely.
- Type 4: more than one valid ordering while only one is listed and the instructions do not constrain order.
- --output-- that does not match what the solution prints.
- Instructions inconsistent with seed/solution (names, values); asserts that pass without doing what the instructions ask (e.g. inheritance never checked).
- A concept used before any earlier/same exercise description introduces it.
- Harness mistakes: Dart type-1 not using result()/expect pattern where values are checked; Kotlin top-level-only constructs inside main; Swift XCTest; missing --err-tN-- markers.
Compile/run correctness of type-1 solutions was already verified by execution; skip that. No style nits. Return the findings list (empty if none).`
}

function fixPrompt(s, findings) {
  return `Fix worker for the new exercises in ${wt(s)} (cd there; do NOT commit/push/checkout/stash). Scope: ONLY the findings below, in en/${s.language}/${s.argument}/ (and en/${s.language}/data.json if named). For each finding first confirm it is real by reading the file; skip it (and say why) if it is not. Apply minimal fixes that keep the exercise's intent.
${FORMAT_RULES}
Findings:
${findings.map((f, i) => `${i + 1}. ${f.file}: ${f.defect}\n   fix: ${f.fix}`).join('\n')}
${CHECKS(s)}
All must pass again (validator, tester for type 1, check_outputs). Return a short list of what you changed and what you skipped.`
}

function translatePrompt(s, group) {
  return `Translation is done by GLM through OpenCode; you only drive the script. Run, one after another (each takes several minutes; wait for it):
${group.map((l) => `sh ${MAIN}/scripts/translate_glm.sh '${wt(s)}' ${s.language} ${s.argument} ${l}`).join('\n')}
Each run ends by printing either "ok <locale> (<n> files)" or, after its own retry, the remaining DIFF/MISSING lines for that locale. Do not edit any file yourself. Return one line per locale with its final printed result.`
}

function verifyPrompt(s) {
  return `Verifier for ${wt(s)} (cd there; no commit/push/checkout/stash; you MAY edit files to fix problems).
${CHECKS(s)}
Also: for each locale in de es fr hi it ja ko pl pt ru zh, the file count in <locale>/${s.language}/${s.argument}/ must equal en's, and <locale>/${s.language}/data.json must contain "${s.argument}". Then regenerate: (cd json_creator && dart run lib/json_creator.dart) and (cd theory_creator && dart run lib/theory_creator.dart), and run the validator once more. Finally 'git status --short' must list only: en + 11 locale folders for ${s.language}/${s.argument}, the 12 data.json files, curriculum.json, _theory.md files, and assets/arguments/${s.argument}.svg if new; tester/.env is ignored.
If something fails and the fix is mechanical or clearly correct (a locale code section differing from en -> copy en's; a missing translated file -> translate it; a missing data.json entry -> add it; an untranslated English sentence in a locale -> translate it), fix it and re-run. Anything needing a content decision goes to remainingProblems with the exact error text.
${FORMAT_RULES}`
}

function shipPrompt(s, report) {
  return `Ship the branch in ${wt(s)} (cd there). Verification report: ${JSON.stringify(report)}.
${report.remainingProblems.length ? 'There are remaining problems; still open the PR but list them in the PR body under "Known issues".' : ''}
Steps:
  git add -A -- '*.md' '*/data.json' curriculum.json assets   # never stage stray helper scripts
  /Users/ale/.local/bin/agent-commit -m "Feat/${s.language} ${s.argument}: add ${s.count} exercises across 12 locales"
    (agent-commit is mandatory; if it reports that the commit-review gate needs a review, do NOT bypass: stop and return notes="gate blocked" with the exact message.)
  git push -u origin ${branch(s)}
  gh pr create --base main --head ${branch(s)} --title "Feat/${s.language} ${s.argument}" --body "<summary: exercise count and type mix, concepts covered in order, checks run (validator, tester, check_outputs, check_locales), and any known issues>"
Return branch, commit sha, PR URL, notes.`
}

const results = await pipeline(
  SPECS,
  (s) => agent(writePrompt(s), { label: `write:${s.language}-${s.argument}`, phase: 'Write', schema: WRITE_SCHEMA }),
  (w, s) => {
    if (!w) throw new Error('write failed')
    return agent(reviewPrompt(s), { label: `review:${s.language}-${s.argument}`, phase: 'Review', model: 'opus', schema: FINDINGS_SCHEMA })
      .then((r) => ({ w, findings: (r && r.findings) || [] }))
  },
  ({ w, findings }, s) => {
    if (!findings.length) { log(`${s.language}/${s.argument}: review clean`); return w }
    log(`${s.language}/${s.argument}: ${findings.length} review findings`)
    return agent(fixPrompt(s, findings), { label: `fix:${s.language}-${s.argument}`, phase: 'Fix' }).then(() => w)
  },
  (w, s) => parallel(LOCALE_GROUPS.map((g) => () => agent(translatePrompt(s, g), { label: `translate:${s.language}-${s.argument}:${g[0]}`, phase: 'Translate', model: 'haiku' }))).then(() => w),
  (w, s) => agent(verifyPrompt(s), { label: `verify:${s.language}-${s.argument}`, phase: 'Verify', model: 'opus', schema: REPORT_SCHEMA }),
  (report, s) => agent(shipPrompt(s, report), { label: `ship:${s.language}-${s.argument}`, phase: 'Ship', model: 'sonnet', schema: SHIP_SCHEMA })
    .then((ship) => ({ language: s.language, argument: s.argument, worktree: wt(s), report, ship })),
)

return results
