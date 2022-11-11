import 'package:equatable/equatable.dart';
import 'package:instagram_clone/models/user_id.dart';

class Profile extends Equatable {
  final UserId id;
  final String firstname;
  final String lastname;
  final String username;
  final String location;
  final String aboutMe;
  final Gender gender;
  int age;
  String status;
  String? phoneNumber;
  final UserState isActive;

  Profile({
    required this.id,
    required this.firstname,
    required this.lastname,
    required this.username,
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
