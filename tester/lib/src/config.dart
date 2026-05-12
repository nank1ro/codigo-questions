import 'dart:io';

import 'package:dotenv/dotenv.dart';

class TesterConfig {
  TesterConfig({
    required this.codecompilerUrl,
    required this.firebaseApiKey,
    required this.firebaseDatabaseUrl,
    required this.timeoutSec,
  });

  final Uri codecompilerUrl;
  final String firebaseApiKey;
  final Uri firebaseDatabaseUrl;
  final int timeoutSec;

  static TesterConfig load() {
    final env = DotEnv(includePlatformEnvironment: true)..load();

    final url = env['CODECOMPILER_URL'] ?? 'http://localhost:8080/hereford_rpc';
    final apiKey = env['FIREBASE_API_KEY'];
    final dbUrl = env['FIREBASE_DATABASE_URL'] ??
        'https://learn-to-code-x-europe.europe-west1.firebasedatabase.app';
    final timeout = int.tryParse(env['TESTER_TIMEOUT_SEC'] ?? '') ?? 30;

    if (apiKey == null || apiKey.isEmpty) {
      stderr.writeln(
        'ERROR: FIREBASE_API_KEY is required. Copy tester/.env.template to '
        'tester/.env and fill it in (use values from codecompiler/.env).',
      );
      exit(2);
    }

    return TesterConfig(
      codecompilerUrl: Uri.parse(url),
      firebaseApiKey: apiKey,
      firebaseDatabaseUrl: Uri.parse(dbUrl),
      timeoutSec: timeout,
    );
  }
}
