import 'package:freezed_annotation/freezed_annotation.dart';
import 'package:json_creator/src/models/argument.dart';

part 'language.freezed.dart';
part 'language.g.dart';

@freezed
class Language with _$Language {
  const factory Language({
    required String name,
    @Default(<Argument>[]) List<Argument> arguments,
    @Default(0) int totalExercises,
  }) = _Language;

  factory Language.fromJson(Map<String, dynamic> json) =>
      _$LanguageFromJson(json);
}
