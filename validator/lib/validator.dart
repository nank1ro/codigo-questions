import 'dart:convert';
import 'dart:io';
import 'dart:math';

import 'package:diff_match_patch/diff_match_patch.dart';
import 'package:parser/parser.dart';
import 'package:path/path.dart' as path;
import 'package:test/test.dart';
import 'package:trotter/trotter.dart';
import 'package:validator/constants.dart';

/// Returns all the available exercise languages.
List<String> get locales => ['en', 'it'];

/// The list of currently supported programming languages
const supportedProgrammingLanguages = <String>{
  'python',
  'swift',
  'javascript',
  'c',
  'kotlin',
};

final RegExp _codeSpaceRegex = RegExp(r'\[\/\]', dotAll: true);

Future<void> main() async {
  final parser = MDParserBLoC();

  final argumentAssetsDir =
      Directory('${Directory.current.path}/../assets/arguments');
  final challengesAssetsDir =
      Directory('${Directory.current.path}/../assets/challenges');
  for (final lang in locales) {
    // Get the language directory.
    final langDir = Directory('${Directory.current.path}/../$lang');

    for (final language in supportedProgrammingLanguages) {
      // Get the language directory.
      final languageDir = Directory('${langDir.path}/$language');

      await _validateDataJson(directory: languageDir);

      await _validateLanguageAssets(
          assetsDir: argumentAssetsDir, targetDir: languageDir);

      final challengeDirectories = languageDir
          .listSync(followLinks: false)
          .whereType<Directory>()
          .where((e) => getFileNameWithoutExtension(e.path) == 'challenges');

      for (final dir in challengeDirectories) {
        await _validateChallengeAssets(
            assetsDir: challengesAssetsDir, targetDir: dir);
      }
    }

    // List directory contents, recursing into sub-directories,
    // but not following symbolic links.
    await for (final entity in langDir.list(
      recursive: true,
      followLinks: false,
    )) {
      final relativePath = getRelativePath(entity);
      if (isAnExerciseDirectory(entity, relativePath)) {
        await _validateExerciseDirectory(
          directory: entity as Directory,
          relativePath: relativePath,
          parser: parser,
        );
      } else if (isExerciseFile(entity)) {
        /* if (relativePath == '/it/javascript/objects/1.md') { */
        final exerciseModel = await parser.parse(file: entity as File);
        _validateExercise(
          exerciseModel: exerciseModel,
          exercisePath: relativePath,
        );
        /* } */
      }
    }
  }
}

Iterable<String> _getSvgAssetNames(Directory assetsDir) {
  final assets = assetsDir
      .listSync(followLinks: false)
      .where((e) => path.extension(e.path) == '.svg');
  return assets.map((e) => getFileNameWithoutExtension(e.path));
}

Future<void> _validateLanguageAssets({
  required Directory assetsDir,
  required Directory targetDir,
}) async {
  final assetNames = _getSvgAssetNames(assetsDir);
  final arguments =
      targetDir.listSync(followLinks: false).whereType<Directory>().where(
            (e) => getFileNameWithoutExtension(e.path) != 'challenges',
          );
  final argumentNames =
      arguments.map((e) => getFileNameWithoutExtension(e.path));
  for (final argumentName in argumentNames) {
    _testHandler('''Verify that argument asset is present''', () {
      final errorDir = Directory('${targetDir.path}/$argumentName.md');
      expect(
        assetNames,
        contains(argumentName),
        reason: _fancyLogger(
          message:
              '''The argument asset `$argumentName` is not present in the `assets` folder''',
          exercisePath: getRelativePath(errorDir),
        ),
      );
    });
  }
}

