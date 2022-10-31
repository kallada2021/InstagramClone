import 'package:equatable/equatable.dart';
import 'package:flutter/material.dart';
import 'package:instagram_clone/models/profile.dart';

class Post extends Equatable {
  Profile owner;
  String title;
  String body;
  int likes;
  // TODO: add rest of fields
  Post({
    required this.owner,
    required this.title,
    required this.body,
    this.likes = 0,
  });

  Post updated([String? title, String? body]) => Post(
        owner: owner,
        title: title ?? this.title,
        body: body ?? this.body,
      );

  Post addLike(int numLikes) {
    return Post(body: body, title: title, owner: owner, likes: numLikes + 1);
  }

  Post decreaseLike(int numLikes) {
    return Post(body: body, title: title, owner: owner, likes: numLikes - 1);
  }

  @override
  // TODO: implement remaining props
  List<Object?> get props => [
        owner,
        title,
        body,
      ];

  @override
  bool? get stringify => true;
}

class PostDataModel extends ChangeNotifier {
  final List<Post> _posts = [];

  int get count => _posts.length;

  void addPost(Post post) {
    _posts.add(post);
    notifyListeners();
  }

  void removePost(Post post) {
    _posts.remove(post);
    notifyListeners();
  }

  void update(Post updatedPost) {
    final index = _posts.indexOf(updatedPost);
    final oldPost = _posts[index];

    if (oldPost.title != updatedPost.title || oldPost.body != oldPost.body) {
      _posts[index] = oldPost.updated(
        updatedPost.title,
        updatedPost.body,
      );
      notifyListeners();
    }
  }
}
