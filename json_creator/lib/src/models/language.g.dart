// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'language.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$_Language _$$_LanguageFromJson(Map<String, dynamic> json) => _$_Language(
      name: json['name'] as String,
      arguments: (json['arguments'] as List<dynamic>?)
              ?.map((e) => Argument.fromJson(e as Map<String, dynamic>))
              .toList() ??
          [],
      totalExercises: json['totalExercises'] as int? ?? 0,
    );

Map<String, dynamic> _$$_LanguageToJson(_$_Language instance) =>
    <String, dynamic>{
      'name': instance.name,
      'arguments': instance.arguments,
      'totalExercises': instance.totalExercises,
    };
