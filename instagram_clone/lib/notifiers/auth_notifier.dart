import 'package:hooks_riverpod/hooks_riverpod.dart';
import 'package:instagram_clone/models/auth_state.dart';
import 'package:instagram_clone/services/authenticator.dart';

class AuthStateNotifier extends StateNotifier<AuthState> {
  final _authenticator = const Authenticator();

  AuthStateNotifier() : super(const AuthState.unknown()) {
    if (_authenticator.isAlreadyLoggedIn) {
      state = AuthState(
        result: AuthResult.success,
        isLoading: false,
        userId: _authenticator.userId,
      );
    }
  }

  Future<void> logOut() async {
    state = state.copiedWithIsLoading(true);
    await _authenticator.logOut();
    state = const AuthState.unknown();
  }

  Future<void> login() async {
    state = state.copiedWithIsLoading(true);
    final result = await _authenticator.login();
    final userId = _authenticator.userId;
    if (result == AuthResult.success && userId != null) {
      // TODO: store login data
    }
  }
}
