import 'dart:io';

import 'package:parser/parser.dart';
import 'package:test/test.dart';
import 'package:tester/tester.dart';

void main() {
  final mdParser = MDParserBLoC();

  group('composer - dart', () {
    test('assignmentOperators/8 produces compilable Dart after Part A fix',
        () async {
      final file =
          File('${Directory.current.path}/../en/dart/assignmentOperators/8.md');
      final model = await mdParser.parse(file: file);
      final composed = compose(model);

      expect(composed.language, equals('dart'));
      expect(composed.languageId, equals(1));

      // sourceCode = beforeSeed + solution + afterSeed
      // The user's mutation statement must be INSIDE the function wrapper.
      expect(composed.sourceCode, contains('dynamic result() {'));
      expect(composed.sourceCode, contains('int points = 20;'));
      expect(composed.sourceCode, contains('points += 15;'));
      expect(composed.sourceCode, contains('return points;'));
      // The closing brace must come AFTER the mutation.
      final mutIdx = composed.sourceCode.indexOf('points += 15;');
      final closeIdx = composed.sourceCode.lastIndexOf('}');
      expect(mutIdx, lessThan(closeIdx),
          reason: 'Mutation statement must be before the function closing brace');

      // testCode is a separate file (the Dart split rule).
      expect(composed.testCode, isNotNull);
      expect(composed.testCode, contains("import 'package:test/test.dart';"));
      expect(composed.testCode, contains('expect(result(), 35,'));
    });

    test('booleans/8 (known-good top-level decl) composes without a wrapper',
        () async {
      final file =
          File('${Directory.current.path}/../en/dart/booleans/8.md');
      final model = await mdParser.parse(file: file);
      final composed = compose(model);

      expect(composed.language, equals('dart'));
      expect(composed.sourceCode, contains('bool isHidden = false;'));
      expect(composed.testCode, isNotNull);
      expect(composed.testCode, contains('expect(isHidden, false,'));
    });

    test('variables/3 (canonical wrap pattern) splits source/test correctly',
        () async {
      final file = File('${Directory.current.path}/../en/dart/variables/3.md');
      final model = await mdParser.parse(file: file);
      final composed = compose(model);

      expect(composed.sourceCode, contains('dynamic number() {'));
      expect(composed.sourceCode, contains('return x;'));
      // No test scaffold lines should leak into sourceCode.
      expect(composed.sourceCode, isNot(contains("import 'package:test")));
      // No solution lines should leak into testCode.
      expect(composed.testCode, isNot(contains('int x = 2')));
    });
  });

  group('composer - non-dart', () {
    test('python flattens everything into sourceCode (no testCode)', () async {
      // Pick any python exerciseType:1 file — addition is in functions/.
      // Fall back to walking en/python/**/*.md to find a type-1 exercise.
      final pyDir =
          Directory('${Directory.current.path}/../en/python');
      File? typeOneFile;
      for (final entity
          in pyDir.listSync(recursive: true).whereType<File>()) {
        if (!entity.path.endsWith('.md')) continue;
        final content = await entity.readAsString();
        if (content.contains('exerciseType: 1')) {
          typeOneFile = entity;
          break;
        }
      }
      if (typeOneFile == null) {
        markTestSkipped('no python exerciseType:1 .md found');
        return;
      }

      final model = await mdParser.parse(file: typeOneFile);
      final composed = compose(model);
      expect(composed.language, equals('python'));
      expect(composed.languageId, equals(2));
      expect(composed.testCode, isNull,
          reason: 'Non-Dart languages should not produce a testCode split');
      // For python, before-asserts (`import unittest\nclass CodigoTests...`)
      // is inside sourceCode.
      expect(composed.sourceCode, contains('unittest'));
    });
  });

  group('result_judge', () {
    test('detects --err-tN-- markers as test failures', () {
      final sub = SubmissionResult(
        compilationResult: CompilationResult(
          exitCode: 0,
          time: 0.5,
          stdout:
              "00:00 +0: test1\nTest Case '--err-t1--' failed\n00:00 +0 -1: Some tests failed.\n",
        ),
      );
      final j = judge(sub, 'dart');
      expect(j.verdict, equals(Verdict.testFailure));
      expect(j.failedTests, contains('test1'));
    });

    test('"All tests passed!" + exit 0 is a Pass for dart', () {
      final sub = SubmissionResult(
        compilationResult: CompilationResult(
          exitCode: 0,
          time: 0.5,
          stdout: '00:00 +1: All tests passed!\n',
        ),
      );
      final j = judge(sub, 'dart');
      expect(j.verdict, equals(Verdict.pass));
    });

    test('"Failed to load test/main_test.dart" => compile failure', () {
      final sub = SubmissionResult(
        compilationResult: CompilationResult(
          exitCode: 1,
          time: 0.5,
          stdout:
              '00:00 +0 -1: loading test/main_test.dart [E]\n  Failed to load "test/main_test.dart":\n  lib/main.dart:2:1: Error: ...',
        ),
      );
      final j = judge(sub, 'dart');
      expect(j.verdict, equals(Verdict.compileFailure));
    });

    test('RPC error -32003 => compile failure', () {
      final sub = SubmissionResult(
        error: SubmissionError(
          code: -32003,
          message: 'compilation failed',
          data: {'stderr': 'syntax error'},
        ),
      );
      final j = judge(sub, 'dart');
      expect(j.verdict, equals(Verdict.compileFailure));
    });
  });
}
