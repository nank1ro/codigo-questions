// coverage:ignore-file
// GENERATED CODE - DO NOT MODIFY BY HAND
// ignore_for_file: type=lint
// ignore_for_file: unused_element, deprecated_member_use, deprecated_member_use_from_same_package, use_function_type_syntax_for_parameters, unnecessary_const, avoid_init_to_null, invalid_override_different_default_values_named, prefer_expression_function_bodies, annotate_overrides, invalid_annotation_target, unnecessary_question_mark

part of 'model.dart';

// **************************************************************************
// FreezedGenerator
// **************************************************************************

T _$identity<T>(T value) => value;

final _privateConstructorUsedError = UnsupportedError(
    'It seems like you constructed your class using `MyClass._()`. This constructor is only meant to be used by freezed and you are not supposed to need it nor use it.\nPlease check the documentation here for more information: https://github.com/rrousselGit/freezed#custom-getters-and-methods');

AssertModel _$AssertModelFromJson(Map<String, dynamic> json) {
  return _AssertModel.fromJson(json);
}

/// @nodoc
mixin _$AssertModel {
  /// The description of the unit test:
  /// e.g: `The function should return "Hello, World!".`
  String get description => throw _privateConstructorUsedError;

  /// The real unit test to be run.
  /// e.g:
  /// ```python
  /// def test_say_hi(self):
  ///     self.assertEqual(hello(), "Hello, World!", "--err-t1--"
  /// ```
  String? get unitTest => throw _privateConstructorUsedError;

  /// An optional regex assert, this assert will be run client side.
  /// e.g:
  /// ```json
  /// {
  ///   "regex": "if|else|switch|\\?|&&|\\|\\||DateTime",
  ///   "modifiers": ["m"],
  ///   "shouldMatch": false
  /// }
  /// ```
  /// The supported modifiers are:
  /// - m: multiLinex.
  /// - i: caseInsensitive.
  /// - u: unicode.
  /// - s: dotAll.
  ///
  /// The shouldMatch flag indicates if the code should match or not.
  /// If `shouldMatch` is true, the regex should match, otherwise it should
  /// not.
  RegexAssert? get regexAssert => throw _privateConstructorUsedError;

  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;
  @JsonKey(ignore: true)
  $AssertModelCopyWith<AssertModel> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $AssertModelCopyWith<$Res> {
  factory $AssertModelCopyWith(
          AssertModel value, $Res Function(AssertModel) then) =
      _$AssertModelCopyWithImpl<$Res, AssertModel>;
  @useResult
  $Res call({String description, String? unitTest, RegexAssert? regexAssert});
}

/// @nodoc
class _$AssertModelCopyWithImpl<$Res, $Val extends AssertModel>
    implements $AssertModelCopyWith<$Res> {
  _$AssertModelCopyWithImpl(this._value, this._then);

  // ignore: unused_field
  final $Val _value;
  // ignore: unused_field
  final $Res Function($Val) _then;

  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? description = null,
    Object? unitTest = freezed,
    Object? regexAssert = freezed,
  }) {
    return _then(_value.copyWith(
      description: null == description
          ? _value.description
          : description // ignore: cast_nullable_to_non_nullable
              as String,
      unitTest: freezed == unitTest
          ? _value.unitTest
          : unitTest // ignore: cast_nullable_to_non_nullable
              as String?,
      regexAssert: freezed == regexAssert
          ? _value.regexAssert
          : regexAssert // ignore: cast_nullable_to_non_nullable
              as RegexAssert?,
    ) as $Val);
  }
}

/// @nodoc
abstract class _$$_AssertModelCopyWith<$Res>
    implements $AssertModelCopyWith<$Res> {
  factory _$$_AssertModelCopyWith(
          _$_AssertModel value, $Res Function(_$_AssertModel) then) =
      __$$_AssertModelCopyWithImpl<$Res>;
  @override
  @useResult
  $Res call({String description, String? unitTest, RegexAssert? regexAssert});
}

