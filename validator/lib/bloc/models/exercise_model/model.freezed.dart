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

ExerciseModel _$ExerciseModelFromJson(Map<String, dynamic> json) {
  return _ExerciseModel.fromJson(json);
}

/// @nodoc
class _$ExerciseModelTearOff {
  const _$ExerciseModelTearOff();

  _ExerciseModel call(
      {required FrontMatterModel frontMatterModel,
      String? description,
      String? instructions,
      CodeModel? seed,
      List<AssertModel>? asserts,
      List<String>? answers,
      List<String>? solutions,
      CodeModel? codeBeforeAsserts,
      CodeModel? codeAfterAsserts,
      String? output}) {
    return _ExerciseModel(
      frontMatterModel: frontMatterModel,
      description: description,
      instructions: instructions,
      seed: seed,
      asserts: asserts,
      answers: answers,
      solutions: solutions,
      codeBeforeAsserts: codeBeforeAsserts,
      codeAfterAsserts: codeAfterAsserts,
      output: output,
    );
  }

  ExerciseModel fromJson(Map<String, Object> json) {
    return ExerciseModel.fromJson(json);
  }
}

/// @nodoc
const $ExerciseModel = _$ExerciseModelTearOff();

/// @nodoc
mixin _$ExerciseModel {
  /// The parsed front matter content
  FrontMatterModel get frontMatterModel => throw _privateConstructorUsedError;

  /// An optional description for the exercise.
  ///
  /// This is used to explain a new topic to the user.
  String? get description => throw _privateConstructorUsedError;

  /// An optional instructions for the exercise.
  ///
  /// This is used to explain what to do to complete the exercise.
  String? get instructions => throw _privateConstructorUsedError;

  /// An optional seed.
  ///
  /// This is used to provide a starting code to the user,
  /// e.g.:
  /// ```
  /// def hello_world():
  ///     return "";
  /// ```
  CodeModel? get seed => throw _privateConstructorUsedError;

  /// The asserts used to validate the exercise.
  List<AssertModel>? get asserts => throw _privateConstructorUsedError;

  /// All the possible answers that are provided to the user.
  List<String>? get answers => throw _privateConstructorUsedError;

  /// All the possible solutions that are used to validate if the
  /// user answer is correct
  List<String>? get solutions => throw _privateConstructorUsedError;

  /// An optional code written before the unit tests.
  ///
  /// This is a good place to put the package imports, like:
  /// ```c
  /// #include <stdio.h>
  /// ```
  CodeModel? get codeBeforeAsserts => throw _privateConstructorUsedError;

  /// An optional code written after the unit tests.
  CodeModel? get codeAfterAsserts => throw _privateConstructorUsedError;

  /// The output of the exercise.
  /// e.g:
  /// Given that your code does something like:
  /// `print("Hello")`
  /// your output will be`
  ///
  /// `Hello`.
  ///
  /// This is often known as the `stdout` (Stardard output).
  String? get output => throw _privateConstructorUsedError;

  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;
  @JsonKey(ignore: true)
  $ExerciseModelCopyWith<ExerciseModel> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $ExerciseModelCopyWith<$Res> {
  factory $ExerciseModelCopyWith(
          ExerciseModel value, $Res Function(ExerciseModel) then) =
      _$ExerciseModelCopyWithImpl<$Res>;
  $Res call(
      {FrontMatterModel frontMatterModel,
      String? description,
      String? instructions,
      CodeModel? seed,
      List<AssertModel>? asserts,
      List<String>? answers,
      List<String>? solutions,
      CodeModel? codeBeforeAsserts,
      CodeModel? codeAfterAsserts,
      String? output});

  $FrontMatterModelCopyWith<$Res> get frontMatterModel;
  $CodeModelCopyWith<$Res>? get seed;
  $CodeModelCopyWith<$Res>? get codeBeforeAsserts;
  $CodeModelCopyWith<$Res>? get codeAfterAsserts;
}

/// @nodoc
class _$ExerciseModelCopyWithImpl<$Res>
    implements $ExerciseModelCopyWith<$Res> {
  _$ExerciseModelCopyWithImpl(this._value, this._then);

  final ExerciseModel _value;
  // ignore: unused_field
  final $Res Function(ExerciseModel) _then;

  @override
  $Res call({
    Object? frontMatterModel = freezed,
    Object? description = freezed,
    Object? instructions = freezed,
    Object? seed = freezed,
    Object? asserts = freezed,
    Object? answers = freezed,
    Object? solutions = freezed,
    Object? codeBeforeAsserts = freezed,
    Object? codeAfterAsserts = freezed,
    Object? output = freezed,
  }) {
    return _then(_value.copyWith(
      frontMatterModel: frontMatterModel == freezed
          ? _value.frontMatterModel
          : frontMatterModel // ignore: cast_nullable_to_non_nullable
              as FrontMatterModel,
      description: description == freezed
          ? _value.description
          : description // ignore: cast_nullable_to_non_nullable
              as String?,
      instructions: instructions == freezed
          ? _value.instructions
          : instructions // ignore: cast_nullable_to_non_nullable
              as String?,
      seed: seed == freezed
          ? _value.seed
          : seed // ignore: cast_nullable_to_non_nullable
              as CodeModel?,
      asserts: asserts == freezed
          ? _value.asserts
          : asserts // ignore: cast_nullable_to_non_nullable
              as List<AssertModel>?,
      answers: answers == freezed
          ? _value.answers
          : answers // ignore: cast_nullable_to_non_nullable
              as List<String>?,
      solutions: solutions == freezed
          ? _value.solutions
          : solutions // ignore: cast_nullable_to_non_nullable
              as List<String>?,
      codeBeforeAsserts: codeBeforeAsserts == freezed
          ? _value.codeBeforeAsserts
          : codeBeforeAsserts // ignore: cast_nullable_to_non_nullable
              as CodeModel?,
      codeAfterAsserts: codeAfterAsserts == freezed
          ? _value.codeAfterAsserts
          : codeAfterAsserts // ignore: cast_nullable_to_non_nullable
              as CodeModel?,
      output: output == freezed
          ? _value.output
          : output // ignore: cast_nullable_to_non_nullable
              as String?,
    ));
  }

  @override
  $FrontMatterModelCopyWith<$Res> get frontMatterModel {
    return $FrontMatterModelCopyWith<$Res>(_value.frontMatterModel, (value) {
      return _then(_value.copyWith(frontMatterModel: value));
    });
  }

  @override
  $CodeModelCopyWith<$Res>? get seed {
    if (_value.seed == null) {
      return null;
    }

    return $CodeModelCopyWith<$Res>(_value.seed!, (value) {
      return _then(_value.copyWith(seed: value));
    });
  }

  @override
  $CodeModelCopyWith<$Res>? get codeBeforeAsserts {
    if (_value.codeBeforeAsserts == null) {
      return null;
    }

    return $CodeModelCopyWith<$Res>(_value.codeBeforeAsserts!, (value) {
      return _then(_value.copyWith(codeBeforeAsserts: value));
    });
  }

  @override
  $CodeModelCopyWith<$Res>? get codeAfterAsserts {
    if (_value.codeAfterAsserts == null) {
      return null;
    }

    return $CodeModelCopyWith<$Res>(_value.codeAfterAsserts!, (value) {
      return _then(_value.copyWith(codeAfterAsserts: value));
    });
  }
}

/// @nodoc
abstract class _$ExerciseModelCopyWith<$Res>
    implements $ExerciseModelCopyWith<$Res> {
  factory _$ExerciseModelCopyWith(
          _ExerciseModel value, $Res Function(_ExerciseModel) then) =
      __$ExerciseModelCopyWithImpl<$Res>;
  @override
  $Res call(
      {FrontMatterModel frontMatterModel,
      String? description,
      String? instructions,
      CodeModel? seed,
      List<AssertModel>? asserts,
      List<String>? answers,
      List<String>? solutions,
      CodeModel? codeBeforeAsserts,
      CodeModel? codeAfterAsserts,
      String? output});

  @override
  $FrontMatterModelCopyWith<$Res> get frontMatterModel;
  @override
  $CodeModelCopyWith<$Res>? get seed;
  @override
  $CodeModelCopyWith<$Res>? get codeBeforeAsserts;
  @override
  $CodeModelCopyWith<$Res>? get codeAfterAsserts;
}

/// @nodoc
class __$ExerciseModelCopyWithImpl<$Res>
    extends _$ExerciseModelCopyWithImpl<$Res>
    implements _$ExerciseModelCopyWith<$Res> {
  __$ExerciseModelCopyWithImpl(
      _ExerciseModel _value, $Res Function(_ExerciseModel) _then)
      : super(_value, (v) => _then(v as _ExerciseModel));

  @override
  _ExerciseModel get _value => super._value as _ExerciseModel;

  @override
  $Res call({
    Object? frontMatterModel = freezed,
    Object? description = freezed,
    Object? instructions = freezed,
    Object? seed = freezed,
    Object? asserts = freezed,
    Object? answers = freezed,
    Object? solutions = freezed,
    Object? codeBeforeAsserts = freezed,
    Object? codeAfterAsserts = freezed,
    Object? output = freezed,
  }) {
    return _then(_ExerciseModel(
      frontMatterModel: frontMatterModel == freezed
          ? _value.frontMatterModel
          : frontMatterModel // ignore: cast_nullable_to_non_nullable
              as FrontMatterModel,
      description: description == freezed
          ? _value.description
          : description // ignore: cast_nullable_to_non_nullable
              as String?,
      instructions: instructions == freezed
          ? _value.instructions
          : instructions // ignore: cast_nullable_to_non_nullable
              as String?,
      seed: seed == freezed
          ? _value.seed
          : seed // ignore: cast_nullable_to_non_nullable
              as CodeModel?,
      asserts: asserts == freezed
          ? _value.asserts
          : asserts // ignore: cast_nullable_to_non_nullable
              as List<AssertModel>?,
      answers: answers == freezed
          ? _value.answers
          : answers // ignore: cast_nullable_to_non_nullable
              as List<String>?,
      solutions: solutions == freezed
          ? _value.solutions
          : solutions // ignore: cast_nullable_to_non_nullable
              as List<String>?,
      codeBeforeAsserts: codeBeforeAsserts == freezed
          ? _value.codeBeforeAsserts
          : codeBeforeAsserts // ignore: cast_nullable_to_non_nullable
              as CodeModel?,
      codeAfterAsserts: codeAfterAsserts == freezed
          ? _value.codeAfterAsserts
          : codeAfterAsserts // ignore: cast_nullable_to_non_nullable
              as CodeModel?,
      output: output == freezed
          ? _value.output
          : output // ignore: cast_nullable_to_non_nullable
              as String?,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$_ExerciseModel implements _ExerciseModel {
  const _$_ExerciseModel(
      {required this.frontMatterModel,
      this.description,
      this.instructions,
      this.seed,
      this.asserts,
      this.answers,
      this.solutions,
      this.codeBeforeAsserts,
      this.codeAfterAsserts,
      this.output});

  factory _$_ExerciseModel.fromJson(Map<String, dynamic> json) =>
      _$$_ExerciseModelFromJson(json);

  @override

  /// The parsed front matter content
  final FrontMatterModel frontMatterModel;
  @override

  /// An optional description for the exercise.
  ///
  /// This is used to explain a new topic to the user.
  final String? description;
  @override

  /// An optional instructions for the exercise.
  ///
  /// This is used to explain what to do to complete the exercise.
  final String? instructions;
  @override

  /// An optional seed.
  ///
  /// This is used to provide a starting code to the user,
  /// e.g.:
  /// ```
  /// def hello_world():
  ///     return "";
  /// ```
  final CodeModel? seed;
  @override

  /// The asserts used to validate the exercise.
  final List<AssertModel>? asserts;
  @override

  /// All the possible answers that are provided to the user.
  final List<String>? answers;
  @override

  /// All the possible solutions that are used to validate if the
  /// user answer is correct
  final List<String>? solutions;
  @override

  /// An optional code written before the unit tests.
  ///
  /// This is a good place to put the package imports, like:
  /// ```c
  /// #include <stdio.h>
  /// ```
  final CodeModel? codeBeforeAsserts;
  @override

  /// An optional code written after the unit tests.
  final CodeModel? codeAfterAsserts;
  @override

  /// The output of the exercise.
  /// e.g:
  /// Given that your code does something like:
  /// `print("Hello")`
  /// your output will be`
  ///
  /// `Hello`.
  ///
  /// This is often known as the `stdout` (Stardard output).
  final String? output;

  @override
  String toString() {
    return 'ExerciseModel(frontMatterModel: $frontMatterModel, description: $description, instructions: $instructions, seed: $seed, asserts: $asserts, answers: $answers, solutions: $solutions, codeBeforeAsserts: $codeBeforeAsserts, codeAfterAsserts: $codeAfterAsserts, output: $output)';
  }

  @override
  bool operator ==(dynamic other) {
    return identical(this, other) ||
        (other is _ExerciseModel &&
            (identical(other.frontMatterModel, frontMatterModel) ||
                const DeepCollectionEquality()
                    .equals(other.frontMatterModel, frontMatterModel)) &&
            (identical(other.description, description) ||
                const DeepCollectionEquality()
                    .equals(other.description, description)) &&
            (identical(other.instructions, instructions) ||
                const DeepCollectionEquality()
                    .equals(other.instructions, instructions)) &&
            (identical(other.seed, seed) ||
                const DeepCollectionEquality().equals(other.seed, seed)) &&
            (identical(other.asserts, asserts) ||
                const DeepCollectionEquality()
                    .equals(other.asserts, asserts)) &&
            (identical(other.answers, answers) ||
                const DeepCollectionEquality()
                    .equals(other.answers, answers)) &&
            (identical(other.solutions, solutions) ||
                const DeepCollectionEquality()
                    .equals(other.solutions, solutions)) &&
            (identical(other.codeBeforeAsserts, codeBeforeAsserts) ||
                const DeepCollectionEquality()
                    .equals(other.codeBeforeAsserts, codeBeforeAsserts)) &&
            (identical(other.codeAfterAsserts, codeAfterAsserts) ||
                const DeepCollectionEquality()
                    .equals(other.codeAfterAsserts, codeAfterAsserts)) &&
            (identical(other.output, output) ||
                const DeepCollectionEquality().equals(other.output, output)));
  }

  @override
  int get hashCode =>
      runtimeType.hashCode ^
      const DeepCollectionEquality().hash(frontMatterModel) ^
      const DeepCollectionEquality().hash(description) ^
      const DeepCollectionEquality().hash(instructions) ^
      const DeepCollectionEquality().hash(seed) ^
      const DeepCollectionEquality().hash(asserts) ^
      const DeepCollectionEquality().hash(answers) ^
      const DeepCollectionEquality().hash(solutions) ^
      const DeepCollectionEquality().hash(codeBeforeAsserts) ^
      const DeepCollectionEquality().hash(codeAfterAsserts) ^
      const DeepCollectionEquality().hash(output);

  @JsonKey(ignore: true)
  @override
  _$ExerciseModelCopyWith<_ExerciseModel> get copyWith =>
      __$ExerciseModelCopyWithImpl<_ExerciseModel>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$_ExerciseModelToJson(this);
  }
}

abstract class _ExerciseModel implements ExerciseModel {
  const factory _ExerciseModel(
      {required FrontMatterModel frontMatterModel,
      String? description,
      String? instructions,
      CodeModel? seed,
      List<AssertModel>? asserts,
      List<String>? answers,
      List<String>? solutions,
      CodeModel? codeBeforeAsserts,
      CodeModel? codeAfterAsserts,
      String? output}) = _$_ExerciseModel;

  factory _ExerciseModel.fromJson(Map<String, dynamic> json) =
      _$_ExerciseModel.fromJson;

  @override

  /// The parsed front matter content
  FrontMatterModel get frontMatterModel => throw _privateConstructorUsedError;
  @override

  /// An optional description for the exercise.
  ///
  /// This is used to explain a new topic to the user.
  String? get description => throw _privateConstructorUsedError;
  @override

  /// An optional instructions for the exercise.
  ///
  /// This is used to explain what to do to complete the exercise.
  String? get instructions => throw _privateConstructorUsedError;
  @override

  /// An optional seed.
  ///
  /// This is used to provide a starting code to the user,
  /// e.g.:
  /// ```
  /// def hello_world():
  ///     return "";
  /// ```
  CodeModel? get seed => throw _privateConstructorUsedError;
  @override

  /// The asserts used to validate the exercise.
  List<AssertModel>? get asserts => throw _privateConstructorUsedError;
  @override

  /// All the possible answers that are provided to the user.
  List<String>? get answers => throw _privateConstructorUsedError;
  @override

  /// All the possible solutions that are used to validate if the
  /// user answer is correct
  List<String>? get solutions => throw _privateConstructorUsedError;
  @override

  /// An optional code written before the unit tests.
  ///
  /// This is a good place to put the package imports, like:
  /// ```c
  /// #include <stdio.h>
  /// ```
  CodeModel? get codeBeforeAsserts => throw _privateConstructorUsedError;
  @override

  /// An optional code written after the unit tests.
  CodeModel? get codeAfterAsserts => throw _privateConstructorUsedError;
  @override

  /// The output of the exercise.
  /// e.g:
  /// Given that your code does something like:
  /// `print("Hello")`
  /// your output will be`
  ///
  /// `Hello`.
  ///
  /// This is often known as the `stdout` (Stardard output).
  String? get output => throw _privateConstructorUsedError;
  @override
  @JsonKey(ignore: true)
  _$ExerciseModelCopyWith<_ExerciseModel> get copyWith =>
      throw _privateConstructorUsedError;
}
