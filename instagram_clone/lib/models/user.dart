import 'package:equatable/equatable.dart';
import 'package:instagram_clone/models/user_id.dart';

class User extends Equatable {
  UserId? id;
  String? firstname;
  String? lastname;
  String? username;
  String? password;
  String? emailAddress;
  String? token;

  User({
    required this.id,
    required this.firstname,
    required this.lastname,
    required this.username,
    required this.password,
    required this.emailAddress,
  });

  User.fromJson(Map<String, dynamic> json) {
    id = json["id"];
    firstname = json["firstname"];
    lastname = json["lastname"];
    username = json["username"];
    emailAddress = json["email"];
    token = json["token"];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = {};
    data["id"] = id;
    data["firstname"] = firstname;
    data["lastname"] = lastname;
    data["username"] = username;
    data["password"] = password;
    data["email"] = emailAddress;
    return data;
  }

  @override
  List<Object?> get props => [
        id,
        firstname,
        lastname,
        username,
        password,
        emailAddress,
      ];

  @override
  bool? get stringify => true;
}
