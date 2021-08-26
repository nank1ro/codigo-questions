// coverage:ignore-file
// GENERATED CODE - DO NOT MODIFY BY HAND
// ignore_for_file: unused_element, deprecated_member_use, deprecated_member_use_from_same_package, use_function_type_syntax_for_parameters, unnecessary_const, avoid_init_to_null, invalid_override_different_default_values_named, prefer_expression_function_bodies, annotate_overrides, invalid_annotation_target

part of 'model.dart';

// **************************************************************************
// FreezedGenerator
// **************************************************************************

T _$identity<T>(T value) => value;

final _privateConstructorUsedError = UnsupportedError(
    'It seems like you constructed your class using `MyClass._()`. This constructor is only meant to be used by freezed and you are not supposed to need it nor use it.\nPlease check the documentation here for more informations: https://github.com/rrousselGit/freezed#custom-getters-and-methods');

AssertModel _$AssertModelFromJson(Map<String, dynamic> json) {
  return _AssertModel.fromJson(json);
}

/// @nodoc
class _$AssertModelTearOff {
  const _$AssertModelTearOff();

  _AssertModel call({required String description, required String unitTest}) {
    return _AssertModel(
      description: description,
      unitTest: unitTest,
    );
  }

  AssertModel fromJson(Map<String, Object> json) {
    return AssertModel.fromJson(json);
  }
}

/// @nodoc
const $AssertModel = _$AssertModelTearOff();

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
  String get unitTest => throw _privateConstructorUsedError;

  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;
  @JsonKey(ignore: true)
  $AssertModelCopyWith<AssertModel> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $AssertModelCopyWith<$Res> {
  factory $AssertModelCopyWith(
          AssertModel value, $Res Function(AssertModel) then) =
      _$AssertModelCopyWithImpl<$Res>;
  $Res call({String description, String unitTest});
}

/// @nodoc
class _$AssertModelCopyWithImpl<$Res> implements $AssertModelCopyWith<$Res> {
  _$AssertModelCopyWithImpl(this._value, this._then);

  final AssertModel _value;
  // ignore: unused_field
  final $Res Function(AssertModel) _then;

  @override
  $Res call({
    Object? description = freezed,
    Object? unitTest = freezed,
  }) {
    return _then(_value.copyWith(
      description: description == freezed
          ? _value.description
          : description // ignore: cast_nullable_to_non_nullable
              as String,
      unitTest: unitTest == freezed
          ? _value.unitTest
          : unitTest // ignore: cast_nullable_to_non_nullable
              as String,
    ));
  }
}

/// @nodoc
abstract class _$AssertModelCopyWith<$Res>
    implements $AssertModelCopyWith<$Res> {
  factory _$AssertModelCopyWith(
          _AssertModel value, $Res Function(_AssertModel) then) =
      __$AssertModelCopyWithImpl<$Res>;
  @override
  $Res call({String description, String unitTest});
}

/// @nodoc
class __$AssertModelCopyWithImpl<$Res> extends _$AssertModelCopyWithImpl<$Res>
    implements _$AssertModelCopyWith<$Res> {
  __$AssertModelCopyWithImpl(
      _AssertModel _value, $Res Function(_AssertModel) _then)
      : super(_value, (v) => _then(v as _AssertModel));

  @override
  _AssertModel get _value => super._value as _AssertModel;

  @override
  $Res call({
    Object? description = freezed,
    Object? unitTest = freezed,
  }) {
    return _then(_AssertModel(
      description: description == freezed
          ? _value.description
          : description // ignore: cast_nullable_to_non_nullable
              as String,
      unitTest: unitTest == freezed
          ? _value.unitTest
          : unitTest // ignore: cast_nullable_to_non_nullable
              as String,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$_AssertModel implements _AssertModel {
  const _$_AssertModel({required this.description, required this.unitTest});

  factory _$_AssertModel.fromJson(Map<String, dynamic> json) =>
      _$$_AssertModelFromJson(json);

  @override

  /// The description of the unit test:
  /// e.g: `The function should return "Hello, World!".`
  final String description;
  @override

  /// The real unit test to be run.
  /// e.g:
  /// ```python
  /// def test_say_hi(self):
  ///     self.assertEqual(hello(), "Hello, World!", "--err-t1--"
  /// ```
  final String unitTest;

  @override
  String toString() {
    return 'AssertModel(description: $description, unitTest: $unitTest)';
  }

  @override
  bool operator ==(dynamic other) {
    return identical(this, other) ||
        (other is _AssertModel &&
            (identical(other.description, description) ||
                const DeepCollectionEquality()
                    .equals(other.description, description)) &&
            (identical(other.unitTest, unitTest) ||
                const DeepCollectionEquality()
                    .equals(other.unitTest, unitTest)));
  }

  @override
  int get hashCode =>
      runtimeType.hashCode ^
      const DeepCollectionEquality().hash(description) ^
      const DeepCollectionEquality().hash(unitTest);

  @JsonKey(ignore: true)
  @override
  _$AssertModelCopyWith<_AssertModel> get copyWith =>
      __$AssertModelCopyWithImpl<_AssertModel>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$_AssertModelToJson(this);
  }
}

abstract class _AssertModel implements AssertModel {
  const factory _AssertModel(
      {required String description, required String unitTest}) = _$_AssertModel;

  factory _AssertModel.fromJson(Map<String, dynamic> json) =
      _$_AssertModel.fromJson;

  @override

  /// The description of the unit test:
  /// e.g: `The function should return "Hello, World!".`
  String get description => throw _privateConstructorUsedError;
  @override

  /// The real unit test to be run.
  /// e.g:
  /// ```python
  /// def test_say_hi(self):
  ///     self.assertEqual(hello(), "Hello, World!", "--err-t1--"
  /// ```
  String get unitTest => throw _privateConstructorUsedError;
  @override
  @JsonKey(ignore: true)
  _$AssertModelCopyWith<_AssertModel> get copyWith =>
      throw _privateConstructorUsedError;
}