Future<void> _validateChallengeAssets({
  required Directory assetsDir,
  required Directory targetDir,
}) async {
  final assetNames = _getSvgAssetNames(assetsDir);
  final challenges =
      targetDir.listSync(followLinks: false).where(isExerciseFile);
  final challengeNames =
      challenges.map((e) => getFileNameWithoutExtension(e.path));

  for (final challengeName in challengeNames) {
    _testHandler('''Verify that challenge asset is present''', () {
      final errorDir = Directory('${targetDir.path}/$challengeName.md');
      expect(
        assetNames,
        contains(challengeName),
        reason: _fancyLogger(
          message:
              '''The challenge asset `$challengeName` is not present in the `assets` folder''',
          exercisePath: getRelativePath(errorDir),
        ),
      );
    });
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

  if (exerciseModel.frontMatterModel.exerciseType == 1) {
    _runCodeTests(
      exercisePath: exercisePath,
      model: exerciseModel,
    );
  } else if (exerciseModel.frontMatterModel.exerciseType == 2) {
    _runFillInEmptySpacesTests(
      model: exerciseModel,
      exercisePath: exercisePath,
    );
  } else if (exerciseModel.frontMatterModel.exerciseType == 3) {
    _runChooseAnAnswerTests(
      model: exerciseModel,
      exercisePath: exercisePath,
    );
  } else if (exerciseModel.frontMatterModel.exerciseType == 4) {
    _runSortItemsTests(
      exercisePath: exercisePath,
      model: exerciseModel,
    );
  }

  _validateSolutions(
    exerciseType: exerciseModel.frontMatterModel.exerciseType,
    solutions: exerciseModel.solutions,
    exercisePath: exercisePath,
  );
}

/// Validates the Run Code exercises
void _runCodeTests({
  required String exercisePath,
  required ExerciseModel model,
}) {
  _testHandler(
      '''Verify that run-code exercise contains at least an assert or an output''',
      () {
    expect(
      [model.asserts, model.output],
      isNot(equals([null, null])),
      reason: _fancyLogger(
        message:
            '''The run-code exercise must contain at least an assert or an output to validate it''',
        exercisePath: exercisePath,
      ),
    );
  });
  final languageName = model.frontMatterModel.language;

  if (!requiredRunCodeExerciseCodes.containsKey(languageName)) return;
  final requiredCode = requiredRunCodeExerciseCodes[languageName];

  if (model.asserts?.isNotEmpty ?? false) {
    final beforeSeed = requiredCode![kBeforeSeedTag]!;
    final afterAsserts = requiredCode[kAfterAssertsTag]!;
    if (model.beforeSeed?.code != null ||
        model.codeBeforeAsserts?.code != null) {
      _testHandler(
          '''Verify that the `$languageName` RunCode exercise, contains the intestation in the before-seed or before-asserts tag''',
          () {
        final hasContent = [
          model.beforeSeed?.code,
          model.codeBeforeAsserts?.code
        ].any((c) => c != null && c.contains(beforeSeed));

        expect(
          hasContent,
          equals(true),
          reason: _fancyLogger(
            message: '''
You must provide the 
```
$beforeSeed
````
 lines of code inside the before-seed tag''',
            exercisePath: exercisePath,
          ),
        );
      });
    }

    _testHandler('''
Verify that the `$languageName` RunCode exercise, contains the end of intestation in the after-asserts tag''',
        () {
      expect(
        model.codeAfterAsserts?.code,
        contains(afterAsserts),
        reason: _fancyLogger(
          message: '''
You must provide the
```
$cAfterAssertsCode
```
lines of code in the after-asserts tag''',
          exercisePath: exercisePath,
        ),
      );
    });
  }
}

/// Validates all the solutions
void _validateSolutions({
  required int exerciseType,
  required String exercisePath,
  List<String>? solutions,
}) {
  _testHandler('Verify that there is at least one solution', () {
    expect(
      solutions,
      isNotEmpty,
      reason: _fancyLogger(
        message: 'You must provide a solution for each exercise',
        exercisePath: exercisePath,
      ),
    );
  });
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
        message: '''
The language provided `$language` is not supported, the currently supported languages are: $supportedProgrammingLanguages.''',
        exercisePath: exercisePath,
      ),
    );
  });

  final languageFromPath = exerciseLanguageFromPath(exercisePath);
  _testHandler('''
Verify that the language is the same to the language retrieved from the exercise path''',
      () {
    expect(
      languageFromPath,
      equals(language),
      reason: _fancyLogger(
        message: '''
The language provided `$language` is different from the one retrieved from the exercise path: `$languageFromPath`. Did you put the exercise in the correct location?''',
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
        message: '''
The exercise provided `$exerciseType` is not supported, the currently supported exercise types are: $_supportedExerciseTypes''',
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
              'You have to provide a `difficulty` inside the front matter.',
          exercisePath: exercisePath,
        ),
      );
      expect(
        _supportedExerciseDifficulties,
        contains(frontMatterModel.difficulty),
        reason: _fancyLogger(
          message: '''
The difficulty provided `${frontMatterModel.difficulty}` is not supported, the currently supported difficulties are: $_supportedExerciseDifficulties''',
          exercisePath: exercisePath,
        ),
      );
    });

    _testHandler('Verify that the challenge contains a title', () {
      expect(
        frontMatterModel.title,
        isNot(equals(null)),
        reason: _fancyLogger(
          message: 'You have to provide a `title` to the challenge',
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
        message: 'You have to provide a `description` to the challenge',
        exercisePath: exercisePath,
      ),
    );
  });

  _testHandler('Verify that the challenge contains instructions', () {
    expect(
      model.instructions?.trim(),
      isNotEmpty,
      reason: _fancyLogger(
        message: 'You have to provide `instructions` to the challenge',
        exercisePath: exercisePath,
      ),
    );
  });

  _testHandler('Verify that the challenge contains a valid seed', () {
    expect(
      model.seed?.code,
      isNotEmpty,
      reason: _fancyLogger(
        message: 'You have to provide a `seed` to the challenge',
        exercisePath: exercisePath,
      ),
    );
    expect(
      model.seed?.language,
      supportedProgrammingLanguages.contains,
      reason: _fancyLogger(
        message: '''
You have to provide a supported language code to the `seed`. The supported languages are $supportedProgrammingLanguages''',
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
        message: """
Your `before asserts` code must not be empty. If you don't want to add it, remove the tag.""",
        exercisePath: exercisePath,
      ),
    );

    if (model.codeBeforeAsserts != null) {
      expect(
        model.codeBeforeAsserts?.language,
        allOf([
          isNot(equals(null)),
          supportedProgrammingLanguages.contains,
        ]),
        reason: _fancyLogger(
          message: '''
Your `before asserts` language code cannot be null or is unsupported. The supported languages are $supportedProgrammingLanguages. Add it after the backticks, for example ```python''',
          exercisePath: exercisePath,
        ),
      );
    }
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
        message: """
Your `after asserts` code must not be empty. If you don't want to add it, remove the tag.""",
        exercisePath: exercisePath,
      ),
    );
    if (model.codeAfterAsserts != null) {
      expect(
        model.codeAfterAsserts?.language,
        allOf([
          isNot(equals(null)),
          supportedProgrammingLanguages.contains,
        ]),
        reason: _fancyLogger(
          message: '''
Your `after asserts` language code cannot be null or is unsupported. The supported languages are $supportedProgrammingLanguages. Add it after the backticks, for example ```python''',
          exercisePath: exercisePath,
        ),
      );
    }
  });

  _testHandler('Verify that the challenge contains valid asserts', () {
    expect(
      model.asserts,
      allOf([
        isNot(equals(null)),
        isNotEmpty,
      ]),
      reason: _fancyLogger(
        message: 'The challenge asserts must not be null or empty',
        exercisePath: exercisePath,
      ),
    );
  });

  if (model.frontMatterModel.language != 'c' &&
      model.frontMatterModel.language != 'javascript') {
    _testHandler('''
Verify that the challenge unit tests (asserts) contains the `--err-t{testNumber}--` message''',
        () {
      for (var i = 0; i < (model.asserts?.length ?? 0); i++) {
        final errorMessage = '--err-t${i + 1}--';
        final unitTest = model.asserts![i].unitTest;
        expect(
          unitTest,
          contains(errorMessage),
          reason: _fancyLogger(
            message: '''
The challenge unit test:
```
$unitTest
```
must contain the error message: $errorMessage''',
            exercisePath: exercisePath,
          ),
        );
      }
    });
  }

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
        message: '''
The challenge solution must not be null or empty and must be only one''',
        exercisePath: exercisePath,
      ),
    );
  });
}

