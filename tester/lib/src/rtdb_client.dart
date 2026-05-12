import 'dart:async';
import 'dart:convert';

import 'package:http/http.dart' as http;

class SubmissionResult {
  SubmissionResult({this.compilationResult, this.error});

  final CompilationResult? compilationResult;
  final SubmissionError? error;

  factory SubmissionResult.fromJson(Map<String, dynamic> json) {
    return SubmissionResult(
      compilationResult: json['compilationResult'] is Map
          ? CompilationResult.fromJson(
              Map<String, dynamic>.from(json['compilationResult'] as Map),
            )
          : null,
      error: json['error'] is Map
          ? SubmissionError.fromJson(
              Map<String, dynamic>.from(json['error'] as Map),
            )
          : null,
    );
  }
}

class CompilationResult {
  CompilationResult({
    required this.exitCode,
    required this.time,
    this.stdout,
    this.stderr,
  });

  final int exitCode;
  final double time;
  final String? stdout;
  final String? stderr;

  factory CompilationResult.fromJson(Map<String, dynamic> json) {
    return CompilationResult(
      exitCode: (json['exitCode'] as num?)?.toInt() ?? 0,
      time: (json['time'] as num?)?.toDouble() ?? 0,
      stdout: json['stdout'] as String?,
      stderr: json['stderr'] as String?,
    );
  }
}

class SubmissionError {
  SubmissionError({required this.code, required this.message, this.data});

  final int code;
  final String message;
  final Map<String, dynamic>? data;

  factory SubmissionError.fromJson(Map<String, dynamic> json) {
    return SubmissionError(
      code: (json['code'] as num?)?.toInt() ?? 0,
      message: json['message'] as String? ?? '',
      data: json['data'] is Map
          ? Map<String, dynamic>.from(json['data'] as Map)
          : null,
    );
  }
}

class SubmissionTimeout implements Exception {
  SubmissionTimeout(this.submissionId, this.elapsed);
  final String submissionId;
  final Duration elapsed;
  @override
  String toString() =>
      'SubmissionTimeout(id=$submissionId, after ${elapsed.inSeconds}s)';
}

/// Polls the Firebase Realtime Database REST endpoint for a submission result.
///
/// The production app uses the streaming SDK; for a CLI tool, REST polling
/// at 500ms intervals is simpler and adequate (codecompiler serialises
/// submissions internally via a global mutex).
class RtdbClient {
  RtdbClient({
    required this.databaseUrl,
    required this.authToken,
    this.pollInterval = const Duration(milliseconds: 500),
    http.Client? client,
  }) : _client = client ?? http.Client();

  final Uri databaseUrl;
  final String authToken;
  final Duration pollInterval;
  final http.Client _client;

  Future<SubmissionResult> waitFor(
    String submissionId, {
    required Duration timeout,
  }) async {
    final url = databaseUrl.replace(
      path: '${databaseUrl.path}/submissions/$submissionId.json'
          .replaceAll('//', '/'),
      queryParameters: {'auth': authToken},
    );

    final deadline = DateTime.now().add(timeout);
    while (DateTime.now().isBefore(deadline)) {
      final resp = await _client.get(url);
      if (resp.statusCode != 200) {
        throw StateError(
          'RTDB GET failed (${resp.statusCode}): ${resp.body}',
        );
      }
      if (resp.body.isNotEmpty && resp.body != 'null') {
        final decoded = jsonDecode(resp.body) as Map<String, dynamic>;
        return SubmissionResult.fromJson(decoded);
      }
      await Future<void>.delayed(pollInterval);
    }

    throw SubmissionTimeout(submissionId, timeout);
  }

  void close() => _client.close();
}
