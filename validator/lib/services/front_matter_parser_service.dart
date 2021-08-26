import 'package:front_matter/front_matter.dart' as fm;
import 'package:yaml/yaml.dart';

typedef JSON = Map<String, dynamic>;

// Default delimiter for YAML.
const _defaultDelimiter = '---';

/// Provides a way to parse the frontmatter content returning a [JSON].
class FrontMatterParserService {
  const FrontMatterParserService();

  /// View documentation here [fm.parse]
  JSON parse(String text, {String delimiter = _defaultDelimiter}) {
    final document = fm.parse(text, delimiter: delimiter);
    return _yamlMapToJson(document.data!);
  }

  Future<JSON> parseFile(String path,
      {String delimiter = _defaultDelimiter}) async {
    final document = await fm.parseFile(path, delimiter: delimiter);
    return _yamlMapToJson(document.data!);
  }

  /// Provides a JSON with each value got from the FrontMatter
  /// of the .md file
  ///
  /// For example this:
  /// ```yaml
  /// ---
  /// language: python
  /// title: Hello World!
  /// exerciseType: 1
  /// fileName: hello_world
  /// ---
  ///
  /// becomes this:
  /// ```dart
  /// {
  ///   "language": "python",
  ///   "title": "Hello World!"",
  ///   "exerciseType": 1,
  ///   "fileName": "hello_world",
  /// }
  /// ```
  JSON _yamlMapToJson(YamlMap yamlMap) {
    final resultMap = <String, dynamic>{};
    for (final entry in yamlMap.entries) {
      resultMap[entry.key.toString()] = entry.value;
    }
    return resultMap;
  }
}
