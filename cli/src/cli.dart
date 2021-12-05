import 'dart:io';

import 'package:args/args.dart';
import 'package:colorize/colorize.dart';
import 'package:parser/parser.dart';

Future<void> main(List<String> arguments) async {
  exitCode = 0;
  final argsParser = ArgParser()..addFlag('path', negatable: false, abbr: 'p');

  ArgResults argResults = argsParser.parse(arguments);
  final path = argResults.rest.first;

  print(path);

  if (await FileSystemEntity.isDirectory(path)) {
    stderr.writeln('error: $path is a directory');
    exitCode = 2;
  } else {
    final file = File(path);

    MDParserBLoC parser = MDParserBLoC();
    final model = await parser.parse(file: file);
    final fullCode = _getFullCode(model);
    final colorizedCode = Colorize(fullCode)..lightCyan();
    stdout.writeln(colorizedCode);
  }
}

String _getFullCode(ExerciseModel model) {
  final codeBeforeSeed = model.beforeSeed?.code;
  final seedCode = model.seed?.code;
  final codeAfterSeed = model.afterSeed?.code;

  final codeBeforeHints = model.codeBeforeAsserts?.code;
  final codeAfterHints = model.codeAfterAsserts?.code;
  final allHints = model.asserts?.map((a) => a.unitTest).join("\n");
  String fullSourceCode = "";
  if (codeBeforeSeed != null) {
    fullSourceCode += '$codeBeforeSeed\n';
  }
  if (seedCode != null) {
    fullSourceCode += '$seedCode\n';
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
