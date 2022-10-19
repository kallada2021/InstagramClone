import 'package:equatable/equatable.dart';

class UserModel extends Equatable {
  final int id;
  final String firstname;
  final String lastname;
  final String username;
  final String password;

  UserModel({
    required this.id,
    required this.firstname,
    required this.lastname,
    required this.username,
    required this.password,
  });

  @override
  List<Object?> get props => [
        id,
        firstname,
        lastname,
        username,
        password,
      ];

  @override
  bool? get stringify => true;
}
