import 'dart:io';
import 'dart:math';

import 'package:path/path.dart' as path;
import 'package:test/test.dart';
import 'package:validator/bloc/md_parser_bloc.dart';
import 'package:validator/bloc/models/exercise_model/model.dart';
import 'package:validator/bloc/models/frontmatter_model/model.dart';

/// Returns all the available exercise languages.
List<String> get locales => ['en', 'it'];

/// The list of currently supported programming languages
const supportedProgrammingLanguages = <String>{
  "python",
  "swift",
  "bash",
  "javascript",
  "c",
};

Future<void> main() async {
  final parser = MDParserBLoC();

  for (final language in locales) {
    // Get the language directory.
    final languageDir = Directory('${Directory.current.path}/../$language');

    int index = 0;
    // List directory contents, recursing into sub-directories,
    // but not following symbolic links.
    await for (final entity in languageDir.list(
      recursive: true,
      followLinks: false,
    )) {
      if (isMDFile(entity)) {
        final exerciseModel = await parser.parse(file: entity as File);

        // The relative path of the exercise:

        // e.g:
        // `/en/c/challenges/atm.md`

        final relativePath = entity.path.split('..')[1];
        _validateExercise(
          exerciseModel: exerciseModel,
          exercisePath: relativePath,
        );

        index++;

        //if (index == 10) return;
      }
    }
  }
}

/// Validates the full exercise.
void _validateExercise({
  required ExerciseModel exerciseModel,
  required String exercisePath,
}) {
  _validateFrontMatter(
    frontMatterModel: exerciseModel.frontMatterModel,
    exercisePath: exercisePath,
  );

  if (isAChallenge(exercisePath)) {
    _runChallengeTests(
      exercisePath: exercisePath,
      model: exerciseModel,
    );
  }
}

/// Validates the front matter
void _validateFrontMatter({
  required FrontMatterModel frontMatterModel,
  required String exercisePath,
}) {
  final language = frontMatterModel.language;
  _testHandler('Verify that the language is supported', () {
    expect(
      supportedProgrammingLanguages,
      contains(language),
      reason: _fancyLogger(
        message:
            "The language provided `$language` is not supported, the currently supported languages are: $supportedProgrammingLanguages.",
        exercisePath: exercisePath,
      ),
    );
  });

  final languageFromPath = exerciseLanguageFromPath(exercisePath);
  _testHandler(
      'Verify that the language is the same to the language retrieved from the exercise path',
      () {
    expect(
      languageFromPath,
      equals(language),
      reason: _fancyLogger(
        message:
            "The language provided `$language` is different from the one retrieved from the exercise path: `$languageFromPath`. Did you put the exercise in the correct location?",
        exercisePath: exercisePath,
      ),
    );
  });

  /// The list of currently supported programming languages
  final _supportedExerciseTypes = List.generate(4, (index) => index + 1);

  final exerciseType = frontMatterModel.exerciseType;
  _testHandler('Verify that the exerciseType is supported', () {
    expect(
      _supportedExerciseTypes,
      contains(exerciseType),
      reason: _fancyLogger(
        message:
            "The exercise provided `$exerciseType` is not supported, the currently supported exercise types are: $_supportedExerciseTypes",
        exercisePath: exercisePath,
      ),
    );
  });

  /// The list of currently supported exercise difficulties
  final _supportedExerciseDifficulties = List.generate(3, (index) => index + 1);
  if (isAChallenge(exercisePath)) {
    _testHandler('Verify that the challenge contains a valid difficulty', () {
      expect(
        frontMatterModel.difficulty,
        isNot(equals(null)),
        reason: _fancyLogger(
          message:
              "You have to provide a `difficulty` inside the front matter.",
          exercisePath: exercisePath,
        ),
      );
      expect(
        _supportedExerciseDifficulties,
        contains(frontMatterModel.difficulty),
        reason: _fancyLogger(
          message:
              "The difficulty provided `${frontMatterModel.difficulty}` is not supported, the currently supported difficulties are: $_supportedExerciseDifficulties",
          exercisePath: exercisePath,
        ),
      );
    });

    _testHandler('Verify that the challenge contains a title', () {
      expect(
        frontMatterModel.title,
        isNot(equals(null)),
        reason: _fancyLogger(
          message: "You have to provide a `title` to the challenge",
          exercisePath: exercisePath,
        ),
      );
    });
  }
}

