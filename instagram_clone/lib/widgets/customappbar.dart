import 'package:flutter/material.dart';
import 'package:flutter_iconly/flutter_iconly.dart';

import '../constants/utils.dart';

AppBar customAppBar(BuildContext context) {
  Size size = Utils(context).screenSize;
  return size.width > 1050
      ? AppBar(
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
                      "MAGNOLIA IT SOLUTIONS",
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
          title: Center(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text("Instagram Clone"),
                const SizedBox(
                  width: Utils.kLineHeight,
                ),
                IconButton(
                  color: Colors.white,
                  tooltip: "Messsages",
                  onPressed: () {
                    if (Navigator.canPop(context)) {
                      Navigator.pop(context);
                    }
                  },
                  icon: const Icon(IconlyBold.message),
                ),
              ],
            ),
          ),
        );
}
