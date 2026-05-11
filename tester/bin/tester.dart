import 'dart:async';
import 'dart:convert';
import 'dart:io';

import 'package:args/args.dart';
import 'package:glob/glob.dart';
import 'package:glob/list_local_fs.dart';
import 'package:parser/parser.dart';
import 'package:path/path.dart' as p;
import 'package:tester/tester.dart';

Future<void> main(List<String> arguments) async {
  final parserArgs = ArgParser()
    ..addOption(
      'path',
      abbr: 'p',
      help: 'Exercise path or glob (relative to repo root).',
      defaultsTo: 'en/dart/**/*.md',
    )
    ..addOption(
      'language',
      abbr: 'l',
      help: 'Filter by language (dart|c|python|kotlin|javascript|swift).',
    )
    ..addOption(
      'type',
      abbr: 't',
      help: 'Filter by exerciseType. Only type 1 is executed; others are '
          'skipped silently.',
    )
    ..addFlag('fail-fast', help: 'Stop on first failure.', negatable: false)
    ..addOption(
      'timeout',
      help: 'Per-exercise timeout for RTDB wait in seconds.',
    )
    ..addOption(
      'report',
      help: 'Report format: text (default) or json.',
      allowed: ['text', 'json'],
      defaultsTo: 'text',
    )
    ..addFlag('help', abbr: 'h', help: 'Show usage.', negatable: false);

  late final ArgResults args;
  try {
    args = parserArgs.parse(arguments);
  } on FormatException catch (e) {
    stderr.writeln(e.message);
    stderr.writeln(parserArgs.usage);
    exit(64);
  }

  if (args['help'] as bool) {
    stdout.writeln('Usage: dart run tester:tester [options]\n');
    stdout.writeln(parserArgs.usage);
    return;
  }

  final config = TesterConfig.load();
  if (args['timeout'] != null) {
    // Override via env-less mechanism: rebuild config with the new timeout.
    // The simplest path is to mutate the local copy via composition — but
    // since TesterConfig is immutable, just construct a fresh one.
    final overridden = TesterConfig(
      codecompilerUrl: config.codecompilerUrl,
      firebaseApiKey: config.firebaseApiKey,
      firebaseDatabaseUrl: config.firebaseDatabaseUrl,
      timeoutSec: int.parse(args['timeout'] as String),
    );
    await _run(args, overridden);
    return;
  }
  await _run(args, config);
}

Future<void> _run(ArgResults args, TesterConfig config) async {
  final repoRoot = _findRepoRoot();
  final pattern = args['path'] as String;
  final langFilter = args['language'] as String?;
  final typeFilter =
      args['type'] != null ? int.tryParse(args['type'] as String) : null;
  final failFast = args['fail-fast'] as bool;
  final report = args['report'] as String;

  final glob = Glob(pattern, recursive: true);
  final matches = glob
      .listSync(root: repoRoot.path)
      .whereType<File>()
      .where((f) => p.extension(f.path) == '.md')
      .toList()
    ..sort((a, b) => a.path.compareTo(b.path));

  if (matches.isEmpty) {
    stderr.writeln('No .md files matched: $pattern (root: ${repoRoot.path})');
    exit(2);
  }

  final mdParser = MDParserBLoC();
  final runner = Runner(config: config, parser: mdParser);
  final results = <ExerciseRun>[];

  try {
    for (final file in matches) {
      final relative = p.relative(file.path, from: repoRoot.path);

      // Skip files that aren't proper exercise files (e.g. _theory.md,
      // arbitrary docs). They have no parseable frontmatter.
      if (p.basename(file.path).startsWith('_')) continue;

      // Pre-filter by language/type without paying the codecompiler cost.
      ExerciseModel preModel;
      try {
        preModel = await mdParser.parse(file: file);
      } catch (_) {
        // File doesn't parse as an exercise — skip it silently.
        continue;
      }
      final lang = preModel.frontMatterModel.language;
      final type = preModel.frontMatterModel.exerciseType;
      if (langFilter != null && lang != langFilter) continue;
      if (typeFilter != null && type != typeFilter) continue;

      // Per-line progress goes to stderr so --report json keeps stdout clean.
      final progressSink = report == 'json' ? stderr : stdout;
      progressSink.write('  $relative ');
      final run = await runner.runOne(file, relative);
      results.add(run);
      _printOneLine(run, progressSink);
      if (failFast && !run.skipped && !run.passed) break;
    }
  } finally {
    runner.close();
  }

  if (report == 'json') {
    _printJson(results);
  } else {
    _printSummary(results);
  }

  final hadFailure = results.any((r) => !r.skipped && !r.passed);
  exit(hadFailure ? 1 : 0);
}

