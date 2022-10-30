import 'package:instagram_clone/models/profile.dart';
import 'package:instagram_clone/models/user.dart';

User getLoggedInUser() {
  return User(
    id: 1,
    firstname: "Abdullah",
    lastname: "User",
    username: "au123",
    password: "",
    emailAddress: "abc@abc.com",
  );
}

Profile getLoggedInUserProfile() {
  return Profile(
    id: 1,
    firstname: "Abdullah",
    lastname: "User",
    username: "u123",
    location: "Earth",
    aboutMe: "About Me",
    gender: Gender.male,
  );
}
