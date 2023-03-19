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

ExerciseModel _$ExerciseModelFromJson(Map<String, dynamic> json) {
  return _ExerciseModel.fromJson(json);
}

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

  /// An optional code placed before the seed.
  ///
  /// This is used to wrap the seed in something (e.g. a function)
  /// hiding it to the final user.
  /// e.g.:
  /// ```
  /// #include <stdio.h>
  ///
  /// int main() {
  /// ```
  CodeModel? get beforeSeed => throw _privateConstructorUsedError;

  /// An optional code placed after the seed.
  ///
  /// This is used to wrap the seed in something (e.g. a function)
  /// hiding it to the final user.
  /// e.g.:
  /// ```
  ///   return 0;
  /// }
  /// ```
  CodeModel? get afterSeed => throw _privateConstructorUsedError;

  /// The asserts used to validate the exercise.
  List<AssertModel>? get asserts => throw _privateConstructorUsedError;

  /// All the possible answers that are provided to the user.
  List<String>? get answers => throw _privateConstructorUsedError;

  /// All the possible answers that are provided to the user.
  List<CodeModel>? get answersCodeBlocks => throw _privateConstructorUsedError;

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
      _$ExerciseModelCopyWithImpl<$Res, ExerciseModel>;
  @useResult
  $Res call(
      {FrontMatterModel frontMatterModel,
      String? description,
      String? instructions,
      CodeModel? seed,
      CodeModel? beforeSeed,
      CodeModel? afterSeed,
      List<AssertModel>? asserts,
      List<String>? answers,
      List<CodeModel>? answersCodeBlocks,
      List<String>? solutions,
      CodeModel? codeBeforeAsserts,
      CodeModel? codeAfterAsserts,
      String? output});

  $FrontMatterModelCopyWith<$Res> get frontMatterModel;
  $CodeModelCopyWith<$Res>? get seed;
  $CodeModelCopyWith<$Res>? get beforeSeed;
  $CodeModelCopyWith<$Res>? get afterSeed;
  $CodeModelCopyWith<$Res>? get codeBeforeAsserts;
  $CodeModelCopyWith<$Res>? get codeAfterAsserts;
}

