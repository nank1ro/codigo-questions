// coverage:ignore-file
// GENERATED CODE - DO NOT MODIFY BY HAND
// ignore_for_file: unused_element, deprecated_member_use, deprecated_member_use_from_same_package, use_function_type_syntax_for_parameters, unnecessary_const, avoid_init_to_null, invalid_override_different_default_values_named, prefer_expression_function_bodies, annotate_overrides, invalid_annotation_target

part of 'argument.dart';

// **************************************************************************
// FreezedGenerator
// **************************************************************************

T _$identity<T>(T value) => value;

final _privateConstructorUsedError = UnsupportedError(
    'It seems like you constructed your class using `MyClass._()`. This constructor is only meant to be used by freezed and you are not supposed to need it nor use it.\nPlease check the documentation here for more informations: https://github.com/rrousselGit/freezed#custom-getters-and-methods');

Argument _$ArgumentFromJson(Map<String, dynamic> json) {
  return _Argument.fromJson(json);
}

/// @nodoc
class _$ArgumentTearOff {
  const _$ArgumentTearOff();

  _Argument call(
      {required String name, int trainUntil = 0, int totalExercises = 0}) {
    return _Argument(
      name: name,
      trainUntil: trainUntil,
      totalExercises: totalExercises,
    );
  }

  Argument fromJson(Map<String, Object> json) {
    return Argument.fromJson(json);
  }
}

/// @nodoc
const $Argument = _$ArgumentTearOff();

/// @nodoc
mixin _$Argument {
  String get name => throw _privateConstructorUsedError;
  int get trainUntil => throw _privateConstructorUsedError;
  int get totalExercises => throw _privateConstructorUsedError;

  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;
  @JsonKey(ignore: true)
  $ArgumentCopyWith<Argument> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $ArgumentCopyWith<$Res> {
  factory $ArgumentCopyWith(Argument value, $Res Function(Argument) then) =
      _$ArgumentCopyWithImpl<$Res>;
  $Res call({String name, int trainUntil, int totalExercises});
}

/// @nodoc
class _$ArgumentCopyWithImpl<$Res> implements $ArgumentCopyWith<$Res> {
  _$ArgumentCopyWithImpl(this._value, this._then);

  final Argument _value;
  // ignore: unused_field
  final $Res Function(Argument) _then;

  @override
  $Res call({
    Object? name = freezed,
    Object? trainUntil = freezed,
    Object? totalExercises = freezed,
  }) {
    return _then(_value.copyWith(
      name: name == freezed
          ? _value.name
          : name // ignore: cast_nullable_to_non_nullable
              as String,
      trainUntil: trainUntil == freezed
          ? _value.trainUntil
          : trainUntil // ignore: cast_nullable_to_non_nullable
              as int,
      totalExercises: totalExercises == freezed
          ? _value.totalExercises
          : totalExercises // ignore: cast_nullable_to_non_nullable
              as int,
    ));
  }
}

/// @nodoc
abstract class _$ArgumentCopyWith<$Res> implements $ArgumentCopyWith<$Res> {
  factory _$ArgumentCopyWith(_Argument value, $Res Function(_Argument) then) =
      __$ArgumentCopyWithImpl<$Res>;
  @override
  $Res call({String name, int trainUntil, int totalExercises});
}

/// @nodoc
class __$ArgumentCopyWithImpl<$Res> extends _$ArgumentCopyWithImpl<$Res>
    implements _$ArgumentCopyWith<$Res> {
  __$ArgumentCopyWithImpl(_Argument _value, $Res Function(_Argument) _then)
      : super(_value, (v) => _then(v as _Argument));

  @override
  _Argument get _value => super._value as _Argument;

  @override
  $Res call({
    Object? name = freezed,
    Object? trainUntil = freezed,
    Object? totalExercises = freezed,
  }) {
    return _then(_Argument(
      name: name == freezed
          ? _value.name
          : name // ignore: cast_nullable_to_non_nullable
              as String,
      trainUntil: trainUntil == freezed
          ? _value.trainUntil
          : trainUntil // ignore: cast_nullable_to_non_nullable
              as int,
      totalExercises: totalExercises == freezed
          ? _value.totalExercises
          : totalExercises // ignore: cast_nullable_to_non_nullable
              as int,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$_Argument implements _Argument {
  const _$_Argument(
      {required this.name, this.trainUntil = 0, this.totalExercises = 0});

  factory _$_Argument.fromJson(Map<String, dynamic> json) =>
      _$$_ArgumentFromJson(json);

  @override
  final String name;
  @JsonKey(defaultValue: 0)
  @override
  final int trainUntil;
  @JsonKey(defaultValue: 0)
  @override
  final int totalExercises;

  @override
  String toString() {
    return 'Argument(name: $name, trainUntil: $trainUntil, totalExercises: $totalExercises)';
  }

  @override
  bool operator ==(dynamic other) {
    return identical(this, other) ||
        (other is _Argument &&
            (identical(other.name, name) ||
                const DeepCollectionEquality().equals(other.name, name)) &&
            (identical(other.trainUntil, trainUntil) ||
                const DeepCollectionEquality()
                    .equals(other.trainUntil, trainUntil)) &&
            (identical(other.totalExercises, totalExercises) ||
                const DeepCollectionEquality()
                    .equals(other.totalExercises, totalExercises)));
  }

  @override
  int get hashCode =>
      runtimeType.hashCode ^
      const DeepCollectionEquality().hash(name) ^
      const DeepCollectionEquality().hash(trainUntil) ^
      const DeepCollectionEquality().hash(totalExercises);

  @JsonKey(ignore: true)
  @override
  _$ArgumentCopyWith<_Argument> get copyWith =>
      __$ArgumentCopyWithImpl<_Argument>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$_ArgumentToJson(this);
  }
}

abstract class _Argument implements Argument {
  const factory _Argument(
      {required String name, int trainUntil, int totalExercises}) = _$_Argument;

  factory _Argument.fromJson(Map<String, dynamic> json) = _$_Argument.fromJson;

  @override
  String get name => throw _privateConstructorUsedError;
  @override
  int get trainUntil => throw _privateConstructorUsedError;
  @override
  int get totalExercises => throw _privateConstructorUsedError;
  @override
  @JsonKey(ignore: true)
  _$ArgumentCopyWith<_Argument> get copyWith =>
      throw _privateConstructorUsedError;
}
