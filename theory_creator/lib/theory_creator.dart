import 'dart:io';

import 'package:parser/parser.dart';
import 'package:path/path.dart';

extension on Object {
  // Used to log easily
  // ignore: avoid_print, unused_element
  void log() => print(toString());
}

/// Returns all the available exercise languages.
List<String> get locales => ['en', 'it'];

Future<void> main() async {
  /// Returns true if the provided [entity] is a [File]
  /// ending with the [.md] extension
  bool isMDFile(FileSystemEntity entity) {
    return entity is File && extension(entity.path) == '.md';
  }

  final parser = MDParserBLoC();

  for (final locale in locales) {
    // Get the language directory.
    final languageDir = Directory('${Directory.current.path}/../$locale');

    // Get all the programming languages
    final programmingLanguages =
        languageDir.listSync(followLinks: false).whereType<Directory>();

    for (final programmingLanguage in programmingLanguages) {
      // Get all the arguments for a programming language
      final argumentsForLanguage = programmingLanguage
          .listSync(followLinks: false)
          .whereType<Directory>()
          .where((e) => basename(e.path) != 'challenges');

      for (final argument in argumentsForLanguage) {
        final theoryContent = StringBuffer();

        // Get all the exercises for an argument
        final exercises = argument.listSync().where(isMDFile);
        for (final exercise in exercises) {
          final exerciseModel = await parser.parse(file: exercise as File);
          // If there isn't a description, stop the iteration.
          if (exerciseModel.description == null) break;

          // Save each theory in the buffer dividing
          // each one with the `---` sign
          if (theoryContent.isNotEmpty) {
            theoryContent.write('\n\n---\n\n');
          }
          theoryContent.write(exerciseModel.description);
        }
        await saveFile(
          result: theoryContent.toString(),
          argumentPath: argument.path,
        );
      }
    }
  }
}

/// Saves the result
Future<void> saveFile({
  required String result,
  required String argumentPath,
}) =>
    File(argumentPath).writeAsString(result);
