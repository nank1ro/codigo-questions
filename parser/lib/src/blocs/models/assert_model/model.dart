import 'package:freezed_annotation/freezed_annotation.dart';

part 'model.freezed.dart';
part 'model.g.dart';

// ignore_for_file: public_member_api_docs
@Freezed()
class AssertModel with _$AssertModel {
  const factory AssertModel({
    /// The description of the unit test:
    /// e.g: `The function should return "Hello, World!".`
    required String description,

    /// The real unit test to be run.
    /// e.g:
    /// ```python
    /// def test_say_hi(self):
    ///     self.assertEqual(hello(), "Hello, World!", "--err-t1--"
    /// ```
    String? unitTest,

    /// An optional regex assert, this assert will be run client side.
    /// e.g:
    /// ```json
    /// {
    ///   "regex": "if|else|switch|\\?|&&|\\|\\||DateTime",
    ///   "modifiers": ["m"],
    ///   "shouldMatch": false
    /// }
    /// ```
    RegexAssert? regexAssert,
  }) = _AssertModel;

  factory AssertModel.fromJson(Map<String, dynamic> json) =>
      _$AssertModelFromJson(json);
}

/// A client-side validation of the user source code using a regex.
///
/// The supported modifiers are:
/// - m: multiLinex.
/// - i: caseInsensitive.
/// - u: unicode.
/// - s: dotAll.
///
/// The [shouldMatch] flag indicates if the code should match or not.
/// If [shouldMatch] is true, the regex should match, otherwise it should
/// not.
@immutable
class RegexAssert {
  const RegexAssert({
    required this.regExp,
    required this.shouldMatch,
  });

  factory RegexAssert.fromJson(Map<String, dynamic> json) {
    final re = json['regex'] as String;
    final modifiers = List<String>.from(json['modifiers'] as List);
    final shouldMatch = json['shouldMatch'] as bool;
    return RegexAssert(
      regExp: RegExp(
        re,
        multiLine: modifiers.contains('m'),
        caseSensitive: !modifiers.contains('i'),
        unicode: modifiers.contains('u'),
        dotAll: modifiers.contains('s'),
      ),
      shouldMatch: shouldMatch,
    );
  }

  Map<String, dynamic> toJson() => {
        'regex': regExp.pattern,
        'modifiers': [
          if (regExp.isMultiLine) 'm',
          if (regExp.isCaseSensitive) 'i',
          if (regExp.isUnicode) 'u',
          if (regExp.isDotAll) 's',
        ],
        'shouldMatch': shouldMatch,
      };

  final RegExp regExp;
  final bool shouldMatch;

  bool eval(String code) {
    return regExp.hasMatch(code) == shouldMatch;
  }

  @override
  bool operator ==(Object other) {
    if (identical(this, other)) return true;

    return other is RegexAssert &&
        other.regExp == regExp &&
        other.shouldMatch == shouldMatch;
  }

  @override
  int get hashCode => regExp.hashCode ^ shouldMatch.hashCode;

  @override
  String toString() =>
      'RegexAssert(regExp: $regExp, shouldMatch: $shouldMatch)';
}
