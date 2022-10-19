import 'package:flutter/material.dart';

class CustomTextField extends StatelessWidget {
  final String hintText;
  final TextEditingController controller;
  final TextInputType inputType;
  final bool isPassword;
  const CustomTextField({
    Key? key,
    required this.controller,
    required this.hintText,
    required this.inputType,
    this.isPassword = false,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      controller: controller,
      decoration: InputDecoration(
        contentPadding: EdgeInsets.symmetric(
          horizontal: 20,
        ),
        hintText: hintText,
        label: Text(hintText),
        border: const OutlineInputBorder(
          borderSide: BorderSide(
            color: Colors.black45,
          ),
        ),
        enabledBorder: const OutlineInputBorder(
          borderSide: BorderSide(
            color: Colors.black87,
          ),
        ),
      ),
      keyboardType: inputType,
      obscureText: isPassword,
      validator: (val) {
        if (val == null || val.isEmpty) {
          return "Please enter your $hintText";
        }
        return null;
      },
    );
  }
}
