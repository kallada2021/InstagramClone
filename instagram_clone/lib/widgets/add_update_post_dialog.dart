import 'package:flutter/material.dart';
import 'package:instagram_clone/models/post.dart';

Future<Post?> createOrUpdatePersonDialog(BuildContext context,
    TextEditingController titleController, TextEditingController bodyController,
    [Post? existingPost]) {
  String? title = existingPost?.title;
  String? body = existingPost?.body;
  titleController.text = title ?? "";
  bodyController.text = body ?? "";

  return showDialog<Post?>(
    context: context,
    builder: (context) {
      return AlertDialog(
        title: const Text("Create a user"),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            TextField(
              controller: titleController,
              decoration: const InputDecoration(
                labelText: "Enter Title Here",
              ),
              onChanged: (value) => title = value,
            ),
            TextField(
              controller: bodyController,
              decoration: const InputDecoration(
                labelText: "Enter Post Here",
              ),
              onChanged: (value) => body = value,
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(),
            child: const Text("CANCEL"),
          ),
          TextButton(
            onPressed: () {
              if (body != null && title != null) {
                if (existingPost != null) {
                  final newPost = existingPost.updated(
                    title,
                    body,
                  );
                  Navigator.of(context).pop(newPost);
                } else {
                  Navigator.of(context).pop(
                    Post(title: title!, body: body!, owner: "Logged in user"),
                  );
                }
              } else {
                Navigator.of(context).pop();
              }
            },
            child: const Text("SAVE"),
          ),
        ],
      );
    },
  );
}