/// @nodoc
class _$ExerciseModelCopyWithImpl<$Res, $Val extends ExerciseModel>
    implements $ExerciseModelCopyWith<$Res> {
  _$ExerciseModelCopyWithImpl(this._value, this._then);

  // ignore: unused_field
  final $Val _value;
  // ignore: unused_field
  final $Res Function($Val) _then;

  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? frontMatterModel = null,
    Object? description = freezed,
    Object? instructions = freezed,
    Object? seed = freezed,
    Object? beforeSeed = freezed,
    Object? afterSeed = freezed,
    Object? asserts = freezed,
    Object? answers = freezed,
    Object? answersCodeBlocks = freezed,
    Object? solutions = freezed,
    Object? codeBeforeAsserts = freezed,
    Object? codeAfterAsserts = freezed,
    Object? output = freezed,
  }) {
    return _then(_value.copyWith(
      frontMatterModel: null == frontMatterModel
          ? _value.frontMatterModel
          : frontMatterModel // ignore: cast_nullable_to_non_nullable
              as FrontMatterModel,
      description: freezed == description
          ? _value.description
          : description // ignore: cast_nullable_to_non_nullable
              as String?,
      instructions: freezed == instructions
          ? _value.instructions
          : instructions // ignore: cast_nullable_to_non_nullable
              as String?,
      seed: freezed == seed
          ? _value.seed
          : seed // ignore: cast_nullable_to_non_nullable
              as CodeModel?,
      beforeSeed: freezed == beforeSeed
          ? _value.beforeSeed
          : beforeSeed // ignore: cast_nullable_to_non_nullable
              as CodeModel?,
      afterSeed: freezed == afterSeed
          ? _value.afterSeed
          : afterSeed // ignore: cast_nullable_to_non_nullable
              as CodeModel?,
      asserts: freezed == asserts
          ? _value.asserts
          : asserts // ignore: cast_nullable_to_non_nullable
              as List<AssertModel>?,
      answers: freezed == answers
          ? _value.answers
          : answers // ignore: cast_nullable_to_non_nullable
              as List<String>?,
      answersCodeBlocks: freezed == answersCodeBlocks
          ? _value.answersCodeBlocks
          : answersCodeBlocks // ignore: cast_nullable_to_non_nullable
              as List<CodeModel>?,
      solutions: freezed == solutions
          ? _value.solutions
          : solutions // ignore: cast_nullable_to_non_nullable
              as List<String>?,
      codeBeforeAsserts: freezed == codeBeforeAsserts
          ? _value.codeBeforeAsserts
          : codeBeforeAsserts // ignore: cast_nullable_to_non_nullable
              as CodeModel?,
      codeAfterAsserts: freezed == codeAfterAsserts
          ? _value.codeAfterAsserts
          : codeAfterAsserts // ignore: cast_nullable_to_non_nullable
              as CodeModel?,
      output: freezed == output
          ? _value.output
          : output // ignore: cast_nullable_to_non_nullable
              as String?,
    ) as $Val);
  }

  @override
  @pragma('vm:prefer-inline')
  $FrontMatterModelCopyWith<$Res> get frontMatterModel {
    return $FrontMatterModelCopyWith<$Res>(_value.frontMatterModel, (value) {
      return _then(_value.copyWith(frontMatterModel: value) as $Val);
    });
  }

  @override
  @pragma('vm:prefer-inline')
  $CodeModelCopyWith<$Res>? get seed {
    if (_value.seed == null) {
      return null;
    }

    return $CodeModelCopyWith<$Res>(_value.seed!, (value) {
      return _then(_value.copyWith(seed: value) as $Val);
    });
  }

  @override
  @pragma('vm:prefer-inline')
  $CodeModelCopyWith<$Res>? get beforeSeed {
    if (_value.beforeSeed == null) {
      return null;
    }

    return $CodeModelCopyWith<$Res>(_value.beforeSeed!, (value) {
      return _then(_value.copyWith(beforeSeed: value) as $Val);
    });
  }

  @override
  @pragma('vm:prefer-inline')
  $CodeModelCopyWith<$Res>? get afterSeed {
    if (_value.afterSeed == null) {
      return null;
    }

    return $CodeModelCopyWith<$Res>(_value.afterSeed!, (value) {
      return _then(_value.copyWith(afterSeed: value) as $Val);
    });
  }

  @override
  @pragma('vm:prefer-inline')
  $CodeModelCopyWith<$Res>? get codeBeforeAsserts {
    if (_value.codeBeforeAsserts == null) {
      return null;
    }

    return $CodeModelCopyWith<$Res>(_value.codeBeforeAsserts!, (value) {
      return _then(_value.copyWith(codeBeforeAsserts: value) as $Val);
    });
  }

  @override
  @pragma('vm:prefer-inline')
  $CodeModelCopyWith<$Res>? get codeAfterAsserts {
    if (_value.codeAfterAsserts == null) {
      return null;
    }

    return $CodeModelCopyWith<$Res>(_value.codeAfterAsserts!, (value) {
      return _then(_value.copyWith(codeAfterAsserts: value) as $Val);
    });
  }
}

/// @nodoc
abstract class _$$_ExerciseModelCopyWith<$Res>
    implements $ExerciseModelCopyWith<$Res> {
  factory _$$_ExerciseModelCopyWith(
          _$_ExerciseModel value, $Res Function(_$_ExerciseModel) then) =
      __$$_ExerciseModelCopyWithImpl<$Res>;
  @override
  @useResult
  $Res call(
      {FrontMatterModel frontMatterModel,
      String? description,
      String? instructions,
      CodeModel? seed,
      CodeModel? beforeSeed,
      CodeModel? afterSeed,
      List<AssertModel>? asserts,
      List<String>? answers,
      List<CodeModel>? answersCodeBlocks,
      List<String>? solutions,
      CodeModel? codeBeforeAsserts,
      CodeModel? codeAfterAsserts,
      String? output});

  @override
  $FrontMatterModelCopyWith<$Res> get frontMatterModel;
  @override
  $CodeModelCopyWith<$Res>? get seed;
  @override
  $CodeModelCopyWith<$Res>? get beforeSeed;
  @override
  $CodeModelCopyWith<$Res>? get afterSeed;
  @override
  $CodeModelCopyWith<$Res>? get codeBeforeAsserts;
  @override
  $CodeModelCopyWith<$Res>? get codeAfterAsserts;
}

