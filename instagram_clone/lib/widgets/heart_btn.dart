import 'package:flutter/material.dart';
import 'package:flutter_iconly/flutter_iconly.dart';

import '../constants/utils.dart';

class HeartBTN extends StatelessWidget {
  final String postId;
  bool isClicked = false;

  HeartBTN({
    Key? key,
    required this.postId,
    isClicked = false,
  }) : super(key: key);
  @override
  Widget build(BuildContext context) {
    final Color color = Utils(context).color;
    // final wishlistProvider = Provider.of<WishlistProvider>(context);
    return GestureDetector(
      onTap: () {
        // final User? user = authInstance.currentUser;
        // if (user == null) {
        //   GlobalMethods.errorDialog(subtitle: "Please login", context: context);
        //   return;
        // }
        // print("User id is ${user.uid}");
      },
      child: Icon(
        isClicked == true ? IconlyBold.heart : IconlyLight.heart,
        size: 22,
        color: isClicked == true ? Colors.red : color,
      ),
    );
  }
}