/// Runs all the tests to validate a challenge.
void _runChallengeTests({
  required ExerciseModel model,
  required String exercisePath,
}) {
  _testHandler('Verify that the challenge contains a description', () {
    expect(
      model.description?.trim(),
      isNotEmpty,
      reason: _fancyLogger(
        message: "You have to provide a `description` to the challenge",
        exercisePath: exercisePath,
      ),
    );
  });

  _testHandler('Verify that the challenge contains instructions', () {
    expect(
      model.instructions?.trim(),
      isNotEmpty,
      reason: _fancyLogger(
        message: "You have to provide `instructions` to the challenge",
        exercisePath: exercisePath,
      ),
    );
  });

  _testHandler('Verify that the challenge contains a valid seed', () {
    expect(
      model.seed?.code,
      isNotEmpty,
      reason: _fancyLogger(
        message: "You have to provide a `seed` to the challenge",
        exercisePath: exercisePath,
      ),
    );
    expect(
      model.seed?.language,
      supportedProgrammingLanguages.contains,
      reason: _fancyLogger(
        message:
            "You have to provide a supported language code to the `seed`. The supported languages are $supportedProgrammingLanguages",
        exercisePath: exercisePath,
      ),
    );
  });

  _testHandler(
      'Verify that the challenge contains a valid - before asserts - code', () {
    expect(
      model.codeBeforeAsserts?.code.trim(),
      anyOf([
        equals(null),
        isNotEmpty,
      ]),
      reason: _fancyLogger(
        message:
            "Your `before asserts` code must not be empty. If you don't want to add it, remove the tag.",
        exercisePath: exercisePath,
      ),
    );
    expect(
      model.codeBeforeAsserts?.language,
      allOf([
        isNot(equals(null)),
        supportedProgrammingLanguages.contains,
      ]),
      reason: _fancyLogger(
        message:
            "Your `before asserts` language code cannot be null or is unsupported. The supported languages are $supportedProgrammingLanguages. Add it after the backticks, for example ```python",
        exercisePath: exercisePath,
      ),
    );
  });

  _testHandler(
      'Verify that the challenge contains a valid - after asserts - code', () {
    expect(
      model.codeAfterAsserts?.code.trim(),
      anyOf([
        equals(null),
        isNotEmpty,
      ]),
      reason: _fancyLogger(
        message:
            "Your `after asserts` code must not be empty. If you don't want to add it, remove the tag.",
        exercisePath: exercisePath,
      ),
    );
    expect(
      model.codeAfterAsserts?.language,
      allOf([
        isNot(equals(null)),
        supportedProgrammingLanguages.contains,
      ]),
      reason: _fancyLogger(
        message:
            "Your `after asserts` language code cannot be null or is unsupported. The supported languages are $supportedProgrammingLanguages. Add it after the backticks, for example ```python",
        exercisePath: exercisePath,
      ),
    );
  });

  _testHandler('Verify that the challenge contains valid asserts', () {
    expect(
      model.asserts,
      allOf([
        isNot(equals(null)),
        isNotEmpty,
      ]),
      reason: _fancyLogger(
        message: "The challenge asserts must not be null or empty",
        exercisePath: exercisePath,
      ),
    );
  });

  _testHandler(
      'Verify that the challenge unit tests (asserts) contains the `--err-t{testNumber}--` message',
      () {
    for (var i = 0; i < (model.asserts?.length ?? 0); i++) {
      final errorMessage = '--err-t${i + 1}--';
      final unitTest = model.asserts![i].unitTest;
      expect(
        unitTest,
        contains(errorMessage),
        reason: _fancyLogger(
          message: """
The challenge unit test:
```
$unitTest
```
must contain the error message: $errorMessage""",
          exercisePath: exercisePath,
        ),
      );
    }
  });

  _testHandler('Verify that the challenge contains a valid single solution',
      () {
    expect(
      model.solutions,
      allOf([
        isNot(equals(null)),
        isNotEmpty,
        hasLength(1),
      ]),
      reason: _fancyLogger(
        message:
            "The challenge solution must not be null or empty and must be only one",
        exercisePath: exercisePath,
      ),
    );
  });
}

/// Returns if the provided [entity] is a [File] ending the [.md] extension.
bool isMDFile(FileSystemEntity entity) {
  return entity is File && path.extension(entity.path) == '.md';
}

/// Tells if the exercise is a challenge
///
/// It must take a path like this:
/// `/en/python/challenges/atm.md`
bool isAChallenge(String relativePath) {
  final Uri path = Uri(path: relativePath);
  return path.pathSegments[2] == 'challenges';
}

/// Returns the exercise language, for example for:
/// `/en/python/challenges/atm.md`
///
/// it returns `python`.
String exerciseLanguageFromPath(String relativePath) {
  final Uri path = Uri(path: relativePath);
  return path.pathSegments[1];
}

/// The handler of the test.
///
/// Utility method only to avoid repeating the structure of the test.
void _testHandler(
  String description,
  dynamic Function() body,
) {
  test(description, body, timeout: const Timeout(Duration(seconds: 1)));
}

/// Returns the provided [message] in a fancy way.
///
/// e.g:
/// Given the following message: `Error: something unexpected happened.`
/// The returned message is
/// ```
/// +-----------------------------------+
/// Error: something unexpected happened.
/// | Exercise relative path => /en/c/challenges/hello_world.md |
/// +-----------------------------------+
/// ```
String _fancyLogger({
  required String message,
  required String exercisePath,
}) {
  final lines = message.split('\n');

  // add the exercise path message to the list, to check if this is the longest line
  final exerciseMessage = "Exercise relative path => $exercisePath";
  lines.add(exerciseMessage);

  final maxLineLength = lines.map((e) => e.length).reduce(max);

  return """
+${'-' * maxLineLength}+
 $message
 Exercise relative path => $exercisePath
+${'-' * maxLineLength}+
""";
}