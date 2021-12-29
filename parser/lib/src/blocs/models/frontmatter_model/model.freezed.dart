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

FrontMatterModel _$FrontMatterModelFromJson(Map<String, dynamic> json) {
  return _FrontMatterModel.fromJson(json);
}

/// @nodoc
class _$FrontMatterModelTearOff {
  const _$FrontMatterModelTearOff();

  _FrontMatterModel call(
      {required String language,
      required int exerciseType,
      String? title,
      int? difficulty,
      String? compilerOptions}) {
    return _FrontMatterModel(
      language: language,
      exerciseType: exerciseType,
      title: title,
      difficulty: difficulty,
      compilerOptions: compilerOptions,
    );
  }

  FrontMatterModel fromJson(Map<String, Object> json) {
    return FrontMatterModel.fromJson(json);
  }
}

/// @nodoc
const $FrontMatterModel = _$FrontMatterModelTearOff();

/// @nodoc
mixin _$FrontMatterModel {
  /// The language of the exercise, e.g.: `python`
  String get language => throw _privateConstructorUsedError;

  /// The type of exercise, e.g.: `1`
  ///
  /// The available exercise types are:
  /// 1 => run code
  /// 2 => fill empty spaces
  /// 3 => choose an answer
  /// 4 => sort items
  int get exerciseType => throw _privateConstructorUsedError;

  /// An optional title, mandatory for the challenges, e.g.: `Hello, World!`
  ///
  /// This will be the name of the challenge.
  String? get title => throw _privateConstructorUsedError;

  /// An optional difficulty value
  ///
  /// Accepted values are:
  /// 1 => easy
  /// 2 => medium
  /// 3 => hard
  int? get difficulty => throw _privateConstructorUsedError;

  /// An optional string that defines with all the compiler options,
  /// e.g.: `-lm` in C tells to link with the standard C libraries
  String? get compilerOptions => throw _privateConstructorUsedError;

  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;
  @JsonKey(ignore: true)
  $FrontMatterModelCopyWith<FrontMatterModel> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $FrontMatterModelCopyWith<$Res> {
  factory $FrontMatterModelCopyWith(
          FrontMatterModel value, $Res Function(FrontMatterModel) then) =
      _$FrontMatterModelCopyWithImpl<$Res>;
  $Res call(
      {String language,
      int exerciseType,
      String? title,
      int? difficulty,
      String? compilerOptions});
}

/// @nodoc
class _$FrontMatterModelCopyWithImpl<$Res>
    implements $FrontMatterModelCopyWith<$Res> {
  _$FrontMatterModelCopyWithImpl(this._value, this._then);

  final FrontMatterModel _value;
  // ignore: unused_field
  final $Res Function(FrontMatterModel) _then;

  @override
  $Res call({
    Object? language = freezed,
    Object? exerciseType = freezed,
    Object? title = freezed,
    Object? difficulty = freezed,
    Object? compilerOptions = freezed,
  }) {
    return _then(_value.copyWith(
      language: language == freezed
          ? _value.language
          : language // ignore: cast_nullable_to_non_nullable
              as String,
      exerciseType: exerciseType == freezed
          ? _value.exerciseType
          : exerciseType // ignore: cast_nullable_to_non_nullable
              as int,
      title: title == freezed
          ? _value.title
          : title // ignore: cast_nullable_to_non_nullable
              as String?,
      difficulty: difficulty == freezed
          ? _value.difficulty
          : difficulty // ignore: cast_nullable_to_non_nullable
              as int?,
      compilerOptions: compilerOptions == freezed
          ? _value.compilerOptions
          : compilerOptions // ignore: cast_nullable_to_non_nullable
              as String?,
    ));
  }
}

/// @nodoc
abstract class _$FrontMatterModelCopyWith<$Res>
    implements $FrontMatterModelCopyWith<$Res> {
  factory _$FrontMatterModelCopyWith(
          _FrontMatterModel value, $Res Function(_FrontMatterModel) then) =
      __$FrontMatterModelCopyWithImpl<$Res>;
  @override
  $Res call(
      {String language,
      int exerciseType,
      String? title,
      int? difficulty,
      String? compilerOptions});
}

/// @nodoc
class __$FrontMatterModelCopyWithImpl<$Res>
    extends _$FrontMatterModelCopyWithImpl<$Res>
    implements _$FrontMatterModelCopyWith<$Res> {
  __$FrontMatterModelCopyWithImpl(
      _FrontMatterModel _value, $Res Function(_FrontMatterModel) _then)
      : super(_value, (v) => _then(v as _FrontMatterModel));

  @override
  _FrontMatterModel get _value => super._value as _FrontMatterModel;

  @override
  $Res call({
    Object? language = freezed,
    Object? exerciseType = freezed,
    Object? title = freezed,
    Object? difficulty = freezed,
    Object? compilerOptions = freezed,
  }) {
    return _then(_FrontMatterModel(
      language: language == freezed
          ? _value.language
          : language // ignore: cast_nullable_to_non_nullable
              as String,
      exerciseType: exerciseType == freezed
          ? _value.exerciseType
          : exerciseType // ignore: cast_nullable_to_non_nullable
              as int,
      title: title == freezed
          ? _value.title
          : title // ignore: cast_nullable_to_non_nullable
              as String?,
      difficulty: difficulty == freezed
          ? _value.difficulty
          : difficulty // ignore: cast_nullable_to_non_nullable
              as int?,
      compilerOptions: compilerOptions == freezed
          ? _value.compilerOptions
          : compilerOptions // ignore: cast_nullable_to_non_nullable
              as String?,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$_FrontMatterModel implements _FrontMatterModel {
  const _$_FrontMatterModel(
      {required this.language,
      required this.exerciseType,
      this.title,
      this.difficulty,
      this.compilerOptions});

  factory _$_FrontMatterModel.fromJson(Map<String, dynamic> json) =>
      _$$_FrontMatterModelFromJson(json);

  @override

  /// The language of the exercise, e.g.: `python`
  final String language;
  @override

  /// The type of exercise, e.g.: `1`
  ///
  /// The available exercise types are:
  /// 1 => run code
  /// 2 => fill empty spaces
  /// 3 => choose an answer
  /// 4 => sort items
  final int exerciseType;
  @override

  /// An optional title, mandatory for the challenges, e.g.: `Hello, World!`
  ///
  /// This will be the name of the challenge.
  final String? title;
  @override

  /// An optional difficulty value
  ///
  /// Accepted values are:
  /// 1 => easy
  /// 2 => medium
  /// 3 => hard
  final int? difficulty;
  @override

  /// An optional string that defines with all the compiler options,
  /// e.g.: `-lm` in C tells to link with the standard C libraries
  final String? compilerOptions;

  @override
  String toString() {
    return 'FrontMatterModel(language: $language, exerciseType: $exerciseType, title: $title, difficulty: $difficulty, compilerOptions: $compilerOptions)';
  }

  @override
  bool operator ==(dynamic other) {
    return identical(this, other) ||
        (other is _FrontMatterModel &&
            (identical(other.language, language) ||
                const DeepCollectionEquality()
                    .equals(other.language, language)) &&
            (identical(other.exerciseType, exerciseType) ||
                const DeepCollectionEquality()
                    .equals(other.exerciseType, exerciseType)) &&
            (identical(other.title, title) ||
                const DeepCollectionEquality().equals(other.title, title)) &&
            (identical(other.difficulty, difficulty) ||
                const DeepCollectionEquality()
                    .equals(other.difficulty, difficulty)) &&
            (identical(other.compilerOptions, compilerOptions) ||
                const DeepCollectionEquality()
                    .equals(other.compilerOptions, compilerOptions)));
  }

  @override
  int get hashCode =>
      runtimeType.hashCode ^
      const DeepCollectionEquality().hash(language) ^
      const DeepCollectionEquality().hash(exerciseType) ^
      const DeepCollectionEquality().hash(title) ^
      const DeepCollectionEquality().hash(difficulty) ^
      const DeepCollectionEquality().hash(compilerOptions);

  @JsonKey(ignore: true)
  @override
  _$FrontMatterModelCopyWith<_FrontMatterModel> get copyWith =>
      __$FrontMatterModelCopyWithImpl<_FrontMatterModel>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$_FrontMatterModelToJson(this);
  }
}

abstract class _FrontMatterModel implements FrontMatterModel {
  const factory _FrontMatterModel(
      {required String language,
      required int exerciseType,
      String? title,
      int? difficulty,
      String? compilerOptions}) = _$_FrontMatterModel;

  factory _FrontMatterModel.fromJson(Map<String, dynamic> json) =
      _$_FrontMatterModel.fromJson;

  @override

  /// The language of the exercise, e.g.: `python`
  String get language => throw _privateConstructorUsedError;
  @override

  /// The type of exercise, e.g.: `1`
  ///
  /// The available exercise types are:
  /// 1 => run code
  /// 2 => fill empty spaces
  /// 3 => choose an answer
  /// 4 => sort items
  int get exerciseType => throw _privateConstructorUsedError;
  @override

  /// An optional title, mandatory for the challenges, e.g.: `Hello, World!`
  ///
  /// This will be the name of the challenge.
  String? get title => throw _privateConstructorUsedError;
  @override

  /// An optional difficulty value
  ///
  /// Accepted values are:
  /// 1 => easy
  /// 2 => medium
  /// 3 => hard
  int? get difficulty => throw _privateConstructorUsedError;
  @override

  /// An optional string that defines with all the compiler options,
  /// e.g.: `-lm` in C tells to link with the standard C libraries
  String? get compilerOptions => throw _privateConstructorUsedError;
  @override
  @JsonKey(ignore: true)
  _$FrontMatterModelCopyWith<_FrontMatterModel> get copyWith =>
      throw _privateConstructorUsedError;
}
