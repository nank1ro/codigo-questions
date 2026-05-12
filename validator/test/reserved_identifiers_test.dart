import 'package:test/test.dart';
import 'package:validator/reserved_identifiers.dart';

void main() {
  group('reservedIdentifiersByLanguage', () {
    test('covers all supported languages', () {
      expect(
        reservedIdentifiersByLanguage.keys.toSet(),
        equals({'dart', 'javascript', 'kotlin', 'python', 'swift', 'c'}),
      );
    });

    test('dart includes scaffold-driven matcher names', () {
      final dart = reservedIdentifiersByLanguage['dart']!;
      expect(dart, containsAll(<String>['isEmpty', 'equals', 'test', 'group']));
    });

    test('javascript includes before-seed names', () {
      final js = reservedIdentifiersByLanguage['javascript']!;
      expect(
        js,
        containsAll(<String>[
          '_testFailedCount',
          '_testCount',
          'assert',
          'tryCatch',
        ]),
      );
    });

    test('kotlin includes before-seed names', () {
      final kt = reservedIdentifiersByLanguage['kotlin']!;
      expect(
        kt,
        containsAll(<String>['_testFailedCount', '_testCount', 'tryCatch', 'main']),
      );
    });

    test('python includes before-asserts names', () {
      final py = reservedIdentifiersByLanguage['python']!;
      expect(py, containsAll(<String>['unittest', 'CodigoTests']));
    });

    test('swift includes scaffold names', () {
      final sw = reservedIdentifiersByLanguage['swift']!;
      expect(
        sw,
        containsAll(<String>[
          'Foundation',
          'XCTest',
          'CodigoTests',
          'XCTMain',
          'testCase',
          'allTests',
        ]),
      );
    });

    test('c includes scaffold names', () {
      final c = reservedIdentifiersByLanguage['c']!;
      expect(
        c,
        containsAll(<String>[
          'e',
          '_test_count',
          '_test_failed_count',
          'try_catch',
          'Throw',
          'CExceptionFrames',
          'main',
        ]),
      );
    });
  });

  group('extractTopLevelIdentifiers - dart', () {
    test('extracts a `bool` variable name', () {
      final ids = extractTopLevelIdentifiers('bool isEmpty = false;', 'dart');
      expect(ids, contains('isEmpty'));
    });

    test('collides with reserved `isEmpty`', () {
      final ids = extractTopLevelIdentifiers('bool isEmpty = false;', 'dart');
      final reserved = reservedIdentifiersByLanguage['dart']!;
      expect(ids.intersection(reserved), equals({'isEmpty'}));
    });

    test('a non-reserved variable does not collide', () {
      final ids = extractTopLevelIdentifiers('bool myFlag = false;', 'dart');
      final reserved = reservedIdentifiersByLanguage['dart']!;
      expect(ids, contains('myFlag'));
      expect(ids.intersection(reserved), isEmpty);
    });

    test('ignores identifiers inside line comments', () {
      final ids = extractTopLevelIdentifiers(
        '// bool isEmpty = false;\nbool ok = true;',
        'dart',
      );
      expect(ids, contains('ok'));
      expect(ids, isNot(contains('isEmpty')));
    });

    test('does not extract identifiers nested inside braces', () {
      final ids = extractTopLevelIdentifiers(
        'void main() {\n  bool isEmpty = false;\n}',
        'dart',
      );
      expect(ids, isNot(contains('isEmpty')));
    });

    test('class name collides with matcher function `equals`', () {
      final ids = extractTopLevelIdentifiers('class equals {}', 'dart');
      final reserved = reservedIdentifiersByLanguage['dart']!;
      expect(ids.intersection(reserved), equals({'equals'}));
    });

    test('ignores identifiers inside block comments', () {
      final ids = extractTopLevelIdentifiers(
        '/* bool isEmpty = false; */\nbool ok = true;',
        'dart',
      );
      expect(ids, contains('ok'));
      expect(ids, isNot(contains('isEmpty')));
    });
  });

  group('extractTopLevelIdentifiers - javascript', () {
    test('`let assert = 1` collides with `assert`', () {
      final ids = extractTopLevelIdentifiers('let assert = 1;', 'javascript');
      final reserved = reservedIdentifiersByLanguage['javascript']!;
      expect(ids.intersection(reserved), equals({'assert'}));
    });

    test('`function tryCatch` collides with `tryCatch`', () {
      final ids = extractTopLevelIdentifiers(
        'function tryCatch() {}',
        'javascript',
      );
      final reserved = reservedIdentifiersByLanguage['javascript']!;
      expect(ids.intersection(reserved), equals({'tryCatch'}));
    });

    test('non-reserved function name does not collide', () {
      final ids = extractTopLevelIdentifiers(
        'function add(a, b) { return a + b; }',
        'javascript',
      );
      final reserved = reservedIdentifiersByLanguage['javascript']!;
      expect(ids, contains('add'));
      expect(ids.intersection(reserved), isEmpty);
    });
  });

  group('extractTopLevelIdentifiers - kotlin', () {
    test('`var tryCatch = 1` collides with `tryCatch`', () {
      final ids = extractTopLevelIdentifiers('var tryCatch = 1', 'kotlin');
      final reserved = reservedIdentifiersByLanguage['kotlin']!;
      expect(ids.intersection(reserved), equals({'tryCatch'}));
    });

    test('non-reserved function name does not collide', () {
      final ids = extractTopLevelIdentifiers('fun addition() {}', 'kotlin');
      final reserved = reservedIdentifiersByLanguage['kotlin']!;
      expect(ids, contains('addition'));
      expect(ids.intersection(reserved), isEmpty);
    });

    test('`var _testCount` collides with `_testCount`', () {
      final ids = extractTopLevelIdentifiers('var _testCount = 5', 'kotlin');
      final reserved = reservedIdentifiersByLanguage['kotlin']!;
      expect(ids.intersection(reserved), equals({'_testCount'}));
    });
  });

  group('extractTopLevelIdentifiers - python', () {
    test('`unittest = 5` collides with `unittest`', () {
      final ids = extractTopLevelIdentifiers('unittest = 5', 'python');
      final reserved = reservedIdentifiersByLanguage['python']!;
      expect(ids.intersection(reserved), equals({'unittest'}));
    });

    test('`class CodigoTests` collides with `CodigoTests`', () {
      final ids = extractTopLevelIdentifiers(
        'class CodigoTests:\n    pass',
        'python',
      );
      final reserved = reservedIdentifiersByLanguage['python']!;
      expect(ids.intersection(reserved), equals({'CodigoTests'}));
    });

    test('non-reserved function does not collide', () {
      final ids = extractTopLevelIdentifiers(
        'def addition():\n    pass',
        'python',
      );
      final reserved = reservedIdentifiersByLanguage['python']!;
      expect(ids, contains('addition'));
      expect(ids.intersection(reserved), isEmpty);
    });

    test('indented assignment is not considered top-level', () {
      final ids = extractTopLevelIdentifiers(
        'def addition():\n    unittest = 5',
        'python',
      );
      expect(ids, isNot(contains('unittest')));
    });
  });

  group('extractTopLevelIdentifiers - swift', () {
    test('`class CodigoTests` collides with `CodigoTests`', () {
      final ids = extractTopLevelIdentifiers('class CodigoTests {}', 'swift');
      final reserved = reservedIdentifiersByLanguage['swift']!;
      expect(ids.intersection(reserved), equals({'CodigoTests'}));
    });

    test('`func XCTMain` collides with `XCTMain`', () {
      final ids = extractTopLevelIdentifiers('func XCTMain() {}', 'swift');
      final reserved = reservedIdentifiersByLanguage['swift']!;
      expect(ids.intersection(reserved), equals({'XCTMain'}));
    });

    test('non-reserved function does not collide', () {
      final ids = extractTopLevelIdentifiers('func addition() {}', 'swift');
      final reserved = reservedIdentifiersByLanguage['swift']!;
      expect(ids, contains('addition'));
      expect(ids.intersection(reserved), isEmpty);
    });
  });

  group('extractTopLevelIdentifiers - c', () {
    test('`int try_catch()` collides with `try_catch`', () {
      final ids = extractTopLevelIdentifiers(
        'int try_catch() { return 0; }',
        'c',
      );
      final reserved = reservedIdentifiersByLanguage['c']!;
      expect(ids.intersection(reserved), equals({'try_catch'}));
    });

    test('`int e = 5` collides with `e`', () {
      final ids = extractTopLevelIdentifiers('int e = 5;', 'c');
      final reserved = reservedIdentifiersByLanguage['c']!;
      expect(ids.intersection(reserved), equals({'e'}));
    });

    test('non-reserved function does not collide', () {
      final ids = extractTopLevelIdentifiers(
        'int addition(int a, int b) { return a + b; }',
        'c',
      );
      final reserved = reservedIdentifiersByLanguage['c']!;
      expect(ids, contains('addition'));
      expect(ids.intersection(reserved), isEmpty);
    });
  });

  group('unsupported language returns no collisions', () {
    test('returns empty set for unknown language', () {
      final ids = extractTopLevelIdentifiers('let assert = 1;', 'rust');
      expect(ids, isEmpty);
    });
  });
}
