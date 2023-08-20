import 'dart:convert';
import 'dart:io';

import 'package:parser/src/blocs/models/assert_model/model.dart';
import 'package:parser/src/blocs/models/code_model/model.dart';
import 'package:parser/src/blocs/models/exercise_model/model.dart';
import 'package:parser/src/blocs/models/frontmatter_model/model.dart';
import 'package:parser/src/services/front_matter_parser_service.dart';

export 'models/assert_model/model.dart';
export 'models/code_model/model.dart';
export 'models/exercise_model/model.dart';
export 'models/frontmatter_model/model.dart';

// ignore_for_file: public_member_api_docs
const String kDescriptionTag = '# --description--';
const String kInstructionsTag = '# --instructions--';
const String kAssertsTag = '# --asserts--';
const String kBeforeSeedTag = '# --before-seed--';
const String kSeedTag = '# --seed--';
const String kAfterSeedTag = '# --after-seed--';
const String kSolutionsTag = '# --solutions--';
const String kAnswersTag = '# --answers--';
const String kBeforeAssertsTag = '# --before-asserts--';
const String kAfterAssertsTag = '# --after-asserts--';
const String kOutputTag = '# --output--';
final RegExp languageCodeRegex = RegExp('(?<=```).+');

/// Parses the md `fileContent`  with its [parse] method,
/// returning an `exerciseModel`.
class MDParserBLoC {
  final FrontMatterParserService _frontMatterParserService =
      const FrontMatterParserService();

  late String filePath;

  /// Parses the entire [file] and returns the
  /// `ExerciseModel` with all the retrieved data.
  Future<ExerciseModel> parse({
    /// The content of the MD file.
    required File file,
  }) async {
    if (file.path.contains('..')) {
      filePath = file.path.split('..')[1];
    } else {
      filePath = file.path;
    }

    final frontMatterModel = await _parseFrontMatter(file.path);

    final fileContent = await _getContentFromFile(file);

    final description = _getContentBetweenTag(
      tag: kDescriptionTag,
      fullContent: fileContent,
    );

    final instructions = _getContentBetweenTag(
      tag: kInstructionsTag,
      fullContent: fileContent,
    );

    final output = _getContentBetweenTag(
      tag: kOutputTag,
      fullContent: fileContent,
    );

    final beforeSeed =
        _getCodeBetweenTag(fileContent: fileContent, tag: kBeforeSeedTag);

    final seed = _getCodeBetweenTag(fileContent: fileContent, tag: kSeedTag);

    final afterSeed =
        _getCodeBetweenTag(fileContent: fileContent, tag: kAfterSeedTag);

    final codeBeforeAsserts =
        _getCodeBetweenTag(fileContent: fileContent, tag: kBeforeAssertsTag);

    final codeAfterAsserts =
        _getCodeBetweenTag(fileContent: fileContent, tag: kAfterAssertsTag);

    final asserts = _getAssertsFromContent(fileContent);

    final answers = _getAnswersFromContent(
      content: fileContent,
    );

    final solutions = _getSolutionsFromContent(fileContent);

    return ExerciseModel(
      frontMatterModel: frontMatterModel,
      description: description,
      instructions: instructions,
      seed: seed,
      asserts: asserts,
      codeBeforeAsserts: codeBeforeAsserts,
      codeAfterAsserts: codeAfterAsserts,
      output: output,
      answers: answers is List<String> ? answers : null,
      answersCodeBlocks: answers is List<CodeModel> ? answers : null,
      solutions: solutions,
      beforeSeed: beforeSeed,
      afterSeed: afterSeed,
    );
  }

  /// Parses the frontmatter returning a [FrontMatterModel].
  Future<FrontMatterModel> _parseFrontMatter(String filePath) async {
    final json = await _frontMatterParserService.parseFile(filePath);
    return FrontMatterModel.fromJson(json);
  }

