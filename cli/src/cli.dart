import 'dart:io';

import 'package:args/args.dart';
import 'package:colorize/colorize.dart';
import 'package:parser/parser.dart';
import 'package:path/path.dart' as path;
import 'package:clippy/server.dart' as clippy;

Future<void> main(List<String> arguments) async {
  exitCode = 0;
  final argsParser = ArgParser()
    ..addSeparator(
        '\nAn useful CLI to text an exercise before submitting it, it formats the exercise to the real code and you can paste it in an editor to try if it works\n')
    ..addFlag('help',
        abbr: 'h', negatable: false, help: "Displays this help information.")
    ..addOption(
      'path',
      help: 'Specity the exercise path, like '
          '"./en/python/variables/1.md"',
      valueHelp: 'path',
      abbr: 'p',
    )
    ..addFlag('copy',
        negatable: true,
        abbr: 'c',
        defaultsTo: true,
        help: 'Automatically copy the output of the exercise in your clipboard')
    ..addFlag('output',
        negatable: false,
        abbr: 'o',
        // defaults to true when the flag `--no-copy` is present
        defaultsTo: arguments.contains('--no-copy'),
        help:
            'Print the output in the console, defaults to true when `--no-copy` is passed, otherwise defaults to false');

  ArgResults argResults = argsParser.parse(arguments);
  final path = argResults['path'];
  final copy = argResults['copy'];
  final help = argResults['help'];
  final printOutput = argResults['output'];

  // print help
  if (help) {
    print(argsParser.usage);
    return;
  }
  if (await FileSystemEntity.isDirectory(path)) {
    stderr.writeln('error: $path is a directory');
    exitCode = 2;
  } else {
    final file = File(path);
    if (!isMDFile(file)) {
      stderr.writeln('error: $path is not an md file');
      exitCode = 2;
      return;
    }

    MDParserBLoC parser = MDParserBLoC();
    final model = await parser.parse(file: file);

    if (model.frontMatterModel.exerciseType != 1) {
      stderr.writeln(
          'error: $path exercise type `${model.frontMatterModel.exerciseType}` is not supported, only type 1 is currently supported');
      exitCode = 2;
      return;
    }

    final fullCode = _getFullCode(model);
    if (printOutput) {
      final colorizedCode = Colorize(fullCode)..lightCyan();
      stdout.writeln(colorizedCode);
    }

    // copy to clipboard
    if (copy) {
      await clippy.write(fullCode);

      if (!printOutput) {
        final coloredText =
            Colorize('exercise code successfully copied to clipboard')..green();
        stdout.writeln(coloredText);
      }
    }
  }
}

/// Returns if the provided [entity] is a [File] ending the [.md] extension.
bool isMDFile(FileSystemEntity entity) {
  return entity is File && path.extension(entity.path) == '.md';
}

String _getFullCode(ExerciseModel model) {
  final codeBeforeSeed = model.beforeSeed?.code;
  final solution = model.solutions?.first;
  final codeAfterSeed = model.afterSeed?.code;

  final codeBeforeHints = model.codeBeforeAsserts?.code;
  final codeAfterHints = model.codeAfterAsserts?.code;
  final allHints = model.asserts
      ?.where((a) => a.unitTest != null)
      .map((a) => a.unitTest)
      .join("\n");
  String fullSourceCode = "";
  if (codeBeforeSeed != null) {
    fullSourceCode += '$codeBeforeSeed\n';
  }
  if (solution != null) {
    fullSourceCode += '$solution\n';
  }

  if (codeAfterSeed != null) {
    fullSourceCode += '\n$codeAfterSeed';
  }

  if (codeBeforeHints != null) {
    fullSourceCode += '\n$codeBeforeHints';
  }
  if (allHints != null) {
    fullSourceCode += '\n$allHints';
  }
  if (codeAfterHints != null) {
    fullSourceCode += '\n$codeAfterHints';
  }
  return fullSourceCode;
}
