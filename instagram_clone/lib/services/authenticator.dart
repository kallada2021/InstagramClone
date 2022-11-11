import 'package:instagram_clone/models/user_id.dart';

import '../models/auth_state.dart';

class Authenticator {
  UserId? get userId => 1; //TODO: Call api to get userId
  bool get isAlreadyLoggedIn => userId != null;
  String get username => ""; //TODO: call api to get username
  String get email => ""; // TODO: call api to get email
}

Future<AuthResult> login() async {
  final loginResult = ""; //TODO: call api
  final token = "";
  if (token == null) {
    return AuthResult.aborted;
  }

  try {
    //TODO call login api
    return AuthResult.success;
  } catch (e) {
    return AuthResult.failure;
  }
}
