export const meta = {
  name: 'new-challenge',
  description: 'Author one coding challenge in all 6 languages, review it, translate to 11 locales, verify with validator+tester, open a PR',
  whenToUse: 'Pass args: [{challenge, name, difficulty, icon, brief, notes?}, ...]. One item per challenge topic; items run in parallel, each in its own worktree /tmp/codigo-new/challenge-<challenge>. Requires the codecompiler-8081 container and tester/.env in the main checkout.',
  phases: [
    { title: 'Fetch', detail: 'fetch origin once, serialized, before any worktree is created' },
    { title: 'Write', detail: 'author the challenge in c, dart, javascript, kotlin, python, swift' },
    { title: 'Review', detail: 'independent content review (ambiguity, spec drift, harness)' },
    { title: 'Fix', detail: 'apply confirmed findings' },
    { title: 'Translate', detail: '3 locale groups, GLM via script' },
    { title: 'Verify', detail: 'validator, tester, locale checks, regenerate' },
    { title: 'Ship', detail: 'commit, push, open PR' },
  ],
}

// ---------------------------------------------------------------------------
// Inputs. `args` is an array of challenge specs (or one spec).
//   challenge   folder-safe name, e.g. 'binary_search' -> en/<lang>/challenges/binary_search.md
//   name        display name for challenges/data.json, e.g. 'Binary search'
//   difficulty  1 | 2 | 3
//   icon        absolute path to an SVG to install as assets/challenges/<challenge>.svg
//   brief       the problem statement the 6 implementations must agree on
//   notes       optional extra guidance (edge cases, signature per language)
// ---------------------------------------------------------------------------
const SPECS = (Array.isArray(args) ? args : [args]).filter(Boolean)
if (!SPECS.length) throw new Error('new-challenge: pass args as an array of {challenge, name, difficulty, icon, brief}')

const MAIN = '/Users/ale/.t3/worktrees/codigo-questions/t3code-3441c85c'
const LANGS = ['c', 'dart', 'javascript', 'kotlin', 'python', 'swift']
const LOCALE_GROUPS = [['de', 'es', 'fr', 'it'], ['pt', 'pl', 'ru', 'zh'], ['ja', 'ko', 'hi']]

const FORMAT_RULES = `
Challenge format: read CLAUDE.md in the worktree root, then read at least three existing challenges of the SAME language (en/<lang>/challenges/*.md) before writing that language.
- A challenge is a single file en/<lang>/challenges/<name>.md with exerciseType: 1 and frontmatter 'difficulty' (1-3) and 'title'.
- Required sections: '# --description--', '# --instructions--', '# --seed--', '# --before-asserts--', '# --asserts--', '# --after-asserts--', '# --solutions--'. '# --before-seed--' carries the language harness.
- COPY the harness blocks verbatim from an existing challenge of the same language. C uses the CException/Unity harness in '# --before-seed--'; Dart uses package:test with group()/test()/expect() split across before-asserts/after-asserts; Kotlin puts user code at top level with main in the asserts harness; Swift uses the tryCatch helper, never XCTest; JavaScript and Python follow their own neighbours.
- Every assert code block must be preceded by a one-line prose description and must carry a distinct '--err-tN--' marker, numbered from 1, exactly as the neighbours do.
- The '# --seed--' is the empty function signature the learner fills in; '# --solutions--' is a complete working implementation.
- Keep the description and instructions IDENTICAL in meaning across all 6 languages (same story, same examples, same edge cases); only the code, the function signature and language-specific phrasing may differ.
- Code must compile and run on the production codecompiler versions: C = GCC 13.3.0 (C11/C17), Dart 3.13.3 (null safety), JavaScript = Node.js 26.8.1, Kotlin 2.4.20 on Java 17 (JVM 17 APIs only), Python 3.14.7, Swift 6.3.3 (Swift 6 strict concurrency). Never use anything deprecated or removed there. Kotlin coroutines are NOT on the compile classpath. Swift regex literals need the extended delimiter #/pattern/#.`

const CHECKS = (s) => `
Checks (run from the worktree root; the codecompiler Docker container must be running: 'docker start codecompiler-8081'):
  cp ${MAIN}/tester/.env tester/.env
  for d in validator tester json_creator theory_creator; do (cd $d && dart pub get >/dev/null); done
  (cd validator && dart test lib/validator.dart --reporter=failures-only --chain-stack-traces --fail-fast 2>&1 | tail -20)
  for L in ${LANGS.join(' ')}; do (cd tester && dart run bin/tester.dart -p "en/$L/challenges/${s.challenge}.md" -t 1 2>&1 | tail -20); done
  python3 scripts/check_locales.py WORKTREE
All 6 type-1 challenge files must PASS in the tester before you are done.`

