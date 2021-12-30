import 'dart:io';

import 'package:args/args.dart';
import 'package:colorize/colorize.dart';
import 'package:parser/parser.dart';
import 'package:path/path.dart' as path;

Future<void> main(List<String> arguments) async {
  exitCode = 0;
  final argsParser = ArgParser()..addFlag('path', negatable: false, abbr: 'p');

  ArgResults argResults = argsParser.parse(arguments);
  final path = argResults.rest.first;

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
    final colorizedCode = Colorize(fullCode)..lightCyan();
    stdout.writeln(colorizedCode);
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
  final allHints = model.asserts?.map((a) => a.unitTest).join("\n");
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
