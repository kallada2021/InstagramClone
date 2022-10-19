import 'package:flutter/material.dart';
import 'package:flutter_iconly/flutter_iconly.dart';

import '../constants/utils.dart';

AppBar customAppBar(BuildContext context) {
  Size size = Utils(context).screenSize;
  bool isDark = Utils(context).getTheme;

  return size.width > 1050
      ? AppBar(
          backgroundColor: isDark ? Utils.kLightPink : Utils.kSecondaryColor,
          title: Center(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.start,
              children: [
                Row(
                  children: [
                    const SizedBox(
                      width: Utils.kLineWidth,
                    ),
                    const Text(
                      "INSTAGRAM CLONE",
                      style: TextStyle(
                        fontSize: 16,
                      ),
                    ),
                    SizedBox(
                      width: size.width * 0.2,
                    ),
                    const SizedBox(
                      width: Utils.kLineWidth,
                    ),
                    TextButton(
                      onPressed: () {
                        if (Navigator.canPop(context)) {
                          Navigator.pop(context);
                        }
                        // TODO: add route
                      },
                      child: Text(
                        "Users",
                        style: Utils.kAppBarTextStyle,
                      ),
                    ),
                    const SizedBox(
                      width: Utils.kLineWidth,
                    ),
                    TextButton(
                      onPressed: () {
                        if (Navigator.canPop(context)) {
                          Navigator.pop(context);
                        }
                        //TODO: add route
                      },
                      child: Text(
                        "Posts",
                        style: Utils.kAppBarTextStyle,
                      ),
                    ),
                    const SizedBox(
                      width: Utils.kLineWidth,
                    ),
                    TextButton(
                      onPressed: () {
                        if (Navigator.canPop(context)) {
                          Navigator.pop(context);
                        }
                      },
                      child: Text(
                        "What's New",
                        style: Utils.kAppBarTextStyle,
                      ),
                    ),
                    const SizedBox(
                      width: Utils.kLineWidth,
                    ),
                  ],
                ),
                Row(
                  children: [
                    TextButton(
                      onPressed: () {
                        if (Navigator.canPop(context)) {
                          Navigator.pop(context);
                        }
                      },
                      child: Text(
                        "Messages",
                        style: Utils.kAppBarTextStyle,
                      ),
                    ),
                    IconButton(
                      color: Colors.white,
                      tooltip: "Messages",
                      onPressed: () {
                        if (Navigator.canPop(context)) {
                          Navigator.pop(context);
                        }
                      },
                      icon: const Icon(IconlyBold.message),
                    ),
                  ],
                ),
              ],
            ),
          ),
        )
      : AppBar(
          backgroundColor: Utils.kSecondaryColor,
          title: Center(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text("INSTAGRAM CLONE"),
                const SizedBox(
                  width: Utils.kLineHeight,
                ),
                IconButton(
                  color: Colors.white,
                  tooltip: "Post",
                  onPressed: () {
                    if (Navigator.canPop(context)) {
                      Navigator.pop(context);
                    }
                    //TODO: Link to add post page
                  },
                  icon: const Icon(IconlyBold.plus),
                ),
                IconButton(
                  color: Colors.white,
                  tooltip: "Messages",
                  onPressed: () {
                    if (Navigator.canPop(context)) {
                      Navigator.pop(context);
                    }
                    //TODO: Link to Message page
                  },
                  icon: const Icon(IconlyBold.message),
                ),
              ],
            ),
          ),
        );
}
