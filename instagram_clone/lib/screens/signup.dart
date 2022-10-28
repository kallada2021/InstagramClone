import 'package:flutter/material.dart';
import 'package:instagram_clone/constants/utils.dart';
import 'package:instagram_clone/widgets/auth_button.dart';
import 'package:instagram_clone/widgets/customappbar.dart';
import 'package:instagram_clone/widgets/textfield.dart';

class SignupScreen extends StatefulWidget {
  const SignupScreen({Key? key}) : super(key: key);

  @override
  State<SignupScreen> createState() => _SignupScreenState();
}

class _SignupScreenState extends State<SignupScreen> {
  // TODO: add firstname, lastname, and email address controller
  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  @override
  void dispose() {
    super.dispose();
    _usernameController.dispose();
    _passwordController.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: customAppBar(context),
      body: SizedBox(
        width: double.infinity,
        child: Padding(
          padding: const EdgeInsets.all(15.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              CustomTextField(
                controller: _usernameController,
                hintText: "Username",
                inputType: TextInputType.text,
              ),
              const SizedBox(
                height: 20,
              ),
              CustomTextField(
                controller: _passwordController,
                hintText: "Username",
                inputType: TextInputType.text,
                isPassword: true,
              ),
              const SizedBox(
                height: 20,
              ),
              AuthButton(
                func: () {
                  //TODO: implement signup
                  print("Signup");
                },
                buttonText: "Signup",
              ),
              const SizedBox(
                height: 20,
              ),
              TextButton(
                onPressed: () {},
                child: Text(
                  "Already have an account?",
                  style: Utils.kMediumFontTextStyle,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
