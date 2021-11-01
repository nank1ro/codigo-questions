import 'dart:io';

import 'package:json_creator/src/models/argument.dart';
import 'package:json_creator/src/models/language.dart';
import 'package:json_creator/src/models/language_locale.dart';
import 'package:parser/parser.dart';
import 'package:path/path.dart';

/// Returns all the available exercise languages.
List<String> get locales => ['en', 'it'];

Future<void> main() async {
  /// The relative path of the exercise:

  /// e.g:
  /// `/en/c/challenges/atm.md`
  String _getRelativePath(FileSystemEntity entity) =>
      entity.path.split('..')[1];

  /// Saves the result in a JSON format.
  Future<void> saveResultInJSON(List<LanguageLocale> results) async {
    for (var i = 0; i < results.length; i++) {
      final res = results[i];
      var resultingJsonString = '${res.locale}: ${res.languages}';

// If it's not the last index, add a comma after the locale.
      if (i != results.length - 1) {
        resultingJsonString += ',';
      }

      final curriculum = File('${Directory.current.path}/../curriculum.json');
      await curriculum.writeAsString(resultingJsonString);
    }
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
    await for (final entity in languageDir.list(
      recursive: true,
    )) {
      // Skip directories
      if (entity is Directory) continue;
      // Skip all .txt files cause the're deprecated
      if (extension(entity.path) == '.txt') continue;

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