Directory _findRepoRoot() {
  var dir = Directory.current;
  while (true) {
    // .git is a directory in normal clones, but a file (gitlink) in worktrees.
    if (FileSystemEntity.typeSync(p.join(dir.path, '.git')) !=
        FileSystemEntityType.notFound) {
      return dir;
    }
    final parent = dir.parent;
    if (parent.path == dir.path) {
      // Fall back to CWD if no .git found.
      return Directory.current;
    }
    dir = parent;
  }
}

void _printOneLine(ExerciseRun run, IOSink sink) {
  if (run.skipped) {
    sink.writeln('SKIP  (${run.skipReason})');
    return;
  }
  final j = run.judgement!;
  final elapsed = run.elapsed == null ? '' : ' ${run.elapsed!.inSeconds}s';
  switch (j.verdict) {
    case Verdict.pass:
      sink.writeln('PASS$elapsed');
    case Verdict.testFailure:
      sink.writeln('FAIL$elapsed  ${j.summary}');
    case Verdict.compileFailure:
      sink.writeln('COMPILE-ERROR$elapsed  ${j.summary}');
    case Verdict.runtimeFailure:
      sink.writeln('RUNTIME-ERROR$elapsed  ${j.summary}');
    case Verdict.unknown:
      sink.writeln('?$elapsed  ${j.summary}');
  }
}

void _printSummary(List<ExerciseRun> results) {
  final pass = results.where((r) => r.passed).length;
  final skipped = results.where((r) => r.skipped).length;
  final failed = results.where((r) => !r.skipped && !r.passed).toList();

  stdout.writeln();
  stdout.writeln('---');
  stdout.writeln('Ran ${results.length} exercises: '
      '$pass passed, ${failed.length} failed, $skipped skipped.');

  if (failed.isNotEmpty) {
    stdout.writeln();
    stdout.writeln('Failures:');
    for (final r in failed) {
      stdout.writeln('  ${r.path}');
      final j = r.judgement!;
      stdout.writeln('    ${j.verdict.name}: ${j.summary}');
      if ((j.stdout ?? '').isNotEmpty) {
        stdout.writeln(
          '    stdout (truncated):\n${_indent(_truncate(j.stdout!), 6)}',
        );
      }
      if ((j.stderr ?? '').isNotEmpty) {
        stdout.writeln(
          '    stderr (truncated):\n${_indent(_truncate(j.stderr!), 6)}',
        );
      }
    }
  }
}

void _printJson(List<ExerciseRun> results) {
  final list = results
      .map(
        (r) => <String, dynamic>{
          'path': r.path,
          'language': r.language,
          'exerciseType': r.exerciseType,
          'skipped': r.skipped,
          'skipReason': r.skipReason,
          'verdict': r.judgement?.verdict.name,
          'summary': r.judgement?.summary,
          'failedTests': r.judgement?.failedTests,
          'elapsedMs': r.elapsed?.inMilliseconds,
        },
      )
      .toList();
  stdout.writeln(const JsonEncoder.withIndent('  ').convert(list));
}

String _truncate(String s, [int maxLines = 20]) {
  final lines = s.split('\n');
  if (lines.length <= maxLines) return s;
  return '${lines.take(maxLines).join('\n')}\n... (${lines.length - maxLines} more lines)';
}

String _indent(String s, int n) {
  final pad = ' ' * n;
  return s.split('\n').map((l) => '$pad$l').join('\n');
}