void _runFillInEmptySpacesTests({
  required ExerciseModel model,
  required String exercisePath,
}) {
  _testHandler(
      'Verify that the exercise can be completed successfully with the answers provided',
      () {
    final answers = model.answers!;
    final seed = model.seed!.code;
    final solutions = model.solutions!;
    final emptySpacesCount = _codeSpaceRegex.allMatches(seed).length;
    final emptySpacesMatches = _codeSpaceRegex.allMatches(seed).toList();

    /// Returns all the empty spaces' start position.
    /// ? Each `[/]` is counted as a single char.
    /// e.g.:
    /// `[/][/]` -> [0, 1]
    /// `[/]code[/]`-> [0, 5]
    List<int> getEmptySpacesPosition() {
      final positions = <int>[];
      for (var i = 0; i < emptySpacesMatches.length; i++) {
        final curr = emptySpacesMatches[i];
        if (positions.isEmpty) {
          positions.add(curr.start);
        } else {
          positions.add(curr.start - (2 * positions.length));
        }
      }
      return positions..sort();
    }

    /// Returns true if the are two empty spaces that touch each other, e.g:
    /// `[/][/] some code` -> true
    /// `[/]some code[/]` -> false
    bool hasNearbyEmptySpaces() {
      final positions = getEmptySpacesPosition();
      return positions.any(
        (p) => positions.contains(p - 1) || positions.contains(p + 1),
      );
    }

    /// Returns the list of differences between the solution and the
    /// seed without empty spaces.
    List<String> getDifferences(String solution) {
      final seedWithoutEmptySpaces = seed.replaceAll(_codeSpaceRegex, '');

      final differences = diff(solution, seedWithoutEmptySpaces);

      return differences
          .where((d) => d.operation == -1)
          .map((e) => e.text)
          .toList();
    }

    /// Returns true if the answers fill correctly and compose a solution equal
    /// to one available
    bool checkIfAnswersFillCorrectly(List<String> answers, String solution) {
      var filledSeed = seed;
      for (final answer in answers) {
        filledSeed = filledSeed.replaceFirst(_codeSpaceRegex, answer);
      }
      return filledSeed == solution;
    }

    /// * This method is slower that the counterpart, because
    /// * it uses permutations to find the correct order of the answers
    /// * needed to complete the exercise successfully.
    bool validateEmptySpacesNearby() {
      var exerciseIsValid = false;

      for (final solution in solutions) {
        exerciseIsValid = false;
        final expectedAnswers = <String>[];
        final availableAnswers = [...answers];

        Map<int, int> groupEmptySpacePositions() {
          final emptyPositions = getEmptySpacesPosition();
          final answersPerGroup = <int, int>{
            emptyPositions.first: 1,
          };
          var lastAddedIndex = emptyPositions.first;
          for (var i = 1; i < emptyPositions.length; i++) {
            final curr = emptyPositions[i];
            final prev = emptyPositions[i - 1];

            if (prev + 1 != curr) {
              lastAddedIndex = curr;
            }

            answersPerGroup.update(
              lastAddedIndex,
              (value) => value + 1,
              ifAbsent: () => 1,
            );
          }
          return answersPerGroup;
        }

        final groupedEmptySpacePositions = groupEmptySpacePositions();

        final differences = getDifferences(solution);

        assert(differences.length == groupedEmptySpacePositions.length,
            'The differences found in the exercise are more than the empty spaces in $exercisePath');

        var differenceIndex = 0;
        for (final entry in groupedEmptySpacePositions.entries) {
          final answersCount = entry.value;
          final difference = differences[differenceIndex];

          final possibleAnswers =
              availableAnswers.where(difference.contains).toList();

          assert(answersCount <= possibleAnswers.length,
              "There are more answers than possibilities in $exercisePath");

          final indexes =
              List.generate(possibleAnswers.length, (index) => index);
          final permutations = Permutations(answersCount, indexes);

          for (final combo in permutations()) {
            final finalAnswers = <String>[];
            for (final c in combo) {
              finalAnswers.add(possibleAnswers[c]);
            }

            if (difference == finalAnswers.join()) {
              expectedAnswers.addAll(finalAnswers);
              for (final c in combo) {
                availableAnswers.remove(possibleAnswers[c]);
              }
              differenceIndex++;
              break;
            }
          }
        }

        if (expectedAnswers.length == emptySpacesCount) {
          exerciseIsValid =
              checkIfAnswersFillCorrectly(expectedAnswers, solution);
        }

        // Solution found, stop the iteration over the next solution.
        if (exerciseIsValid) break;
      }

      return exerciseIsValid;
    }

    /// * This method is faster that the counterpart, because
    /// * it simply finds the answers from the solution.
    bool validateEmptySpacesNotNearby() {
      var exerciseIsValid = false;

      for (final solution in solutions) {
        exerciseIsValid = false;
        // Gets the difference between the solution and the seed
        final differences = getDifferences(solution);
        final expectedAnswers = <String>[];
        final availableAnswers = [...answers];

        for (final dif in differences) {
          // If there is a difference, it should be an answer, check if the
          // [availableAnswers] contains it and remove it.
          // In case the answer is not present, the exercise is not valid.
          expectedAnswers.add(dif);
          if (availableAnswers.contains(dif)) {
            availableAnswers.remove(dif);
          } else {
            exerciseIsValid = false;
            break;
          }
        }
        // Solution found, stop the iteration over the next solution.

        exerciseIsValid =
            checkIfAnswersFillCorrectly(expectedAnswers, solution);
        if (exerciseIsValid) break;
      }

      return exerciseIsValid;
    }

    bool hasValidCombo() {
      final hasNearbySpaces = hasNearbyEmptySpaces();
      if (hasNearbySpaces) return validateEmptySpacesNearby();
      return validateEmptySpacesNotNearby();
    }

    expect(
      hasValidCombo(),
      equals(true),
      reason: _fancyLogger(
        message:
            'The exercise cannot be completed successfully with the answers provided',
        exercisePath: exercisePath,
      ),
    );
  });
}