/// @nodoc
class __$$_ExerciseModelCopyWithImpl<$Res>
    extends _$ExerciseModelCopyWithImpl<$Res, _$_ExerciseModel>
    implements _$$_ExerciseModelCopyWith<$Res> {
  __$$_ExerciseModelCopyWithImpl(
      _$_ExerciseModel _value, $Res Function(_$_ExerciseModel) _then)
      : super(_value, _then);

  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? frontMatterModel = null,
    Object? description = freezed,
    Object? instructions = freezed,
    Object? seed = freezed,
    Object? beforeSeed = freezed,
    Object? afterSeed = freezed,
    Object? asserts = freezed,
    Object? answers = freezed,
    Object? answersCodeBlocks = freezed,
    Object? solutions = freezed,
    Object? codeBeforeAsserts = freezed,
    Object? codeAfterAsserts = freezed,
    Object? output = freezed,
  }) {
    return _then(_$_ExerciseModel(
      frontMatterModel: null == frontMatterModel
          ? _value.frontMatterModel
          : frontMatterModel // ignore: cast_nullable_to_non_nullable
              as FrontMatterModel,
      description: freezed == description
          ? _value.description
          : description // ignore: cast_nullable_to_non_nullable
              as String?,
      instructions: freezed == instructions
          ? _value.instructions
          : instructions // ignore: cast_nullable_to_non_nullable
              as String?,
      seed: freezed == seed
          ? _value.seed
          : seed // ignore: cast_nullable_to_non_nullable
              as CodeModel?,
      beforeSeed: freezed == beforeSeed
          ? _value.beforeSeed
          : beforeSeed // ignore: cast_nullable_to_non_nullable
              as CodeModel?,
      afterSeed: freezed == afterSeed
          ? _value.afterSeed
          : afterSeed // ignore: cast_nullable_to_non_nullable
              as CodeModel?,
      asserts: freezed == asserts
          ? _value._asserts
          : asserts // ignore: cast_nullable_to_non_nullable
              as List<AssertModel>?,
      answers: freezed == answers
          ? _value._answers
          : answers // ignore: cast_nullable_to_non_nullable
              as List<String>?,
      answersCodeBlocks: freezed == answersCodeBlocks
          ? _value._answersCodeBlocks
          : answersCodeBlocks // ignore: cast_nullable_to_non_nullable
              as List<CodeModel>?,
      solutions: freezed == solutions
          ? _value._solutions
          : solutions // ignore: cast_nullable_to_non_nullable
              as List<String>?,
      codeBeforeAsserts: freezed == codeBeforeAsserts
          ? _value.codeBeforeAsserts
          : codeBeforeAsserts // ignore: cast_nullable_to_non_nullable
              as CodeModel?,
      codeAfterAsserts: freezed == codeAfterAsserts
          ? _value.codeAfterAsserts
          : codeAfterAsserts // ignore: cast_nullable_to_non_nullable
              as CodeModel?,
      output: freezed == output
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
      this.beforeSeed,
      this.afterSeed,
      final List<AssertModel>? asserts,
      final List<String>? answers,
      final List<CodeModel>? answersCodeBlocks,
      final List<String>? solutions,
      this.codeBeforeAsserts,
      this.codeAfterAsserts,
      this.output})
      : _asserts = asserts,
        _answers = answers,
        _answersCodeBlocks = answersCodeBlocks,
        _solutions = solutions;

  factory _$_ExerciseModel.fromJson(Map<String, dynamic> json) =>
      _$$_ExerciseModelFromJson(json);

  /// The parsed front matter content
  @override
  final FrontMatterModel frontMatterModel;

  /// An optional description for the exercise.
  ///
  /// This is used to explain a new topic to the user.
  @override
  final String? description;

  /// An optional instructions for the exercise.
  ///
  /// This is used to explain what to do to complete the exercise.
  @override
  final String? instructions;

  /// An optional seed.
  ///
  /// This is used to provide a starting code to the user,
  /// e.g.:
  /// ```
  /// def hello_world():
  ///     return "";
  /// ```
  @override
  final CodeModel? seed;

  /// An optional code placed before the seed.
  ///
  /// This is used to wrap the seed in something (e.g. a function)
  /// hiding it to the final user.
  /// e.g.:
  /// ```
  /// #include <stdio.h>
  ///
  /// int main() {
  /// ```
  @override
  final CodeModel? beforeSeed;

  /// An optional code placed after the seed.
  ///
  /// This is used to wrap the seed in something (e.g. a function)
  /// hiding it to the final user.
  /// e.g.:
  /// ```
  ///   return 0;
  /// }
  /// ```
  @override
  final CodeModel? afterSeed;

  /// The asserts used to validate the exercise.
  final List<AssertModel>? _asserts;

  /// The asserts used to validate the exercise.
  @override
  List<AssertModel>? get asserts {
    final value = _asserts;
    if (value == null) return null;
    if (_asserts is EqualUnmodifiableListView) return _asserts;
    // ignore: implicit_dynamic_type
    return EqualUnmodifiableListView(value);
  }

  /// All the possible answers that are provided to the user.
  final List<String>? _answers;

  /// All the possible answers that are provided to the user.
  @override
  List<String>? get answers {
    final value = _answers;
    if (value == null) return null;
    if (_answers is EqualUnmodifiableListView) return _answers;
    // ignore: implicit_dynamic_type
    return EqualUnmodifiableListView(value);
  }

  /// All the possible answers that are provided to the user.
  final List<CodeModel>? _answersCodeBlocks;

  /// All the possible answers that are provided to the user.
  @override
  List<CodeModel>? get answersCodeBlocks {
    final value = _answersCodeBlocks;
    if (value == null) return null;
    if (_answersCodeBlocks is EqualUnmodifiableListView)
      return _answersCodeBlocks;
    // ignore: implicit_dynamic_type
    return EqualUnmodifiableListView(value);
  }

  /// All the possible solutions that are used to validate if the
  /// user answer is correct
  final List<String>? _solutions;

  /// All the possible solutions that are used to validate if the
  /// user answer is correct
  @override
  List<String>? get solutions {
    final value = _solutions;
    if (value == null) return null;
    if (_solutions is EqualUnmodifiableListView) return _solutions;
    // ignore: implicit_dynamic_type
    return EqualUnmodifiableListView(value);
  }

  /// An optional code written before the unit tests.
  ///
  /// This is a good place to put the package imports, like:
  /// ```c
  /// #include <stdio.h>
  /// ```
  @override
  final CodeModel? codeBeforeAsserts;

  /// An optional code written after the unit tests.
  @override
  final CodeModel? codeAfterAsserts;

  /// The output of the exercise.
  /// e.g:
  /// Given that your code does something like:
  /// `print("Hello")`
  /// your output will be`
  ///
  /// `Hello`.
  ///
  /// This is often known as the `stdout` (Stardard output).
  @override
  final String? output;

  @override
  String toString() {
    return 'ExerciseModel(frontMatterModel: $frontMatterModel, description: $description, instructions: $instructions, seed: $seed, beforeSeed: $beforeSeed, afterSeed: $afterSeed, asserts: $asserts, answers: $answers, answersCodeBlocks: $answersCodeBlocks, solutions: $solutions, codeBeforeAsserts: $codeBeforeAsserts, codeAfterAsserts: $codeAfterAsserts, output: $output)';
  }

  @override
  bool operator ==(dynamic other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$_ExerciseModel &&
            (identical(other.frontMatterModel, frontMatterModel) ||
                other.frontMatterModel == frontMatterModel) &&
            (identical(other.description, description) ||
                other.description == description) &&
            (identical(other.instructions, instructions) ||
                other.instructions == instructions) &&
            (identical(other.seed, seed) || other.seed == seed) &&
            (identical(other.beforeSeed, beforeSeed) ||
                other.beforeSeed == beforeSeed) &&
            (identical(other.afterSeed, afterSeed) ||
                other.afterSeed == afterSeed) &&
            const DeepCollectionEquality().equals(other._asserts, _asserts) &&
            const DeepCollectionEquality().equals(other._answers, _answers) &&
            const DeepCollectionEquality()
                .equals(other._answersCodeBlocks, _answersCodeBlocks) &&
            const DeepCollectionEquality()
                .equals(other._solutions, _solutions) &&
            (identical(other.codeBeforeAsserts, codeBeforeAsserts) ||
                other.codeBeforeAsserts == codeBeforeAsserts) &&
            (identical(other.codeAfterAsserts, codeAfterAsserts) ||
                other.codeAfterAsserts == codeAfterAsserts) &&
            (identical(other.output, output) || other.output == output));
  }

  @JsonKey(ignore: true)
  @override
  int get hashCode => Object.hash(
      runtimeType,
      frontMatterModel,
      description,
      instructions,
      seed,
      beforeSeed,
      afterSeed,
      const DeepCollectionEquality().hash(_asserts),
      const DeepCollectionEquality().hash(_answers),
      const DeepCollectionEquality().hash(_answersCodeBlocks),
      const DeepCollectionEquality().hash(_solutions),
      codeBeforeAsserts,
      codeAfterAsserts,
      output);

  @JsonKey(ignore: true)
  @override
  @pragma('vm:prefer-inline')
  _$$_ExerciseModelCopyWith<_$_ExerciseModel> get copyWith =>
      __$$_ExerciseModelCopyWithImpl<_$_ExerciseModel>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$_ExerciseModelToJson(
      this,
    );
  }
}

