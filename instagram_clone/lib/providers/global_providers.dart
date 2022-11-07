import 'package:hooks_riverpod/hooks_riverpod.dart';
import 'package:instagram_clone/constants/utils.dart';
import 'package:instagram_clone/models/post.dart';

final postProvider = ChangeNotifierProvider(
  (ref) => PostDataModel(),
);

final likedPostStatusProvider = StateProvider<LikeStatus>(
  (ref) => LikeStatus.all,
);

final allPostStatusProvider = StateNotifierProvider<PostsNotifier, List<Post>>(
  (ref) => PostsNotifier(),
);

// Liked post status
final likedPostProvider = Provider<Iterable<Post>>(
  (ref) => ref.watch(allPostStatusProvider).where((post) => post.isLiked),
);

// Not Liked post status
final unlikedPostProvider = Provider<Iterable<Post>>(
  (ref) => ref.watch(allPostStatusProvider).where((post) => !post.isLiked),
);
