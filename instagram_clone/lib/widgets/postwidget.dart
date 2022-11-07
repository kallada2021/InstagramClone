import 'package:flutter/material.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';
import 'package:instagram_clone/providers/global_providers.dart';
import 'package:instagram_clone/widgets/heart_btn.dart';

import '../constants/utils.dart';
import '../models/post.dart';

class PostWidget extends ConsumerWidget {
  final AlwaysAliveProviderBase<Iterable<Post>> provider;
  const PostWidget({required this.provider, Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final posts = ref.watch(provider);
    return Expanded(
      child: ListView.builder(
        itemCount: posts.length,
        itemBuilder: (context, index) {
          final post = posts.elementAt(index);
          final likedIcon = post.isLiked
              ? HeartBTN(
                  postId: post.id.toString(),
                  isClicked: true,
                )
              : HeartBTN(
                  postId: post.id.toString(),
                  isClicked: false,
                );

          return ListTile(
            trailing: likedIcon,
            title: Text(post.title),
            subtitle: Text(post.body),
            leading: Text(post.likes.toString()),
          );
        },
      ),
    );
  }
}

class PostFilterWidget extends StatelessWidget {
  const PostFilterWidget({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Consumer(
      builder: (context, ref, child) {
        return DropdownButton(
          value: ref.watch(likedPostStatusProvider),
          items: LikeStatus.values
              .map(
                (ps) => DropdownMenuItem(
                  value: ps,
                  child: Text(
                    ps.toString().split(".").last,
                  ),
                ),
              )
              .toList(),
          onChanged: (LikeStatus? ps) {
            ref
                .read(
                  likedPostStatusProvider.state,
                )
                .state = ps!;
          },
        );
      },
    );
  }
}
