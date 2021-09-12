// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'model.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$_FrontMatterModel _$$_FrontMatterModelFromJson(Map<String, dynamic> json) =>
    _$_FrontMatterModel(
      language: json['language'] as String,
      exerciseType: json['exerciseType'] as int,
      title: json['title'] as String?,
      difficulty: json['difficulty'] as int?,
    );

Map<String, dynamic> _$$_FrontMatterModelToJson(_$_FrontMatterModel instance) =>
    <String, dynamic>{
      'language': instance.language,
      'exerciseType': instance.exerciseType,
      'title': instance.title,
      'difficulty': instance.difficulty,
    };
