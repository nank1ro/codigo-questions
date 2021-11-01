// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'argument.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$_Argument _$$_ArgumentFromJson(Map<String, dynamic> json) => _$_Argument(
      name: json['name'] as String,
      trainUntil: json['trainUntil'] as int? ?? 0,
      totalExercises: json['totalExercises'] as int? ?? 0,
    );

Map<String, dynamic> _$$_ArgumentToJson(_$_Argument instance) =>
    <String, dynamic>{
      'name': instance.name,
      'trainUntil': instance.trainUntil,
      'totalExercises': instance.totalExercises,
    };