/// @nodoc
class __$$_AssertModelCopyWithImpl<$Res>
    extends _$AssertModelCopyWithImpl<$Res, _$_AssertModel>
    implements _$$_AssertModelCopyWith<$Res> {
  __$$_AssertModelCopyWithImpl(
      _$_AssertModel _value, $Res Function(_$_AssertModel) _then)
      : super(_value, _then);

  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? description = null,
    Object? unitTest = freezed,
    Object? regexAssert = freezed,
  }) {
    return _then(_$_AssertModel(
      description: null == description
          ? _value.description
          : description // ignore: cast_nullable_to_non_nullable
              as String,
      unitTest: freezed == unitTest
          ? _value.unitTest
          : unitTest // ignore: cast_nullable_to_non_nullable
              as String?,
      regexAssert: freezed == regexAssert
          ? _value.regexAssert
          : regexAssert // ignore: cast_nullable_to_non_nullable
              as RegexAssert?,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$_AssertModel implements _AssertModel {
  const _$_AssertModel(
      {required this.description, this.unitTest, this.regexAssert});

  factory _$_AssertModel.fromJson(Map<String, dynamic> json) =>
      _$$_AssertModelFromJson(json);

  /// The description of the unit test:
  /// e.g: `The function should return "Hello, World!".`
  @override
  final String description;

  /// The real unit test to be run.
  /// e.g:
  /// ```python
  /// def test_say_hi(self):
  ///     self.assertEqual(hello(), "Hello, World!", "--err-t1--"
  /// ```
  @override
  final String? unitTest;

  /// An optional regex assert, this assert will be run client side.
  /// e.g:
  /// ```json
  /// {
  ///   "regex": "if|else|switch|\\?|&&|\\|\\||DateTime",
  ///   "modifiers": ["m"],
  ///   "shouldMatch": false
  /// }
  /// ```
  /// The supported modifiers are:
  /// - m: multiLinex.
  /// - i: caseInsensitive.
  /// - u: unicode.
  /// - s: dotAll.
  ///
  /// The shouldMatch flag indicates if the code should match or not.
  /// If `shouldMatch` is true, the regex should match, otherwise it should
  /// not.
  @override
  final RegexAssert? regexAssert;

  @override
  String toString() {
    return 'AssertModel(description: $description, unitTest: $unitTest, regexAssert: $regexAssert)';
  }

  @override
  bool operator ==(dynamic other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$_AssertModel &&
            (identical(other.description, description) ||
                other.description == description) &&
            (identical(other.unitTest, unitTest) ||
                other.unitTest == unitTest) &&
            (identical(other.regexAssert, regexAssert) ||
                other.regexAssert == regexAssert));
  }

  @JsonKey(ignore: true)
  @override
  int get hashCode =>
      Object.hash(runtimeType, description, unitTest, regexAssert);

  @JsonKey(ignore: true)
  @override
  @pragma('vm:prefer-inline')
  _$$_AssertModelCopyWith<_$_AssertModel> get copyWith =>
      __$$_AssertModelCopyWithImpl<_$_AssertModel>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$_AssertModelToJson(
      this,
    );
  }
}

abstract class _AssertModel implements AssertModel {
  const factory _AssertModel(
      {required final String description,
      final String? unitTest,
      final RegexAssert? regexAssert}) = _$_AssertModel;

  factory _AssertModel.fromJson(Map<String, dynamic> json) =
      _$_AssertModel.fromJson;

  @override

  /// The description of the unit test:
  /// e.g: `The function should return "Hello, World!".`
  String get description;
  @override

  /// The real unit test to be run.
  /// e.g:
  /// ```python
  /// def test_say_hi(self):
  ///     self.assertEqual(hello(), "Hello, World!", "--err-t1--"
  /// ```
  String? get unitTest;
  @override

  /// An optional regex assert, this assert will be run client side.
  /// e.g:
  /// ```json
  /// {
  ///   "regex": "if|else|switch|\\?|&&|\\|\\||DateTime",
  ///   "modifiers": ["m"],
  ///   "shouldMatch": false
  /// }
  /// ```
  /// The supported modifiers are:
  /// - m: multiLinex.
  /// - i: caseInsensitive.
  /// - u: unicode.
  /// - s: dotAll.
  ///
  /// The shouldMatch flag indicates if the code should match or not.
  /// If `shouldMatch` is true, the regex should match, otherwise it should
  /// not.
  RegexAssert? get regexAssert;
  @override
  @JsonKey(ignore: true)
  _$$_AssertModelCopyWith<_$_AssertModel> get copyWith =>
      throw _privateConstructorUsedError;
}
