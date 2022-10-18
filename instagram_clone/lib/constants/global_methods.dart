import 'package:flutter/material.dart';
import 'package:flutter_iconly/flutter_iconly.dart';

import '../widgets/textwidget.dart';

class GlobalMethods {
  static navigateTo(
      {required BuildContext context, required String routeName}) {
    Navigator.pushNamed(context, routeName);
  }

  static Future<void> warningDialog({
    required String title,
    required String subtitle,
    required Function func,
    required BuildContext context,
  }) async {
    await showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: Row(
            children: [
              const Padding(
                padding: EdgeInsets.all(10.0),
                child: Icon(
                  IconlyBold.danger,
                  color: Colors.red,
                ),
              ),
              Text(title),
            ],
          ),
          content: TextWidget(
            color: Colors.red,
            text: subtitle,
            textSize: 20,
          ),
          actions: [
            TextButton(
              onPressed: () {
                func();
                if (Navigator.canPop(context)) {
                  Navigator.pop(context);
                }
              },
              child: const Text(
                "OK",
                style: TextStyle(
                  color: Colors.teal,
                ),
              ),
            ),
            const SizedBox(
              width: 15.0,
            ),
            TextButton(
              onPressed: () {
                if (Navigator.canPop(context)) {
                  Navigator.pop(context);
                }
              },
              child: const Text(
                "Cancel",
                style: TextStyle(color: Colors.red),
              ),
            ),
          ],
        );
      },
    );
  }

  static Future<void> errorDialog({
    required String subtitle,
    required BuildContext context,
  }) async {
    await showDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            title: Row(
              children: const [
                Padding(
                  padding: EdgeInsets.all(10.0),
                  child: Icon(
                    IconlyBold.danger,
                    color: Colors.red,
                  ),
                ),
                Text("An error occurred"),
              ],
            ),
            content: TextWidget(
              color: Colors.red,
              text: subtitle,
              textSize: 20,
            ),
            actions: [
              const SizedBox(
                width: 15.0,
              ),
              TextButton(
                onPressed: () {
                  if (Navigator.canPop(context)) {
                    Navigator.pop(context);
                  }
                },
                child: const Text(
                  "OK",
                  style: TextStyle(color: Colors.cyan),
                ),
              ),
            ],
          );
        });
  }
}
