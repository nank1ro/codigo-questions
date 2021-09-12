import 'package:freezed_annotation/freezed_annotation.dart';

part 'model.freezed.dart';
part 'model.g.dart';

// ignore_for_file: public_member_api_docs
@freezed
class CodeModel with _$CodeModel {
  const factory CodeModel({
    required String language,
    required String code,
  }) = _CodeModel;

  factory CodeModel.fromJson(Map<String, dynamic> json) =>
      _$CodeModelFromJson(json);
}
