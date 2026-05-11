import 'dart:io';

import 'package:parser/parser.dart';

import 'codecompiler_client.dart';
import 'composer.dart';
import 'config.dart';
import 'firebase_auth_client.dart';
import 'result_judge.dart';
import 'rtdb_client.dart';

class ExerciseRun {
  ExerciseRun({
    required this.path,
    required this.language,
    required this.exerciseType,
    this.judgement,
    this.skipReason,
    this.elapsed,
  });

  final String path;
  final String language;
  final int exerciseType;
  final Judgement? judgement;
  final String? skipReason;
  final Duration? elapsed;

  bool get skipped => skipReason != null;
  bool get passed => judgement?.verdict == Verdict.pass;
}

class Runner {
  Runner({required this.config, required this.parser});

  final TesterConfig config;
  final MDParserBLoC parser;

  CodecompilerClient? _compiler;
  RtdbClient? _rtdb;
  FirebaseAuthClient? _auth;
  String? _idToken;

  Future<void> _ensureAuth() async {
    if (_idToken != null) return;
    _auth = FirebaseAuthClient(apiKey: config.firebaseApiKey);
    _idToken = await _auth!.signInAnonymously();
    _compiler = CodecompilerClient(
      endpoint: config.codecompilerUrl,
      authToken: _idToken!,
    );
    _rtdb = RtdbClient(
      databaseUrl: config.firebaseDatabaseUrl,
      authToken: _idToken!,
    );
  }

  Future<ExerciseRun> runOne(File file, String relativePath) async {
    final stopwatch = Stopwatch()..start();
    final model = await parser.parse(file: file);
    final language = model.frontMatterModel.language;
    final type = model.frontMatterModel.exerciseType;

    if (type != 1) {
      return ExerciseRun(
        path: relativePath,
        language: language,
        exerciseType: type,
        skipReason: 'exerciseType $type (only type 1 is executed)',
      );
    }

    if (languageIdFor(language) == null) {
      return ExerciseRun(
        path: relativePath,
        language: language,
        exerciseType: type,
        skipReason: 'unsupported language',
      );
    }

    await _ensureAuth();

    final composed = compose(model);
    String submissionId;
    try {
      submissionId = await _compiler!.submit(composed);
    } on CodecompilerError catch (e) {
      // Some compile/runtime errors come back inline on the RPC reply rather
      // than via RTDB. Synthesize a SubmissionResult so the judge handles it.
      final synthetic = SubmissionResult(
        error: SubmissionError(code: e.code, message: e.message, data: e.data),
      );
      return ExerciseRun(
        path: relativePath,
        language: language,
        exerciseType: type,
        judgement: judge(synthetic, language, expectedOutput: composed.expectedOutput),
        elapsed: stopwatch.elapsed,
      );
    } catch (e) {
      // Network / unexpected transport errors. Don't crash the sweep.
      return ExerciseRun(
        path: relativePath,
        language: language,
        exerciseType: type,
        judgement: Judgement(
          verdict: Verdict.unknown,
          summary: 'Submit failed: $e',
        ),
        elapsed: stopwatch.elapsed,
      );
    }

    try {
      final result = await _rtdb!.waitFor(
        submissionId,
        timeout: Duration(seconds: config.timeoutSec),
      );
      return ExerciseRun(
        path: relativePath,
        language: language,
        exerciseType: type,
        judgement:
            judge(result, language, expectedOutput: composed.expectedOutput),
        elapsed: stopwatch.elapsed,
      );
    } on SubmissionTimeout catch (e) {
      return ExerciseRun(
        path: relativePath,
        language: language,
        exerciseType: type,
        judgement: Judgement(
          verdict: Verdict.runtimeFailure,
          summary: 'Timed out after ${e.elapsed.inSeconds}s waiting for RTDB',
        ),
        elapsed: stopwatch.elapsed,
      );
    } catch (e) {
      return ExerciseRun(
        path: relativePath,
        language: language,
        exerciseType: type,
        judgement: Judgement(
          verdict: Verdict.unknown,
          summary: 'RTDB wait failed: $e',
        ),
        elapsed: stopwatch.elapsed,
      );
    }
  }

  void close() {
    _compiler?.close();
    _rtdb?.close();
    _auth?.close();
  }
}
