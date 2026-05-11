/// Reserved identifiers per language that collide with test scaffolds.
/// Derived from actual imports and declarations in translations/en/templates/{lang}_1.md
final Map<String, Set<String>> reservedIdentifiersByLanguage = {
  'dart': _dartReserved,
  'javascript': _javascriptReserved,
  'kotlin': _kotlinReserved,
  'python': _pythonReserved,
  'swift': _swiftReserved,
  'c': _cReserved,
};

// Dart: package:test/test.dart re-exports package:matcher
final _dartReserved = <String>{
  // Matcher constants
  'isEmpty',
  'isNotEmpty',
  'isNull',
  'isNotNull',
  'isTrue',
  'isFalse',
  'isNaN',
  'isNotNaN',
  'anything',
  'returnsNormally',
  'isZero',
  'isNonZero',
  'isPositive',
  'isNonPositive',
  'isNegative',
  'isNonNegative',
  'isMap',
  'isList',
  'isArgumentError',
  'isCastError',
  'isConcurrentModificationError',
  'isCyclicInitializationError',
  'isException',
  'isFormatException',
  'isNoSuchMethodError',
  'isNullThrownError',
  'isRangeError',
  'isStateError',
  'isUnimplementedError',
  'isUnsupportedError',
  // Matcher functions
  'same',
  'equals',
  'contains',
  'hasLength',
  'isIn',
  'predicate',
  'everyElement',
  'anyElement',
  'orderedEquals',
  'unorderedEquals',
  'unorderedMatches',
  'pairwiseCompare',
  'containsAll',
  'containsAllInOrder',
  'containsOnce',
  'isSorted',
  'isSortedUsing',
  'isSortedBy',
  'containsValue',
  'containsPair',
  'closeTo',
  'inInclusiveRange',
  'inExclusiveRange',
  'inOpenClosedRange',
  'inClosedOpenRange',
  'isNot',
  'allOf',
  'anyOf',
  'greaterThan',
  'greaterThanOrEqualTo',
  'lessThan',
  'lessThanOrEqualTo',
  'equalsIgnoringCase',
  'equalsIgnoringWhitespace',
  'startsWith',
  'endsWith',
  'stringContainsInOrder',
  'matches',
  'wrapMatcher',
  'throwsA',
  'throws',
  'completion',
  // package:test scaffolding
  'test',
  'group',
  'setUp',
  'tearDown',
  'setUpAll',
  'tearDownAll',
  'expect',
  'expectLater',
  'fail',
  'addTearDown',
  'markTestSkipped',
};

// JavaScript: from before-seed
final _javascriptReserved = <String>{
  '_testFailedCount',
  '_testCount',
  'assert',
  'tryCatch',
};

// Kotlin: from before-seed
final _kotlinReserved = <String>{
  '_testFailedCount',
  '_testCount',
  'tryCatch',
  'main',
};

// Python: from before-asserts
final _pythonReserved = <String>{
  'unittest',
  'CodigoTests',
};

// Swift: from before-asserts and after-asserts
final _swiftReserved = <String>{
  'Foundation',
  'XCTest',
  'CodigoTests',
  'XCTMain',
  'testCase',
  'allTests',
};

// C: from before-seed
final _cReserved = <String>{
  'e',
  '_test_count',
  '_test_failed_count',
  'try_catch',
  'Throw',
  'CExceptionFrames',
  'main',
};

/// Extracts top-level identifiers declared in code by language.
/// Returns a set of identifiers that would be declared at module/global scope.
Set<String> extractTopLevelIdentifiers(String code, String language) {
  final identifiers = <String>{};

  // Remove comments based on language
  String cleanCode = _stripComments(code, language);

  // Split into lines and process based on language
  final lines = cleanCode.split('\n');

  switch (language) {
    case 'dart':
      identifiers.addAll(_extractDartIdentifiers(lines));
      break;
    case 'javascript':
      identifiers.addAll(_extractJavaScriptIdentifiers(lines));
      break;
    case 'kotlin':
      identifiers.addAll(_extractKotlinIdentifiers(lines));
      break;
    case 'python':
      identifiers.addAll(_extractPythonIdentifiers(lines));
      break;
    case 'swift':
      identifiers.addAll(_extractSwiftIdentifiers(lines));
      break;
    case 'c':
      identifiers.addAll(_extractCIdentifiers(lines));
      break;
  }

  return identifiers;
}

/// Strips single-line and block comments from code.
String _stripComments(String code, String language) {
  if (language == 'python') {
    // Python uses # for comments
    return code.replaceAll(RegExp(r'#[^\n]*'), '');
  } else {
    // Dart, JavaScript, Kotlin, Swift, C use // and /* */
    // Remove block comments first
    String result = code.replaceAll(RegExp(r'/\*.*?\*/', dotAll: true), '');
    // Then remove line comments
    result = result.replaceAll(RegExp(r'//[^\n]*'), '');
    return result;
  }
}

