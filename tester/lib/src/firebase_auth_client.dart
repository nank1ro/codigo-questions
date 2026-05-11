import 'dart:convert';

import 'package:http/http.dart' as http;

/// Anonymous Firebase sign-in via the Identity Toolkit REST API.
///
/// Returns a fresh ID token. The token is short-lived (~1 hour); for a CLI
/// run that takes minutes, fetching once at startup is sufficient.
class FirebaseAuthClient {
  FirebaseAuthClient({required this.apiKey, http.Client? client})
      : _client = client ?? http.Client();

  final String apiKey;
  final http.Client _client;

  Future<String> signInAnonymously() async {
    final url = Uri.https(
      'identitytoolkit.googleapis.com',
      '/v1/accounts:signUp',
      {'key': apiKey},
    );
    final resp = await _client.post(
      url,
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'returnSecureToken': true}),
    );
    if (resp.statusCode != 200) {
      throw StateError(
        'Anonymous sign-in failed (${resp.statusCode}): ${resp.body}',
      );
    }
    final body = jsonDecode(resp.body) as Map<String, dynamic>;
    final token = body['idToken'] as String?;
    if (token == null || token.isEmpty) {
      throw StateError('Anonymous sign-in returned no idToken: ${resp.body}');
    }
    return token;
  }

  void close() => _client.close();
}
