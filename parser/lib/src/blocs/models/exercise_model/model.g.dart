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
      beforeSeed: json['beforeSeed'] == null
          ? null
          : CodeModel.fromJson(json['beforeSeed'] as Map<String, dynamic>),
      afterSeed: json['afterSeed'] == null
          ? null
          : CodeModel.fromJson(json['afterSeed'] as Map<String, dynamic>),
      asserts: (json['asserts'] as List<dynamic>?)
          ?.map((e) => AssertModel.fromJson(e as Map<String, dynamic>))
          .toList(),
      answers:
          (json['answers'] as List<dynamic>?)?.map((e) => e as String).toList(),
      answersCodeBlocks: (json['answersCodeBlocks'] as List<dynamic>?)
          ?.map((e) => CodeModel.fromJson(e as Map<String, dynamic>))
          .toList(),
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
      'beforeSeed': instance.beforeSeed,
      'afterSeed': instance.afterSeed,
      'asserts': instance.asserts,
      'answers': instance.answers,
      'answersCodeBlocks': instance.answersCodeBlocks,
      'solutions': instance.solutions,
      'codeBeforeAsserts': instance.codeBeforeAsserts,
      'codeAfterAsserts': instance.codeAfterAsserts,
      'output': instance.output,
    };
