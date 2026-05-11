import 'package:parser/parser.dart';

class ComposedExercise {
  ComposedExercise({
    required this.sourceCode,
    required this.testCode,
    required this.languageId,
    required this.language,
    this.expectedOutput,
  });

  final String sourceCode;
  final String? testCode;
  final int languageId;
  final String language;

  /// When non-null, the exercise has no `--asserts--`; pass/fail is decided
  /// by comparing program stdout to this expected string.
  final String? expectedOutput;
}

const _languageIds = <String, int>{
  'dart': 1,
  'python': 2,
  'swift': 3,
  'kotlin': 4,
  'javascript': 5,
  'c': 6,
};

int? languageIdFor(String language) => _languageIds[language];

String _join(Iterable<String?> parts) =>
    parts.where((p) => p != null && p.isNotEmpty).map((p) => p!).join('\n');

String? _assertsCode(List<AssertModel>? asserts) {
  if (asserts == null || asserts.isEmpty) return null;
  final lines = asserts
      .where((a) => a.unitTest != null)
      .map((a) => a.unitTest!)
      .toList();
  if (lines.isEmpty) return null;
  return lines.join('\n');
}

ComposedExercise compose(ExerciseModel model) {
  final language = model.frontMatterModel.language;
  final id = languageIdFor(language);
  if (id == null) {
    throw ArgumentError('Unsupported language: $language');
  }

  final solution = model.solutions?.first ?? '';
  final beforeSeed = model.beforeSeed?.code;
  final afterSeed = model.afterSeed?.code;
  final codeBeforeAsserts = model.codeBeforeAsserts?.code;
  final codeAfterAsserts = model.codeAfterAsserts?.code;
  final asserts = _assertsCode(model.asserts);

  // --output-- exercises have no --asserts--; the expected stdout is the
  // success criterion. Keep the expected output around so the judge can
  // compare it.
  final hasAsserts = asserts != null && asserts.isNotEmpty;
  final expectedOutput = !hasAsserts ? model.output : null;

  if (language == 'dart') {
    final sourceCode = _join([beforeSeed, solution, afterSeed]);
    final testCode = _join([codeBeforeAsserts, asserts, codeAfterAsserts]);
    return ComposedExercise(
      sourceCode: sourceCode,
      testCode: testCode.isEmpty ? null : testCode,
      languageId: id,
      language: language,
      expectedOutput: expectedOutput,
    );
  }

  final sourceCode = _join([
    beforeSeed,
    solution,
    afterSeed,
    codeBeforeAsserts,
    asserts,
    codeAfterAsserts,
  ]);
  return ComposedExercise(
    sourceCode: sourceCode,
    testCode: null,
    languageId: id,
    language: language,
    expectedOutput: expectedOutput,
  );
}
