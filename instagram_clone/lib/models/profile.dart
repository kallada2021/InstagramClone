import 'package:equatable/equatable.dart';

class ProfileModel extends Equatable {
  final int id;
  final String firstname;
  final String lastname;
  final String username;
  final String password;
  final String location;
  final String aboutMe;
  final Gender gender;
  int age;
  String status;
  String? phoneNumber;
  final UserState isActive;

  ProfileModel({
    required this.id,
    required this.firstname,
    required this.lastname,
    required this.username,
    required this.password,
    required this.location,
    required this.aboutMe,
    required this.gender,
    this.age = 0,
    this.status = "Unavailable",
    this.isActive = UserState.inactive,
  });

  @override
  List<Object?> get props => [
        id,
        firstname,
        lastname,
        username,
        password,
        isActive,
      ];

  @override
  bool? get stringify => true;
}

enum UserState {
  active,
  inactive,
}

enum Gender { male, female }
