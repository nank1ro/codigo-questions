import 'package:freezed_annotation/freezed_annotation.dart';

part 'argument.freezed.dart';
part 'argument.g.dart';

@freezed
class Argument with _$Argument {
  const factory Argument({
    required String name,
    @Default(0) int trainUntil,
    @Default(0) int totalExercises,
  }) = _Argument;

  factory Argument.fromJson(Map<String, dynamic> json) =>
      _$ArgumentFromJson(json);
}
