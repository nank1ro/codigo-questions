// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'model.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$_ExerciseModel _$$_ExerciseModelFromJson(Map<String, dynamic> json) =>
    _$_ExerciseModel(
      frontMatterModel: FrontMatterModel.fromJson(
          json['frontMatterModel'] as Map<String, dynamic>),
      description: json['description'] as String?,
      instructions: json['instructions'] as String?,
      seed: json['seed'] == null
          ? null
          : CodeModel.fromJson(json['seed'] as Map<String, dynamic>),
      asserts: (json['asserts'] as List<dynamic>?)
          ?.map((e) => AssertModel.fromJson(e as Map<String, dynamic>))
          .toList(),
      answers:
          (json['answers'] as List<dynamic>?)?.map((e) => e as String).toList(),
      solutions: (json['solutions'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      codeBeforeAsserts: json['codeBeforeAsserts'] == null
          ? null
          : CodeModel.fromJson(
              json['codeBeforeAsserts'] as Map<String, dynamic>),
      codeAfterAsserts: json['codeAfterAsserts'] == null
          ? null
          : CodeModel.fromJson(
              json['codeAfterAsserts'] as Map<String, dynamic>),
      output: json['output'] as String?,
    );

Map<String, dynamic> _$$_ExerciseModelToJson(_$_ExerciseModel instance) =>
    <String, dynamic>{
      'frontMatterModel': instance.frontMatterModel,
      'description': instance.description,
      'instructions': instance.instructions,
      'seed': instance.seed,
      'asserts': instance.asserts,
      'answers': instance.answers,
      'solutions': instance.solutions,
      'codeBeforeAsserts': instance.codeBeforeAsserts,
      'codeAfterAsserts': instance.codeAfterAsserts,
      'output': instance.output,
    };
