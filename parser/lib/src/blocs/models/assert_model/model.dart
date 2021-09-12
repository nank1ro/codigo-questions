import 'package:freezed_annotation/freezed_annotation.dart';

part 'model.freezed.dart';
part 'model.g.dart';

@freezed
class AssertModel with _$AssertModel {
  const factory AssertModel({
    /// The description of the unit test:
    /// e.g: `The function should return "Hello, World!".`
    required String description,

    /// The real unit test to be run.
    /// e.g:
    /// ```python
    /// def test_say_hi(self):
    ///     self.assertEqual(hello(), "Hello, World!", "--err-t1--"
    /// ```
    required String unitTest,
  }) = _AssertModel;

  factory AssertModel.fromJson(Map<String, dynamic> json) =>
      _$AssertModelFromJson(json);
}
