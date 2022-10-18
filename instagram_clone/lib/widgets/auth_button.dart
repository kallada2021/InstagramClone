import 'package:flutter/material.dart';
import 'package:instagram_clone/widgets/textwidget.dart';

class AuthButton extends StatelessWidget {
  final Function func;
  final String buttonText;
  final Color primaryColor;
  const AuthButton({
    Key? key,
    required this.func,
    required this.buttonText,
    this.primaryColor = Colors.white30,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Center(
      child: SizedBox(
        width: 300,
        height: 50,
        child: ElevatedButton(
          style: ElevatedButton.styleFrom(
            primary: primaryColor,
          ),
          onPressed: () {
            func();
          },
          child: TextWidget(
            textSize: 18,
            text: buttonText,
            color: Colors.white,
          ),
        ),
      ),
    );
  }
}