const WRITE_SCHEMA = {
  type: 'object',
  properties: {
    worktree: { type: 'string' },
    files: { type: 'array', items: { type: 'string' } },
    testerResults: { type: 'string' },
    notes: { type: 'string' },
  },
  required: ['worktree', 'files', 'testerResults', 'notes'],
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
    locales: { type: 'string' },
    fixesApplied: { type: 'array', items: { type: 'string' } },
    remainingProblems: { type: 'array', items: { type: 'string' } },
  },
  required: ['validator', 'tester', 'locales', 'fixesApplied', 'remainingProblems'],
}
const SHIP_SCHEMA = {
  type: 'object',
  properties: { branch: { type: 'string' }, commit: { type: 'string' }, prUrl: { type: 'string' }, notes: { type: 'string' } },
  required: ['branch', 'commit', 'prUrl', 'notes'],
}

const wt = (s) => `/tmp/codigo-new/challenge-${s.challenge}`
const branch = (s) => `feat/challenge-${s.challenge}`

function writePrompt(s) {
  return `You are a senior educator writing ONE new coding challenge for the Codigo app, in all 6 supported languages.

SETUP (exactly):
  cd ${MAIN} && mkdir -p /tmp/codigo-new && git worktree add ${wt(s)} -b ${branch(s)} origin/main
  cd ${wt(s)}
Work ONLY inside ${wt(s)}. Do NOT commit, push, stash, checkout or touch other worktrees. origin was already fetched for you before this step; do not fetch it again yourself.

CHALLENGE: name="${s.name}", folder-safe key="${s.challenge}", difficulty=${s.difficulty}.
Problem: ${s.brief}
${s.notes ? 'Author notes: ' + s.notes : ''}

Deliverables:
1. en/<lang>/challenges/${s.challenge}.md for every lang in: ${LANGS.join(' ')}
2. In every en/<lang>/challenges/data.json add "${s.challenge}": {"difficulty": ${s.difficulty}, "name": "${s.name}"} — append it in the same style as the neighbouring entries.
3. cp ${s.icon} assets/challenges/${s.challenge}.svg
Do NOT create _theory.md and do NOT touch en/<lang>/data.json (challenges are not arguments).
${FORMAT_RULES}
${CHECKS(s)}
Iterate until the validator passes and all 6 files PASS in the tester. check_locales will report MISSING for the 11 other locales; that is expected (they are translated later). Return worktree, the file list, the per-language tester results, and notes.`
}

function reviewPrompt(s) {
  return `You are an independent reviewer of a new coding challenge. Read-only: do not modify files, do not run git commands that change state. Files: ${wt(s)}/en/<lang>/challenges/${s.challenge}.md for ${LANGS.join(', ')}, plus ${wt(s)}/CLAUDE.md for the format.

Report ONLY actual defects, each with file path, the defect, and a one-line fix:
- The 6 language versions disagree: different problem statement, different examples, different edge-case behaviour, or different expected results for the same input.
- Instructions that do not uniquely determine the expected output (ambiguous tie-breaking, unspecified behaviour on empty input, unspecified ordering).
- Instructions inconsistent with the seed signature or the solution (names, parameter order, return type).
- Asserts that pass without exercising what the instructions ask; missing or duplicated '--err-tN--' markers; an assert whose prose line does not match what it checks.
- Factually wrong statements about a language.
- Harness mistakes: Dart not using the package:test group/expect pattern; Kotlin top-level-only constructs inside main; Swift XCTest instead of the tryCatch helper; C missing the CException harness.
- difficulty/title frontmatter missing or inconsistent with the data.json entry.
Compile/run correctness was already verified by execution; skip that. No style nits. Return the findings list (empty if none).`
}

function fixPrompt(s, findings) {
  return `Fix worker for the new challenge in ${wt(s)} (cd there; do NOT commit/push/checkout/stash). Scope: ONLY the findings below, in en/*/challenges/${s.challenge}.md and en/*/challenges/data.json. For each finding first confirm it is real by reading the file; skip it (and say why) if it is not. Apply minimal fixes that keep the challenge's intent.
${FORMAT_RULES}
Findings:
${findings.map((f, i) => `${i + 1}. ${f.file}: ${f.defect}\n   fix: ${f.fix}`).join('\n')}
${CHECKS(s)}
All must pass again. Return a short list of what you changed and what you skipped.`
}

