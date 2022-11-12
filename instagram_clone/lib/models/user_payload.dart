import 'dart:collection';

import 'package:flutter/foundation.dart';
import 'package:instagram_clone/constants/json_fields.dart';
import 'package:instagram_clone/models/user_id.dart';

@immutable
class UserInfoPayload extends MapView<String, dynamic> {
  UserInfoPayload({
    required UserId userId,
    required String username,
    required String email,
    required String? firstname,
  }) : super({
          JSONFieldNames.userId: userId,
          JSONFieldNames.username: username,
          JSONFieldNames.email: email,
          JSONFieldNames.firstName: firstname ?? "",
        });
}
