import 'dart:convert';

import 'package:http/http.dart' as http;

import 'composer.dart';

class CodecompilerError implements Exception {
  CodecompilerError({required this.code, required this.message, this.data});

  final int code;
  final String message;
  final Map<String, dynamic>? data;

  @override
  String toString() =>
      'CodecompilerError($code, $message${data == null ? '' : ', $data'})';
}

/// HTTP JSON-RPC client for the production codecompiler service.
///
/// Mirrors codigo_x/lib/services/codecompiler_service.dart. Posts to
/// `Hereford.Compile` and returns the async submission UUID — the actual
/// pass/fail arrives later in Firebase RTDB under `submissions/<id>`.
class CodecompilerClient {
  CodecompilerClient({
    required this.endpoint,
    required this.authToken,
    this.appVersion = '2.1.0',
    http.Client? client,
  }) : _client = client ?? http.Client();

  final Uri endpoint;
  final String authToken;
  final String appVersion;
  final http.Client _client;

  Future<String> submit(ComposedExercise exercise) async {
    final params = <String, dynamic>{
      'languageID': exercise.languageId,
      'sourceCode': base64.encode(utf8.encode(exercise.sourceCode)),
      'testCode': exercise.testCode == null
          ? null
          : base64.encode(utf8.encode(exercise.testCode!)),
      'stdin': null,
      'commandLineArgs': <String>[],
      'compilerOptions': <String>[],
    };
    final body = jsonEncode({
      'id': 1,
      'jsonrpc': '2.0',
      'method': 'Hereford.Compile',
      'params': params,
    });

    final resp = await _client.post(
      endpoint,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer $authToken',
        'X-ClientID': 'codigo/$appVersion',
      },
      body: body,
    );

    final decoded = jsonDecode(resp.body) as Map<String, dynamic>;

    if (decoded['error'] != null) {
      final err = decoded['error'] as Map<String, dynamic>;
      throw CodecompilerError(
        code: (err['code'] as num).toInt(),
        message: err['message'] as String? ?? 'unknown',
        data: err['data'] as Map<String, dynamic>?,
      );
    }

    final result = decoded['result'];
    if (result is String && result.isNotEmpty) return result;

    throw StateError(
      'codecompiler returned unexpected body (status ${resp.statusCode}): '
      '${resp.body}',
    );
  }

  void close() => _client.close();
}