function translatePrompt(s, group) {
  return `Translation is done by GLM through OpenCode; you only drive the script. Run, one after another (each takes several minutes; wait for it):
${group.map((l) => `sh ${MAIN}/scripts/translate_challenge_glm.sh '${wt(s)}' ${s.challenge} ${l}`).join('\n')}
Each run ends by printing either "ok <locale> (<n> files)" or, after its own retry, the remaining DIFF/MISSING/BAD lines for that locale. Do not edit any file yourself. Return one line per locale with its final printed result.`
}

function verifyPrompt(s) {
  return `Verifier for ${wt(s)} (cd there; no commit/push/checkout/stash; you MAY edit files to fix problems).
${CHECKS(s)}
Also: for every locale in de es fr hi it ja ko pl pt ru zh and every language in ${LANGS.join(' ')}, <locale>/<lang>/challenges/${s.challenge}.md must exist and <locale>/<lang>/challenges/data.json must contain "${s.challenge}" with the same difficulty as en and a non-empty translated name. Then regenerate: (cd json_creator && dart run lib/json_creator.dart) and (cd theory_creator && dart run lib/theory_creator.dart), and run the validator once more.
Finally 'git status --short' must list only: the 72 challenge .md files, the 72 challenges/data.json files, curriculum.json, assets/challenges/${s.challenge}.svg, and any _theory.md the generator touched; tester/.env is ignored. Delete any stray helper script you created.
If something fails and the fix is mechanical or clearly correct (a locale code section differing from en -> copy en's; a missing translated file -> translate it; a missing data.json entry -> add it; an untranslated English sentence in a locale -> translate it), fix it and re-run. Anything needing a content decision goes to remainingProblems with the exact error text.
${FORMAT_RULES}`
}

function shipPrompt(s, report) {
  return `Ship the branch in ${wt(s)} (cd there). Verification report: ${JSON.stringify(report)}.
${report.remainingProblems.length ? 'There are remaining problems; still open the PR but list them in the PR body under "Known issues".' : ''}
Steps:
  git add -A -- '*.md' '*/data.json' curriculum.json assets   # never stage stray helper scripts
  /Users/ale/.local/bin/agent-commit -m "Feat/challenge ${s.challenge}: add the ${s.name} challenge in 6 languages across 12 locales"
    (agent-commit is mandatory; if it reports that the commit-review gate needs a review, do NOT bypass: stop and return notes="gate blocked" with the exact message.)
  git push -u origin ${branch(s)}
  gh pr create --base main --head ${branch(s)} --title "Feat/challenge ${s.challenge}" --body "<summary: the problem, difficulty, the 6 languages, the checks run (validator, tester, check_locales), and any known issues>"
Return branch, commit sha, PR URL, notes.`
}

const fetchSha = await agent(
  `Run exactly: cd ${MAIN} && git fetch -q origin && git rev-parse --short origin/main\nReturn only the resulting short commit sha, nothing else.`,
  { label: 'fetch:origin', phase: 'Fetch', model: 'haiku' },
)
log(`origin/main fetched @ ${fetchSha}`)

const results = await pipeline(
  SPECS,
  (s) => agent(writePrompt(s), { label: `write:${s.challenge}`, phase: 'Write', schema: WRITE_SCHEMA }),
  (w, s) => {
    if (!w) throw new Error('write failed')
    return agent(reviewPrompt(s), { label: `review:${s.challenge}`, phase: 'Review', model: 'opus', schema: FINDINGS_SCHEMA })
      .then((r) => ({ w, findings: (r && r.findings) || [] }))
  },
  ({ w, findings }, s) => {
    if (!findings.length) { log(`${s.challenge}: review clean`); return w }
    log(`${s.challenge}: ${findings.length} review findings`)
    return agent(fixPrompt(s, findings), { label: `fix:${s.challenge}`, phase: 'Fix' }).then(() => w)
  },
  (w, s) => parallel(LOCALE_GROUPS.map((g) => () => agent(translatePrompt(s, g), { label: `translate:${s.challenge}:${g[0]}`, phase: 'Translate', model: 'haiku' }))).then(() => w),
  (w, s) => agent(verifyPrompt(s), { label: `verify:${s.challenge}`, phase: 'Verify', model: 'opus', schema: REPORT_SCHEMA }),
  (report, s) => agent(shipPrompt(s, report), { label: `ship:${s.challenge}`, phase: 'Ship', model: 'sonnet', schema: SHIP_SCHEMA })
    .then((ship) => ({ challenge: s.challenge, worktree: wt(s), report, ship })),
)

return results
