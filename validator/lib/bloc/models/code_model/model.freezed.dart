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

CodeModel _$CodeModelFromJson(Map<String, dynamic> json) {
  return _CodeModel.fromJson(json);
}

/// @nodoc
class _$CodeModelTearOff {
  const _$CodeModelTearOff();

  _CodeModel call({required String language, required String code}) {
    return _CodeModel(
      language: language,
      code: code,
    );
  }

  CodeModel fromJson(Map<String, Object> json) {
    return CodeModel.fromJson(json);
  }
}

/// @nodoc
const $CodeModel = _$CodeModelTearOff();

/// @nodoc
mixin _$CodeModel {
  String get language => throw _privateConstructorUsedError;
  String get code => throw _privateConstructorUsedError;

  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;
  @JsonKey(ignore: true)
  $CodeModelCopyWith<CodeModel> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $CodeModelCopyWith<$Res> {
  factory $CodeModelCopyWith(CodeModel value, $Res Function(CodeModel) then) =
      _$CodeModelCopyWithImpl<$Res>;
  $Res call({String language, String code});
}

/// @nodoc
class _$CodeModelCopyWithImpl<$Res> implements $CodeModelCopyWith<$Res> {
  _$CodeModelCopyWithImpl(this._value, this._then);

  final CodeModel _value;
  // ignore: unused_field
  final $Res Function(CodeModel) _then;

  @override
  $Res call({
    Object? language = freezed,
    Object? code = freezed,
  }) {
    return _then(_value.copyWith(
      language: language == freezed
          ? _value.language
          : language // ignore: cast_nullable_to_non_nullable
              as String,
      code: code == freezed
          ? _value.code
          : code // ignore: cast_nullable_to_non_nullable
              as String,
    ));
  }
}

/// @nodoc
abstract class _$CodeModelCopyWith<$Res> implements $CodeModelCopyWith<$Res> {
  factory _$CodeModelCopyWith(
          _CodeModel value, $Res Function(_CodeModel) then) =
      __$CodeModelCopyWithImpl<$Res>;
  @override
  $Res call({String language, String code});
}

/// @nodoc
class __$CodeModelCopyWithImpl<$Res> extends _$CodeModelCopyWithImpl<$Res>
    implements _$CodeModelCopyWith<$Res> {
  __$CodeModelCopyWithImpl(_CodeModel _value, $Res Function(_CodeModel) _then)
      : super(_value, (v) => _then(v as _CodeModel));

  @override
  _CodeModel get _value => super._value as _CodeModel;

  @override
  $Res call({
    Object? language = freezed,
    Object? code = freezed,
  }) {
    return _then(_CodeModel(
      language: language == freezed
          ? _value.language
          : language // ignore: cast_nullable_to_non_nullable
              as String,
      code: code == freezed
          ? _value.code
          : code // ignore: cast_nullable_to_non_nullable
              as String,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$_CodeModel implements _CodeModel {
  const _$_CodeModel({required this.language, required this.code});

  factory _$_CodeModel.fromJson(Map<String, dynamic> json) =>
      _$$_CodeModelFromJson(json);

  @override
  final String language;
  @override
  final String code;

  @override
  String toString() {
    return 'CodeModel(language: $language, code: $code)';
  }

  @override
  bool operator ==(dynamic other) {
    return identical(this, other) ||
        (other is _CodeModel &&
            (identical(other.language, language) ||
                const DeepCollectionEquality()
                    .equals(other.language, language)) &&
            (identical(other.code, code) ||
                const DeepCollectionEquality().equals(other.code, code)));
  }

  @override
  int get hashCode =>
      runtimeType.hashCode ^
      const DeepCollectionEquality().hash(language) ^
      const DeepCollectionEquality().hash(code);

  @JsonKey(ignore: true)
  @override
  _$CodeModelCopyWith<_CodeModel> get copyWith =>
      __$CodeModelCopyWithImpl<_CodeModel>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$_CodeModelToJson(this);
  }
}

abstract class _CodeModel implements CodeModel {
  const factory _CodeModel({required String language, required String code}) =
      _$_CodeModel;

  factory _CodeModel.fromJson(Map<String, dynamic> json) =
      _$_CodeModel.fromJson;

  @override
  String get language => throw _privateConstructorUsedError;
  @override
  String get code => throw _privateConstructorUsedError;
  @override
  @JsonKey(ignore: true)
  _$CodeModelCopyWith<_CodeModel> get copyWith =>
      throw _privateConstructorUsedError;
}
