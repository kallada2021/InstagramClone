import 'package:flutter/material.dart';
import 'package:flutter_iconly/flutter_iconly.dart';

import '../constants/utils.dart';

class Footer extends StatelessWidget {
  const Footer({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    Size size = Utils(context).screenSize;
    return Container(
      width: double.infinity,
      height: 100.0,
      color: Utils.kSecondaryColor,
      child: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Center(
            child: TextButton(
              onPressed: () {
                if (Navigator.canPop(context)) {
                  Navigator.canPop(context);
                }
                // TODO: Add route
              },
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Row(
                      children: const [
                        Text(
                          "My Profile",
                          style: Utils.kFooterTextStyle,
                        ),
                        SizedBox(
                          width: 10,
                        ),
                        Icon(
                          IconlyBold.profile,
                          color: Colors.white60,
                          size: 30,
                        ),
                      ],
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: TextButton(
                      onPressed: () {
                        if (Navigator.canPop(context)) {
                          Navigator.canPop(context);
                        }
                      },
                      child: Row(
                        children: const [
                          Text(
                            "Latest Posts",
                            style: Utils.kFooterTextStyle,
                          ),
                          SizedBox(
                            width: 10,
                          ),
                          Icon(
                            IconlyBold.chat,
                            color: Colors.white60,
                            size: 30,
                          ),
                        ],
                      ),
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: TextButton(
                      onPressed: () {
                        if (Navigator.canPop(context)) {
                          Navigator.canPop(context);
                        }
                      },
                      child: Row(
                        children: const [
                          Text(
                            "Login",
                            style: Utils.kFooterTextStyle,
                          ),
                          SizedBox(
                            width: 10,
                          ),
                          Icon(
                            IconlyBold.login,
                            color: Colors.white60,
                            size: 30,
                          ),
                        ],
                      ),
                    ),
                  ),
                  size.width > 900
                      ? Padding(
                          padding: const EdgeInsets.all(8.0),
                          child: TextButton(
                            onPressed: () {
                              if (Navigator.canPop(context)) {
                                Navigator.canPop(context);
                              }
                              // TODO: Link to user profile
                            },
                            child: Row(
                              children: const [
                                Text(
                                  "My Profile",
                                  style: Utils.kFooterTextStyle,
                                ),
                                SizedBox(
                                  width: 10,
                                ),
                                Icon(
                                  IconlyBold.profile,
                                  color: Colors.white60,
                                  size: 30,
                                ),
                              ],
                            ),
                          ),
                        )
                      : Container(),
                ],
              ),
            ),
          )
        ],
      ),
    );
  }
}
