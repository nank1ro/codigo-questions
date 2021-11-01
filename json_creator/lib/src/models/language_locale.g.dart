// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'language_locale.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$_LanguageLocale _$$_LanguageLocaleFromJson(Map<String, dynamic> json) =>
    _$_LanguageLocale(
      locale: json['locale'] as String,
      languages: (json['languages'] as List<dynamic>?)
              ?.map((e) => Language.fromJson(e as Map<String, dynamic>))
              .toList() ??
          [],
    );

Map<String, dynamic> _$$_LanguageLocaleToJson(_$_LanguageLocale instance) =>
    <String, dynamic>{
      'locale': instance.locale,
      'languages': instance.languages,
    };
