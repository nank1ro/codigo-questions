import 'dart:io';

import 'package:collection/collection.dart';
import 'package:json_creator/src/models/argument.dart';
import 'package:json_creator/src/models/language.dart';
import 'package:json_creator/src/models/language_locale.dart';
import 'package:json_sorter/json_sorter.dart';
import 'package:parser/parser.dart';
import 'package:path/path.dart';

/// Returns all the available exercise languages.
List<String> get locales => ['en', 'it'];

Future<void> main() async {
  /// Returns if the provided [entity] is a [File] ending the [.md] extension.
  bool isMDFile(FileSystemEntity entity) {
    return entity is File && extension(entity.path) == '.md';
  }

  /// Tells if the exercise is a challenge
  ///
  /// It must take a path like this:
  /// `/en/python/challenges/atm.md`
  bool isAChallenge(String relativePath) {
    final path = Uri(path: relativePath);
    return path.pathSegments.length >= 3 &&
        path.pathSegments[2] == 'challenges';
  }

  /// The relative path of the exercise:

  /// e.g:
  /// `/en/c/challenges/atm.md`
  String _getRelativePath(FileSystemEntity entity) =>
      entity.path.split('..')[1];

  /// Saves the result in a JSON format.
  Future<void> saveResultInJSON(List<LanguageLocale> results) async {
    final resultingMap = <String, dynamic>{
      for (final res in results) res.locale: res.languages,
    };

    final curriculum = File('${Directory.current.path}/../curriculum.json');
    // Prettify the json.
    const encoder = JsonSortedEncoder.withIndent('  ');

    await curriculum.writeAsString(encoder.convert(resultingMap));
  }

  final parser = MDParserBLoC();

  // The resulting json in dart format (converted later).
  final results = <LanguageLocale>[];
  var index = 0;

  for (final locale in locales) {
    // Get the language directory.
    final languageDir = Directory('${Directory.current.path}/../$locale');

    results.add(LanguageLocale(locale: locale));
    // Loop through the locale directory to check for the available languages.
    final sortedFiles = languageDir
        .listSync(
          recursive: true,
        )
        // Skip all non .md files
        .where(isMDFile)
        // Skip the `challenges` folder
        .whereNot((f) => isAChallenge(_getRelativePath(f)))
        .toList()
      ..sort(
        // Sort by file names
        (a, b) => a.path.compareTo(b.path),
      );

    for (final entity in sortedFiles) {
      final relativePath = _getRelativePath(entity);

      final languageName = relativePath.split('/')[2];

      final argumentName = relativePath.split('/')[3];

      final languageIndex =
          results[index].languages.indexWhere((e) => e.name == languageName);

      final exerciseModel = await parser.parse(file: entity as File);

      // If the language is already present, update the data.
      // Otherwise add the new language to the list.
      if (languageIndex != -1) {
        final languageBefore = results[index].languages[languageIndex];

        final argumentIndex = results[index]
            .languages[languageIndex]
            .arguments
            .indexWhere((e) => e.name == argumentName);
        // If the argument is already present, update the data.
        // Otherwise add the new argument to the list.
        if (argumentIndex != -1) {
          final argumentBefore =
              results[index].languages[languageIndex].arguments[argumentIndex];

          final updatedArgument = argumentBefore.copyWith(
            totalExercises: argumentBefore.totalExercises + 1,
            trainUntil: argumentBefore.trainUntil +
                (exerciseModel.description != null ? 1 : 0),
          );
          final updatedLanguage = languageBefore.copyWith(
            totalExercises: languageBefore.totalExercises + 1,
            arguments: [
              for (final arg in languageBefore.arguments)
                if (arg.name == argumentName) updatedArgument else arg
            ],
          );
          results[index] = results[index].copyWith(
            languages: [
              for (final language in results[index].languages)
                if (language.name == languageName) updatedLanguage else language
            ],
          );
        } else {
          final languageBefore = results[index].languages[languageIndex];
          final updatedLanguage = languageBefore.copyWith(
            arguments: [
              ...languageBefore.arguments,
              Argument(
                name: argumentName,
                trainUntil: exerciseModel.description != null ? 1 : 0,
                totalExercises: 1,
              ),
            ],
            totalExercises: languageBefore.totalExercises + 1,
          );
          results[index] = results[index].copyWith(
            languages: [
              for (final language in results[index].languages)
                if (language.name == languageName) updatedLanguage else language
            ],
          );
        }
      } else {
        results[index] = results[index].copyWith(
          languages: [
            ...results[index].languages,
            Language(
              name: languageName,
              arguments: [
                Argument(
                  name: argumentName,
                  totalExercises: 1,
                  trainUntil: exerciseModel.description != null ? 1 : 0,
                ),
              ],
              totalExercises: 1,
            )
          ],
        );
      }
    }
    index++;
  }
  await saveResultInJSON(results);
}