Set<String> _extractDartIdentifiers(List<String> lines) {
  final identifiers = <String>{};
  int braceDepth = 0;

  for (final line in lines) {
    final trimmed = line.trimLeft();

    // Track brace depth
    braceDepth += trimmed.split('{').length - 1;
    braceDepth -= trimmed.split('}').length - 1;

    // Only process top-level (depth 0)
    if (braceDepth > 0) continue;
    if (!line.startsWith(RegExp(r'^\s*\S'))) continue;

    // Variable declarations: bool/int/double/String/num/dynamic/var/final/const/late
    var match = RegExp(
      r'^(?:bool|int|double|String|num|dynamic|var|final|const|late)\s+(?:[A-Za-z_][\w<>?,. ]*\s+)?([A-Za-z_]\w*)\s*[=;]',
    ).firstMatch(trimmed);
    if (match != null) {
      identifiers.add(match.group(1)!);
      continue;
    }

    // Class/enum/mixin/extension/typedef declarations
    match = RegExp(r'^(?:class|enum|mixin|extension|typedef)\s+([A-Za-z_]\w*)')
        .firstMatch(trimmed);
    if (match != null) {
      identifiers.add(match.group(1)!);
      continue;
    }

    // Function and typed variable declarations
    match = RegExp(r'^(?:[A-Za-z_][\w<>?,. ]*)\s+([A-Za-z_]\w*)\s*[=(]')
        .firstMatch(trimmed);
    if (match != null) {
      identifiers.add(match.group(1)!);
      continue;
    }
  }

  return identifiers;
}

Set<String> _extractJavaScriptIdentifiers(List<String> lines) {
  final identifiers = <String>{};
  int braceDepth = 0;

  for (final line in lines) {
    final trimmed = line.trimLeft();

    braceDepth += trimmed.split('{').length - 1;
    braceDepth -= trimmed.split('}').length - 1;

    if (braceDepth > 0) continue;
    if (!line.startsWith(RegExp(r'^\s*\S'))) continue;

    // var/let/const/function/class declarations
    final match = RegExp(r'^(?:var|let|const|function|class)\s+([A-Za-z_$][\w$]*)')
        .firstMatch(trimmed);
    if (match != null) {
      identifiers.add(match.group(1)!);
    }
  }

  return identifiers;
}

Set<String> _extractKotlinIdentifiers(List<String> lines) {
  final identifiers = <String>{};
  int braceDepth = 0;

  for (final line in lines) {
    final trimmed = line.trimLeft();

    braceDepth += trimmed.split('{').length - 1;
    braceDepth -= trimmed.split('}').length - 1;

    if (braceDepth > 0) continue;
    if (!line.startsWith(RegExp(r'^\s*\S'))) continue;

    // val/var/fun/class/object/interface/typealias declarations
    final match = RegExp(r'^(?:val|var|fun|class|object|interface|typealias)\s+([A-Za-z_]\w*)')
        .firstMatch(trimmed);
    if (match != null) {
      identifiers.add(match.group(1)!);
    }
  }

  return identifiers;
}

Set<String> _extractPythonIdentifiers(List<String> lines) {
  final identifiers = <String>{};

  for (final line in lines) {
    // Python: only lines at column 0 are top-level
    if (line.isEmpty || !line.startsWith(RegExp(r'^\S'))) continue;

    // def/class declarations
    var match = RegExp(r'^(?:def|class)\s+([A-Za-z_]\w*)')
        .firstMatch(line);
    if (match != null) {
      identifiers.add(match.group(1)!);
      continue;
    }

    // Top-level assignments
    match = RegExp(r'^([A-Za-z_]\w*)\s*=').firstMatch(line);
    if (match != null) {
      identifiers.add(match.group(1)!);
    }
  }

  return identifiers;
}

Set<String> _extractSwiftIdentifiers(List<String> lines) {
  final identifiers = <String>{};
  int braceDepth = 0;

  for (final line in lines) {
    final trimmed = line.trimLeft();

    braceDepth += trimmed.split('{').length - 1;
    braceDepth -= trimmed.split('}').length - 1;

    if (braceDepth > 0) continue;
    if (!line.startsWith(RegExp(r'^\s*\S'))) continue;

    // let/var/func/class/struct/enum/protocol/typealias declarations
    final match = RegExp(r'^(?:let|var|func|class|struct|enum|protocol|typealias)\s+([A-Za-z_]\w*)')
        .firstMatch(trimmed);
    if (match != null) {
      identifiers.add(match.group(1)!);
    }
  }

  return identifiers;
}

Set<String> _extractCIdentifiers(List<String> lines) {
  final identifiers = <String>{};
  int braceDepth = 0;

  for (final line in lines) {
    final trimmed = line.trimLeft();

    braceDepth += trimmed.split('{').length - 1;
    braceDepth -= trimmed.split('}').length - 1;

    if (braceDepth > 0) continue;
    if (!line.startsWith(RegExp(r'^\s*\S'))) continue;

    // Function and variable declarations: type name = or type name (
    // Pattern: one or more type tokens (with possible *) followed by identifier
    final match = RegExp(r'^(?:[A-Za-z_]\w*[\s*]+)+([A-Za-z_]\w*)\s*[(=;]')
        .firstMatch(trimmed);
    if (match != null) {
      identifiers.add(match.group(1)!);
    }
  }

  return identifiers;
}
