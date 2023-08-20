// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'model.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$_AssertModel _$$_AssertModelFromJson(Map<String, dynamic> json) =>
    _$_AssertModel(
      description: json['description'] as String,
      unitTest: json['unitTest'] as String?,
      regexAssert: json['regexAssert'] == null
          ? null
          : RegexAssert.fromJson(json['regexAssert'] as Map<String, dynamic>),
    );

Map<String, dynamic> _$$_AssertModelToJson(_$_AssertModel instance) =>
    <String, dynamic>{
      'description': instance.description,
      'unitTest': instance.unitTest,
      'regexAssert': instance.regexAssert,
    };