void _runChooseAnAnswerTests({
  required ExerciseModel model,
  required String exercisePath,
}) {
  _testHandler(
      'Verify that the exercise can be completed successfully with the solutions provided',
      () {
    final solutionsAreValid =
        model.solutions!.every((s) => model.answers!.contains(s));
    expect(
      solutionsAreValid,
      equals(true),
      reason: _fancyLogger(
        message:
            'The exercise cannot be completed successfully with the solutions provided',
        exercisePath: exercisePath,
      ),
    );
  });
}

void _runSortItemsTests({
  required ExerciseModel model,
  required String exercisePath,
}) {
  _testHandler('Verify that the sort items exercise contains some answers', () {
    expect(
      model.answers,
      allOf([
        isNot(equals(null)),
        isNotEmpty,
      ]),
      reason: _fancyLogger(
        message: 'The sort items exercise answers must not be null or empty',
        exercisePath: exercisePath,
      ),
    );
  });

  _testHandler('Verify that the sort items exercise contains valid answers',
      () {
    bool checkValidity() {
      final solutions = model.solutions!;
      final answers = model.answers!;
      var isValid = false;

      for (final solution in solutions) {
        var _sol = solution;
        for (final answer in answers) {
          // Remove all the answer from the solution
          _sol = _sol.replaceFirst(answer, '');
        }
        // Remove also all the new lines
        _sol = _sol.replaceAll('\n', '');
        if (_sol.isEmpty) {
          isValid = true;
          break;
        }
      }
      return isValid;
    }

    expect(
      checkValidity(),
      equals(true),
      reason: _fancyLogger(
        message:
            'The sort items exercise cannot be completed with the answers provided',
        exercisePath: exercisePath,
      ),
    );
  });
}