abstract class _ExerciseModel implements ExerciseModel {
  const factory _ExerciseModel(
      {required final FrontMatterModel frontMatterModel,
      final String? description,
      final String? instructions,
      final CodeModel? seed,
      final CodeModel? beforeSeed,
      final CodeModel? afterSeed,
      final List<AssertModel>? asserts,
      final List<String>? answers,
      final List<CodeModel>? answersCodeBlocks,
      final List<String>? solutions,
      final CodeModel? codeBeforeAsserts,
      final CodeModel? codeAfterAsserts,
      final String? output}) = _$_ExerciseModel;

  factory _ExerciseModel.fromJson(Map<String, dynamic> json) =
      _$_ExerciseModel.fromJson;

  @override

  /// The parsed front matter content
  FrontMatterModel get frontMatterModel;
  @override

  /// An optional description for the exercise.
  ///
  /// This is used to explain a new topic to the user.
  String? get description;
  @override

  /// An optional instructions for the exercise.
  ///
  /// This is used to explain what to do to complete the exercise.
  String? get instructions;
  @override

  /// An optional seed.
  ///
  /// This is used to provide a starting code to the user,
  /// e.g.:
  /// ```
  /// def hello_world():
  ///     return "";
  /// ```
  CodeModel? get seed;
  @override

