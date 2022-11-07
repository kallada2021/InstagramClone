import 'package:flutter/material.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';
import 'package:instagram_clone/widgets/customappbar.dart';

class PostsPage extends ConsumerWidget {
  const PostsPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Scaffold(
      appBar: customAppBar(context),
    );
  }
}
