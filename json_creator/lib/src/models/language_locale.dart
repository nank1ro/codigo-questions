import 'package:freezed_annotation/freezed_annotation.dart';
import 'package:json_creator/src/models/language.dart';

part 'language_locale.freezed.dart';
part 'language_locale.g.dart';

@freezed
class LanguageLocale with _$LanguageLocale {
  const factory LanguageLocale({
    required String locale,
    @Default(<Language>[]) List<Language> languages,
  }) = _LanguageLocale;

  factory LanguageLocale.fromJson(Map<String, dynamic> json) =>
      _$LanguageLocaleFromJson(json);
}