/// Checks if the directory has a consisten structure of the files.
Future<void> _validateExerciseDirectory({
  required Directory directory,
  required String relativePath,
  required MDParserBLoC parser,
}) async {
  final files = directory.listSync(followLinks: false);
  final totalMDFiles = files.where(isExerciseFile).toList()
    // Sort the files
    ..sort(
      (a, b) => int.parse(getFileNameWithoutExtension(a.path)).compareTo(
        int.parse(
          getFileNameWithoutExtension(b.path),
        ),
      ),
    );

  // A map with the file name `1.md` with a boolean indicating
  // if the file has a description or not.
  final filesHaveDescription = <String, bool>{};

  for (var i = 0; i < totalMDFiles.length; i++) {
    final fileName = path.basename(totalMDFiles[i].path);

    final exerciseModel = await parser.parse(file: totalMDFiles[i] as File);
    filesHaveDescription[fileName] = exerciseModel.description != null;

    _testHandler('Verify that the MD files are in order', () {
      expect(
        fileName,
        equals('${i + 1}.md'),
        reason: _fancyLogger(
          message: '''
The MD files must be in order, for example:
[1.md, 2.md, 3.md]

But the file `$fileName` is not in order.
''',
          exercisePath: relativePath,
        ),
      );
    });
  }

  final entries = filesHaveDescription.entries.toList();
  for (var i = 0; i < filesHaveDescription.length - 1; i++) {
    final entry = entries[i];
    final currentHasDescription = entry.value;

    final nextEntry = entries[i + 1];
    final nextHasDescription = nextEntry.value;

    _testHandler('''
Verify that the exercises with a description come before the ones without''',
        () async {
      expect(
        [currentHasDescription, nextHasDescription],
        isNot(
          equals(
            [false, true],
          ),
        ),
        reason: _fancyLogger(
          message: '''
The exercises with a description must be put before the ones without.
But `${entry.key}` doesn't have a description while ${nextEntry.key} has one.
''',
          exercisePath: relativePath,
        ),
      );
    });
  }
}