  /// Returns the content of the file as a [String].
  Future<String> _getContentFromFile(File file) async {
    final contents = await file.readAsLines();
    return contents.join('\n');
  }

  /// Returns the content between the provided tags
  ///
  /// The tags are intented in the following format:
  /// # --{tag}--
  ///
  /// e.g.:
  /// Given the following content:
  /// # --description--
  ///
  /// Some description
  ///
  /// the method called with the `description` tag will return:
  /// Some description
  String? _getContentBetweenTag({
    required String tag,
    required String fullContent,
  }) {
    final startIndex = fullContent.indexOf(tag);
    if (startIndex == -1) return null;
    const end = '# --';
    final endIndex = fullContent.indexOf(end, startIndex + tag.length);
    final content = fullContent.substring(
      startIndex + tag.length,
      endIndex != -1 ? endIndex : fullContent.length,
    );
    return content.trimNewLines();
  }

  /// Returns the list of asserts (if any) from the provided [fileContent].
  List<AssertModel>? _getAssertsFromContent(String fileContent) {
    final assertsContent = _getContentBetweenTag(
      tag: kAssertsTag,
      fullContent: fileContent,
    );
    if (assertsContent == null) return null;

    final descriptions = _getListOfContentBetweenBackticks(
      content: assertsContent,
      skipHeadings: false,
    );
    final unitTests = _getListOfContentBetweenBackticks(
      content: assertsContent,
      skipHeadings: true,
    );

    assert(
      descriptions.length == unitTests.length,
      '''
Asserts and unit tests must have the same length. Did you provide both the description and the unit test?
Exercise file path: $filePath
      ''',
    );

    return List.generate(
      unitTests.length,
      (i) {
        final unitTest = unitTests[i];
        return AssertModel(
          description: descriptions[i],
          unitTest: isRegexAssert(unitTest) ? null : unitTest,
          regexAssert: isRegexAssert(unitTest)
              ? RegexAssert.fromJson(
                  jsonDecode(unitTest) as Map<String, dynamic>,
                )
              : null,
        );
      },
    );
  }

  bool isRegexAssert(String unitTest) {
    try {
      final json = jsonDecode(unitTest);
      if (json is Map &&
          json.containsKey('regex') &&
          json.containsKey('modifiers') &&
          json.containsKey('shouldMatch')) {
        return true;
      } else {
        return false;
      }
    } catch (_) {
      return false;
    }
  }

  /// Returns a list of content that is divided by backticks:
  /// e.g:
  /// Given this content:
  /// The function should return "Hello, World!".

  /// ```
  ///     def test_say_hi(self):
  ///         self.assertEqual(hello(), "Hello, World!", "--err-t1--")
  /// ```
  ///
  /// if this method is called with [skipHeadings] set to `false`, then
  /// the return List is: `[The function should return "Hello, World!".]`
  ///
  /// Otherwise, if the [skipHeadings] is set to true, the returned List is:
  // ignore: comment_references
  /// `[def test_say_hi(self):
  ///      self.assertEqual(hello(), "Hello, World!", "--err-t1--")]`
  List<String> _getListOfContentBetweenBackticks({
    required String content,
    // tells if the description above the code has to be skipped
    required bool skipHeadings,
  }) {
    final split = content.split('\n');

    final result = <int, String>{};

    var skip = skipHeadings;

    var index = 0;
    for (final val in split) {
      final containsCodeOperator = val.contains('```');
      if (containsCodeOperator) {
        skip = !skip;
      }
      if (!skip && !containsCodeOperator) {
        final encodedValue = _parseToUtf8(val);
        result.update(
          index,
          (prev) => '$prev\n$encodedValue',
          ifAbsent: () => encodedValue,
        );
      } else if (skip) {
        index++;
      }
    }

    return result.values.toList();
  }

  /// Parses the string with the UTF8 encoding.
  String _parseToUtf8(String input) {
    final encoded = utf8.encode(input);
    return utf8.decode(encoded);
  }

