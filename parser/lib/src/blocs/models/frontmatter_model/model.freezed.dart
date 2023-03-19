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

FrontMatterModel _$FrontMatterModelFromJson(Map<String, dynamic> json) {
  return _FrontMatterModel.fromJson(json);
}

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

  /// An optional string that defines all the compiler options,
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
      _$FrontMatterModelCopyWithImpl<$Res, FrontMatterModel>;
  @useResult
  $Res call(
      {String language,
      int exerciseType,
      String? title,
      int? difficulty,
      String? compilerOptions});
}

/// @nodoc
class _$FrontMatterModelCopyWithImpl<$Res, $Val extends FrontMatterModel>
    implements $FrontMatterModelCopyWith<$Res> {
  _$FrontMatterModelCopyWithImpl(this._value, this._then);

  // ignore: unused_field
  final $Val _value;
  // ignore: unused_field
  final $Res Function($Val) _then;

  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? language = null,
    Object? exerciseType = null,
    Object? title = freezed,
    Object? difficulty = freezed,
    Object? compilerOptions = freezed,
  }) {
    return _then(_value.copyWith(
      language: null == language
          ? _value.language
          : language // ignore: cast_nullable_to_non_nullable
              as String,
      exerciseType: null == exerciseType
          ? _value.exerciseType
          : exerciseType // ignore: cast_nullable_to_non_nullable
              as int,
      title: freezed == title
          ? _value.title
          : title // ignore: cast_nullable_to_non_nullable
              as String?,
      difficulty: freezed == difficulty
          ? _value.difficulty
          : difficulty // ignore: cast_nullable_to_non_nullable
              as int?,
      compilerOptions: freezed == compilerOptions
          ? _value.compilerOptions
          : compilerOptions // ignore: cast_nullable_to_non_nullable
              as String?,
    ) as $Val);
  }
}

/// @nodoc
abstract class _$$_FrontMatterModelCopyWith<$Res>
    implements $FrontMatterModelCopyWith<$Res> {
  factory _$$_FrontMatterModelCopyWith(
          _$_FrontMatterModel value, $Res Function(_$_FrontMatterModel) then) =
      __$$_FrontMatterModelCopyWithImpl<$Res>;
  @override
  @useResult
  $Res call(
      {String language,
      int exerciseType,
      String? title,
      int? difficulty,
      String? compilerOptions});
}

/// @nodoc
class __$$_FrontMatterModelCopyWithImpl<$Res>
    extends _$FrontMatterModelCopyWithImpl<$Res, _$_FrontMatterModel>
    implements _$$_FrontMatterModelCopyWith<$Res> {
  __$$_FrontMatterModelCopyWithImpl(
      _$_FrontMatterModel _value, $Res Function(_$_FrontMatterModel) _then)
      : super(_value, _then);

  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? language = null,
    Object? exerciseType = null,
    Object? title = freezed,
    Object? difficulty = freezed,
    Object? compilerOptions = freezed,
  }) {
    return _then(_$_FrontMatterModel(
      language: null == language
          ? _value.language
          : language // ignore: cast_nullable_to_non_nullable
              as String,
      exerciseType: null == exerciseType
          ? _value.exerciseType
          : exerciseType // ignore: cast_nullable_to_non_nullable
              as int,
      title: freezed == title
          ? _value.title
          : title // ignore: cast_nullable_to_non_nullable
              as String?,
      difficulty: freezed == difficulty
          ? _value.difficulty
          : difficulty // ignore: cast_nullable_to_non_nullable
              as int?,
      compilerOptions: freezed == compilerOptions
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

  /// The language of the exercise, e.g.: `python`
  @override
  final String language;

  /// The type of exercise, e.g.: `1`
  ///
  /// The available exercise types are:
  /// 1 => run code
  /// 2 => fill empty spaces
  /// 3 => choose an answer
  /// 4 => sort items
  @override
  final int exerciseType;

  /// An optional title, mandatory for the challenges, e.g.: `Hello, World!`
  ///
  /// This will be the name of the challenge.
  @override
  final String? title;

  /// An optional difficulty value
  ///
  /// Accepted values are:
  /// 1 => easy
  /// 2 => medium
  /// 3 => hard
  @override
  final int? difficulty;

  /// An optional string that defines all the compiler options,
  /// e.g.: `-lm` in C tells to link with the standard C libraries
  @override
  final String? compilerOptions;

  @override
  String toString() {
    return 'FrontMatterModel(language: $language, exerciseType: $exerciseType, title: $title, difficulty: $difficulty, compilerOptions: $compilerOptions)';
  }

  @override
  bool operator ==(dynamic other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$_FrontMatterModel &&
            (identical(other.language, language) ||
                other.language == language) &&
            (identical(other.exerciseType, exerciseType) ||
                other.exerciseType == exerciseType) &&
            (identical(other.title, title) || other.title == title) &&
            (identical(other.difficulty, difficulty) ||
                other.difficulty == difficulty) &&
            (identical(other.compilerOptions, compilerOptions) ||
                other.compilerOptions == compilerOptions));
  }

  @JsonKey(ignore: true)
  @override
  int get hashCode => Object.hash(
      runtimeType, language, exerciseType, title, difficulty, compilerOptions);

  @JsonKey(ignore: true)
  @override
  @pragma('vm:prefer-inline')
  _$$_FrontMatterModelCopyWith<_$_FrontMatterModel> get copyWith =>
      __$$_FrontMatterModelCopyWithImpl<_$_FrontMatterModel>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$_FrontMatterModelToJson(
      this,
    );
  }
}

abstract class _FrontMatterModel implements FrontMatterModel {
  const factory _FrontMatterModel(
      {required final String language,
      required final int exerciseType,
      final String? title,
      final int? difficulty,
      final String? compilerOptions}) = _$_FrontMatterModel;

  factory _FrontMatterModel.fromJson(Map<String, dynamic> json) =
      _$_FrontMatterModel.fromJson;

  @override

  /// The language of the exercise, e.g.: `python`
  String get language;
  @override

  /// The type of exercise, e.g.: `1`
  ///
  /// The available exercise types are:
  /// 1 => run code
  /// 2 => fill empty spaces
  /// 3 => choose an answer
  /// 4 => sort items
  int get exerciseType;
  @override

  /// An optional title, mandatory for the challenges, e.g.: `Hello, World!`
  ///
  /// This will be the name of the challenge.
  String? get title;
  @override

  /// An optional difficulty value
  ///
  /// Accepted values are:
  /// 1 => easy
  /// 2 => medium
  /// 3 => hard
  int? get difficulty;
  @override

  /// An optional string that defines all the compiler options,
  /// e.g.: `-lm` in C tells to link with the standard C libraries
  String? get compilerOptions;
  @override
  @JsonKey(ignore: true)
  _$$_FrontMatterModelCopyWith<_$_FrontMatterModel> get copyWith =>
      throw _privateConstructorUsedError;
}