  /// An optional code placed before the seed.
  ///
  /// This is used to wrap the seed in something (e.g. a function)
  /// hiding it to the final user.
  /// e.g.:
  /// ```
  /// #include <stdio.h>
  ///
  /// int main() {
  /// ```
  CodeModel? get beforeSeed;
  @override

  /// An optional code placed after the seed.
  ///
  /// This is used to wrap the seed in something (e.g. a function)
  /// hiding it to the final user.
  /// e.g.:
  /// ```
  ///   return 0;
  /// }
  /// ```
  CodeModel? get afterSeed;
  @override

  /// The asserts used to validate the exercise.
  List<AssertModel>? get asserts;
  @override

  /// All the possible answers that are provided to the user.
  List<String>? get answers;
  @override

  /// All the possible answers that are provided to the user.
  List<CodeModel>? get answersCodeBlocks;
  @override

  /// All the possible solutions that are used to validate if the
  /// user answer is correct
  List<String>? get solutions;
  @override

  /// An optional code written before the unit tests.
  ///
  /// This is a good place to put the package imports, like:
  /// ```c
  /// #include <stdio.h>
  /// ```
  CodeModel? get codeBeforeAsserts;
  @override

  /// An optional code written after the unit tests.
  CodeModel? get codeAfterAsserts;
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
  String? get output;
  @override
  @JsonKey(ignore: true)
  _$$_ExerciseModelCopyWith<_$_ExerciseModel> get copyWith =>
      throw _privateConstructorUsedError;
}
