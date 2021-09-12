import 'package:freezed_annotation/freezed_annotation.dart';
import 'package:parser/src/blocs/models/assert_model/model.dart';
import 'package:parser/src/blocs/models/code_model/model.dart';
import 'package:parser/src/blocs/models/frontmatter_model/model.dart';

part 'model.freezed.dart';
part 'model.g.dart';

// ignore_for_file: public_member_api_docs
@freezed
class ExerciseModel with _$ExerciseModel {
  const factory ExerciseModel({
    /// The parsed front matter content
    required FrontMatterModel frontMatterModel,

    /// An optional description for the exercise.
    ///
    /// This is used to explain a new topic to the user.
    String? description,

    /// An optional instructions for the exercise.
    ///
    /// This is used to explain what to do to complete the exercise.
    String? instructions,

    /// An optional seed.
    ///
    /// This is used to provide a starting code to the user,
    /// e.g.:
    /// ```
    /// def hello_world():
    ///     return "";
    /// ```
    CodeModel? seed,

    /// The asserts used to validate the exercise.
    List<AssertModel>? asserts,

    /// All the possible answers that are provided to the user.
    List<String>? answers,

    /// All the possible solutions that are used to validate if the
    /// user answer is correct
    List<String>? solutions,

    /// An optional code written before the unit tests.
    ///
    /// This is a good place to put the package imports, like:
    /// ```c
    /// #include <stdio.h>
    /// ```
    CodeModel? codeBeforeAsserts,

    /// An optional code written after the unit tests.
    CodeModel? codeAfterAsserts,

    /// The output of the exercise.
    /// e.g:
    /// Given that your code does something like:
    /// `print("Hello")`
    /// your output will be`
    ///
    /// `Hello`.
    ///
    /// This is often known as the `stdout` (Stardard output).
    String? output,
  }) = _ExerciseModel;

  factory ExerciseModel.fromJson(Map<String, dynamic> json) =>
      _$ExerciseModelFromJson(json);
}
