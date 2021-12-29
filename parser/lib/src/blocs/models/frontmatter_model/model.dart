import 'package:freezed_annotation/freezed_annotation.dart';

part 'model.freezed.dart';
part 'model.g.dart';

// ignore_for_file: public_member_api_docs
@freezed
class FrontMatterModel with _$FrontMatterModel {
  const factory FrontMatterModel({
    /// The language of the exercise, e.g.: `python`
    required String language,

    /// The type of exercise, e.g.: `1`
    ///
    /// The available exercise types are:
    /// 1 => run code
    /// 2 => fill empty spaces
    /// 3 => choose an answer
    /// 4 => sort items
    required int exerciseType,

    /// An optional title, mandatory for the challenges, e.g.: `Hello, World!`
    ///
    /// This will be the name of the challenge.
    String? title,

    /// An optional difficulty value
    ///
    /// Accepted values are:
    /// 1 => easy
    /// 2 => medium
    /// 3 => hard
    int? difficulty,

    /// An optional string that defines all the compiler options,
    /// e.g.: `-lm` in C tells to link with the standard C libraries
    String? compilerOptions,
  }) = _FrontMatterModel;

  factory FrontMatterModel.fromJson(Map<String, dynamic> json) =>
      _$FrontMatterModelFromJson(json);
}
