import 'package:hooks_riverpod/hooks_riverpod.dart';
import 'package:instagram_clone/models/post.dart';

final postProvider = ChangeNotifierProvider(
  (ref) => PostDataModel(),
);