  /// Returns the language declared in the code, in order to highlight
  /// it properly.
  ///
  /// e.g. => given this code:
  /// ```javascript
  /// console.log("Hello");
  /// ```
  ///
  /// will return `javascript`.
  String? getLanguageFromCode(String code) =>
      languageCodeRegex.firstMatch(code)?.group(0);

  /// Returns the code between the provided [tag] and the
  /// backticks (```).
  /// e.g:
  /// Given the following content
  ///
  /// # --seed--
  ///
  /// ```python
  /// def hello():
  ///     pass
  /// ```
  ///
  /// the method called with `seed` as tag returns:
  /// CodeModel(
  ///   language: "python",
  ///   code: "def hello():
  ///     pass"
  /// )
  CodeModel? _getCodeBetweenTag({
    required String fileContent,
    required String tag,
  }) {
    if (!fileContent.contains(tag)) return null;
    if (!fileContent.contains(languageCodeRegex)) return null;

    final code = _getContentBetweenTag(
      tag: tag,
      fullContent: fileContent,
    )!
        .replaceAll(RegExp('```[a-zA-Z]*\n'), '')
        .replaceAll('\n```', '');

    final language = getLanguageFromCode(fileContent)!;

    return CodeModel(language: language, code: code);
  }

  /// Returns all the items retrieved in the list of items:
  /// e.g:
  /// - 1
  /// - 2
  ///
  /// becomes [1, 2]
  List<String> _getAllItemsInList(String content) {
    final regex = RegExp(r'(?<=- ).*(^[\n- ]|$)', multiLine: true);
    final allMatches = regex.allMatches(content);
    final groups = allMatches.map((e) => e.group(0)).toList();

    // Filter out all the null strings
    return groups.whereType<String>().toList();
  }

  /// Returns all the answers retrieved from the content.
  List<dynamic>? _getAnswersFromContent({
    required String content,
  }) {
    final answersContent = _getContentBetweenTag(
      tag: kAnswersTag,
      fullContent: content,
    );
    if (answersContent == null) return null;

    final isCodeBlock = answersContent.trimLeft().startsWith('```');
    if (isCodeBlock) {
      final answers = _getListOfContentBetweenBackticks(
        content: answersContent,
        skipHeadings: true,
      );
      final languageCode = getLanguageFromCode(answersContent)!;
      return answers
          .map((a) => CodeModel(language: languageCode, code: a))
          .toList(growable: false);
    }
    return _getAllItemsInList(answersContent);
  }

  /// Returns all the solutions retrieved from the content.
  ///
  /// The solutions can be in two different ways:
  /// 1. as code inside the backticks (```)
  /// e.g:
  ///
  /// ```
  /// printf("Hello, World!");
  /// ```
  ///
  /// 2. as list like:
  /// - first solution
  /// - second solution
  List<String>? _getSolutionsFromContent(String fileContent) {
    final solutionsContent = _getContentBetweenTag(
      tag: kSolutionsTag,
      fullContent: fileContent,
    );
    if (solutionsContent == null) return null;
    late final List<String> solutions;
    if (solutionsContent.contains('```')) {
      solutions = _getListOfContentBetweenBackticks(
        content: solutionsContent,
        skipHeadings: true,
      );
    } else {
      solutions = _getAllItemsInList(solutionsContent);
    }
    return solutions;
  }
}

extension on String {
  /// Creates a new string with the last occurrence of [from] replaced by [to].
  String replaceLast(Pattern from, String to) {
    final match = from.allMatches(this).last;
    return replaceRange(match.start, match.end, to);
  }

  /// Trims out all the new lines (`\n` specifically) in both the leading and the trailing sides.
  String trimNewLines() {
    var initialString = this;
    while (initialString.startsWith('\n')) {
      initialString = initialString.replaceFirst('\n', '');
    }
    while (initialString.endsWith('\n')) {
      initialString = initialString.replaceLast('\n', '');
    }
    return initialString;
  }
}
