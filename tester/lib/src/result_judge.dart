import 'rtdb_client.dart';

enum Verdict { pass, testFailure, compileFailure, runtimeFailure, unknown }

class Judgement {
  Judgement({
    required this.verdict,
    required this.summary,
    this.failedTests = const [],
    this.stdout,
    this.stderr,
  });

  final Verdict verdict;
  final String summary;
  final List<String> failedTests;
  final String? stdout;
  final String? stderr;
}

/// Mirrors codigo_x's response-validation logic. Inputs are the RTDB
/// `SubmissionResult` plus the exercise's language (since Dart's pass
/// detection is unique) plus an optional expected stdout for `--output--`
/// style exercises.
Judgement judge(
  SubmissionResult result,
  String language, {
  String? expectedOutput,
}) {
  final err = result.error;
  if (err != null) {
    switch (err.code) {
      case -32003:
        return Judgement(
          verdict: Verdict.compileFailure,
          summary: 'Compilation failed: ${err.message}',
          stdout: err.data?['stdout'] as String?,
          stderr: err.data?['stderr'] as String?,
        );
      case -32004:
        // -32004 ("program execution failed") is overloaded: it covers both
        // genuine runtime errors AND Dart's compile-error path (where
        // `dart test` can't load test/main_test.dart because lib/main.dart
        // doesn't parse). Always send stdout through _judgeStdout so that
        // compile-error and test-marker patterns get the right verdict.
        final stderr = err.data?['stderr'] as String?;
        final stdout = err.data?['stdout'] as String?;
        if (stdout != null && stdout.isNotEmpty) {
          return _judgeStdout(stdout, language, exitCode: 1, stderr: stderr);
        }
        return Judgement(
          verdict: Verdict.runtimeFailure,
          summary: 'Runtime error: ${err.message}',
          stdout: stdout,
          stderr: stderr,
        );
      case -32005:
        return Judgement(
          verdict: Verdict.runtimeFailure,
          summary: 'Timeout: ${err.message}',
        );
      default:
        return Judgement(
          verdict: Verdict.unknown,
          summary: 'codecompiler error ${err.code}: ${err.message}',
          stderr: err.data?['stderr'] as String?,
          stdout: err.data?['stdout'] as String?,
        );
    }
  }

  final res = result.compilationResult;
  if (res == null) {
    return Judgement(
      verdict: Verdict.unknown,
      summary: 'No compilationResult and no error in RTDB record',
    );
  }

  // --output-- style: compare stdout to the exercise's expected output.
  if (expectedOutput != null) {
    final got = (res.stdout ?? '').trim();
    final want = expectedOutput.trim();
    if (res.exitCode == 0 && got == want) {
      return Judgement(
        verdict: Verdict.pass,
        summary: 'stdout matches expected output',
        stdout: res.stdout,
      );
    }
    return Judgement(
      verdict: Verdict.testFailure,
      summary: 'stdout (${got.length} chars) does not match expected output '
          '(${want.length} chars)',
      stdout: res.stdout,
      stderr: res.stderr,
    );
  }

  return _judgeStdout(
    res.stdout ?? '',
    language,
    exitCode: res.exitCode,
    stderr: res.stderr,
  );
}

Judgement _judgeStdout(
  String stdout,
  String language, {
  required int exitCode,
  String? stderr,
}) {
  // Dart-specific compile failure: dart test prints a "Failed to load" line
  // when test/main_test.dart can't compile (often because lib/main.dart has
  // a Dart syntax error).
  if (language == 'dart' &&
      RegExp(r'Failed to load "?test/main_test\.dart').hasMatch(stdout)) {
    return Judgement(
      verdict: Verdict.compileFailure,
      summary: 'Dart compile/load failure (see stdout)',
      stdout: stdout,
      stderr: stderr,
    );
  }

  // Test failure: one or more --err-tN-- markers in stdout.
  final markers = RegExp(r'--err-t(\d+)--')
      .allMatches(stdout)
      .map((m) => 'test${m.group(1)}')
      .toSet()
      .toList();
  if (markers.isNotEmpty) {
    return Judgement(
      verdict: Verdict.testFailure,
      summary: '${markers.length} test(s) failed: ${markers.join(', ')}',
      failedTests: markers,
      stdout: stdout,
      stderr: stderr,
    );
  }

  // Pass criteria are language-specific.
  if (language == 'dart') {
    if (exitCode == 0 && stdout.contains('All tests passed!')) {
      return Judgement(
        verdict: Verdict.pass,
        summary: 'All tests passed',
        stdout: stdout,
      );
    }
    return Judgement(
      verdict: Verdict.unknown,
      summary: 'Dart run completed but no "All tests passed!" marker '
          '(exitCode=$exitCode)',
      stdout: stdout,
      stderr: stderr,
    );
  }

  // Non-Dart languages: pass if no --err-tN-- marker (already established
  // above) AND exit code 0 (for languages that exit non-zero on failure)
  // OR stdout reports "0 failures" (for languages that always exit 0).
  if (exitCode == 0) {
    return Judgement(
      verdict: Verdict.pass,
      summary: 'No test failures detected',
      stdout: stdout,
    );
  }
  return Judgement(
    verdict: Verdict.runtimeFailure,
    summary: 'Non-zero exit code ($exitCode), no test markers in stdout',
    stdout: stdout,
    stderr: stderr,
  );
}
