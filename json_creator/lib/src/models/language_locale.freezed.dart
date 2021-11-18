// coverage:ignore-file
// GENERATED CODE - DO NOT MODIFY BY HAND
// ignore_for_file: unused_element, deprecated_member_use, deprecated_member_use_from_same_package, use_function_type_syntax_for_parameters, unnecessary_const, avoid_init_to_null, invalid_override_different_default_values_named, prefer_expression_function_bodies, annotate_overrides, invalid_annotation_target

part of 'language_locale.dart';

// **************************************************************************
// FreezedGenerator
// **************************************************************************

T _$identity<T>(T value) => value;

final _privateConstructorUsedError = UnsupportedError(
    'It seems like you constructed your class using `MyClass._()`. This constructor is only meant to be used by freezed and you are not supposed to need it nor use it.\nPlease check the documentation here for more informations: https://github.com/rrousselGit/freezed#custom-getters-and-methods');

LanguageLocale _$LanguageLocaleFromJson(Map<String, dynamic> json) {
  return _LanguageLocale.fromJson(json);
}

/// @nodoc
class _$LanguageLocaleTearOff {
  const _$LanguageLocaleTearOff();

  _LanguageLocale call(
      {required String locale, List<Language> languages = const <Language>[]}) {
    return _LanguageLocale(
      locale: locale,
      languages: languages,
    );
  }

  LanguageLocale fromJson(Map<String, Object> json) {
    return LanguageLocale.fromJson(json);
  }
}

/// @nodoc
const $LanguageLocale = _$LanguageLocaleTearOff();

/// @nodoc
mixin _$LanguageLocale {
  String get locale => throw _privateConstructorUsedError;
  List<Language> get languages => throw _privateConstructorUsedError;

  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;
  @JsonKey(ignore: true)
  $LanguageLocaleCopyWith<LanguageLocale> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $LanguageLocaleCopyWith<$Res> {
  factory $LanguageLocaleCopyWith(
          LanguageLocale value, $Res Function(LanguageLocale) then) =
      _$LanguageLocaleCopyWithImpl<$Res>;
  $Res call({String locale, List<Language> languages});
}

/// @nodoc
class _$LanguageLocaleCopyWithImpl<$Res>
    implements $LanguageLocaleCopyWith<$Res> {
  _$LanguageLocaleCopyWithImpl(this._value, this._then);

  final LanguageLocale _value;
  // ignore: unused_field
  final $Res Function(LanguageLocale) _then;

  @override
  $Res call({
    Object? locale = freezed,
    Object? languages = freezed,
  }) {
    return _then(_value.copyWith(
      locale: locale == freezed
          ? _value.locale
          : locale // ignore: cast_nullable_to_non_nullable
              as String,
      languages: languages == freezed
          ? _value.languages
          : languages // ignore: cast_nullable_to_non_nullable
              as List<Language>,
    ));
  }
}

/// @nodoc
abstract class _$LanguageLocaleCopyWith<$Res>
    implements $LanguageLocaleCopyWith<$Res> {
  factory _$LanguageLocaleCopyWith(
          _LanguageLocale value, $Res Function(_LanguageLocale) then) =
      __$LanguageLocaleCopyWithImpl<$Res>;
  @override
  $Res call({String locale, List<Language> languages});
}

/// @nodoc
class __$LanguageLocaleCopyWithImpl<$Res>
    extends _$LanguageLocaleCopyWithImpl<$Res>
    implements _$LanguageLocaleCopyWith<$Res> {
  __$LanguageLocaleCopyWithImpl(
      _LanguageLocale _value, $Res Function(_LanguageLocale) _then)
      : super(_value, (v) => _then(v as _LanguageLocale));

  @override
  _LanguageLocale get _value => super._value as _LanguageLocale;

  @override
  $Res call({
    Object? locale = freezed,
    Object? languages = freezed,
  }) {
    return _then(_LanguageLocale(
      locale: locale == freezed
          ? _value.locale
          : locale // ignore: cast_nullable_to_non_nullable
              as String,
      languages: languages == freezed
          ? _value.languages
          : languages // ignore: cast_nullable_to_non_nullable
              as List<Language>,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$_LanguageLocale implements _LanguageLocale {
  const _$_LanguageLocale(
      {required this.locale, this.languages = const <Language>[]});

  factory _$_LanguageLocale.fromJson(Map<String, dynamic> json) =>
      _$$_LanguageLocaleFromJson(json);

  @override
  final String locale;
  @JsonKey(defaultValue: const <Language>[])
  @override
  final List<Language> languages;

  @override
  String toString() {
    return 'LanguageLocale(locale: $locale, languages: $languages)';
  }

  @override
  bool operator ==(dynamic other) {
    return identical(this, other) ||
        (other is _LanguageLocale &&
            (identical(other.locale, locale) ||
                const DeepCollectionEquality().equals(other.locale, locale)) &&
            (identical(other.languages, languages) ||
                const DeepCollectionEquality()
                    .equals(other.languages, languages)));
  }

  @override
  int get hashCode =>
      runtimeType.hashCode ^
      const DeepCollectionEquality().hash(locale) ^
      const DeepCollectionEquality().hash(languages);

  @JsonKey(ignore: true)
  @override
  _$LanguageLocaleCopyWith<_LanguageLocale> get copyWith =>
      __$LanguageLocaleCopyWithImpl<_LanguageLocale>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$_LanguageLocaleToJson(this);
  }
}

abstract class _LanguageLocale implements LanguageLocale {
  const factory _LanguageLocale(
      {required String locale, List<Language> languages}) = _$_LanguageLocale;

  factory _LanguageLocale.fromJson(Map<String, dynamic> json) =
      _$_LanguageLocale.fromJson;

  @override
  String get locale => throw _privateConstructorUsedError;
  @override
  List<Language> get languages => throw _privateConstructorUsedError;
  @override
  @JsonKey(ignore: true)
  _$LanguageLocaleCopyWith<_LanguageLocale> get copyWith =>
      throw _privateConstructorUsedError;
}