Future<Iterable<String>> _getArgumentsInPath(String path) async {
  final dataFile = File('$path/data.json');

  final jsonString = await dataFile.readAsString();
  final json = jsonDecode(jsonString) as Map<String, dynamic>;

  return json.keys;
}

Future<void> _validateDataJson({
  required Directory directory,
}) async {
  final subDirectories =
      directory.listSync(followLinks: false).whereType<Directory>();

  for (final dir in subDirectories) {
    final argumentOfDir = getFileNameWithoutExtension(dir.path);
    if (argumentOfDir == 'challenges') {
      final challenges = await _getArgumentsInPath(dir.path);
      final files = dir.listSync(followLinks: false).where(isExerciseFile);
      for (final file in files) {
        final challengeName = getFileNameWithoutExtension(file.path);
        _testHandler('''
Verify that the challenge is defined in the data.json file''', () async {
          expect(
            challenges,
            contains(challengeName),
            reason: _fancyLogger(
              message: '''
The challenge `$challengeName` has not been declared in the `data.json` file.
''',
              exercisePath: dir.path,
            ),
          );
        });
      }
    } else {
      final arguments = await _getArgumentsInPath(directory.path);
      _testHandler('''
Verify that the argument is defined in the data.json file''', () async {
        expect(
          arguments,
          contains(argumentOfDir),
          reason: _fancyLogger(
            message: '''
The argument `$argumentOfDir` has not been declared in the `data.json` file.
''',
            exercisePath: dir.path,
          ),
        );
      });
    }
  }
}

/// Returns if the provided [entity] is an exercise [Directory]
bool isAnExerciseDirectory(FileSystemEntity entity, String relativePath) {
  return entity is Directory && !isAChallenge(relativePath);
}

/// Returns if the provided [entity] is a [File] named with a number that ends
/// with the [.md] extension.
bool isExerciseFile(FileSystemEntity entity) {
  return entity is File &&
      path.extension(entity.path) == '.md' &&
      int.tryParse(path.basenameWithoutExtension(entity.path)) != null;
}

/// The relative path of the exercise:

/// e.g:
/// `/en/c/challenges/atm.md`
String getRelativePath(FileSystemEntity entity) => entity.path.split('..')[1];

/// Tells if the exercise is a challenge
///
/// It must take a path like this:
/// `/en/python/challenges/atm.md`
bool isAChallenge(String relativePath) {
  final path = Uri(path: relativePath);
  return path.pathSegments.length >= 3 && path.pathSegments[2] == 'challenges';
}

/// Returns the file name, see [path.basename]
String getFileName(String filePath) => path.basename(filePath);

/// Returns the file name without the extension, see [path.basename]
String getFileNameWithoutExtension(String filePath) =>
    getFileName(filePath).split('.').first;

/// Returns the exercise language, for example for:
/// `/en/python/challenges/atm.md`
///
/// it returns `python`.
String exerciseLanguageFromPath(String relativePath) {
  final path = Uri(path: relativePath);
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

  // add the exercise path message to the list,
  // to check if this is the longest line
  final exerciseMessage = 'Exercise relative path => $exercisePath';
  lines.add(exerciseMessage);

  final maxLineLength = lines.map((e) => e.length).reduce(max);

  return """
+${'-' * maxLineLength}+
 $message
 Exercise relative path => $exercisePath
+${'-' * maxLineLength}+
""";
}
