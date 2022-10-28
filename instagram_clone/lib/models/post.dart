import 'package:equatable/equatable.dart';

class PostModel extends Equatable {
  String owner;
  String title;
  // TODO: add rest of fields
  PostModel({
    required this.owner,
    required this.title,
  });

  @override
  // TODO: implement remaining props
  List<Object?> get props => [owner, title];

  @override
  bool? get stringify => true;
}
