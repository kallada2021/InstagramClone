import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../providers/theme_provider.dart';
import '../widgets/customappbar.dart';
import '../widgets/textwidget.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    final themeState = Provider.of<ThemeProvider>(context);
    Color color = themeState.getDarkTheme ? Colors.white : Colors.black;

    return Scaffold(
      appBar: customAppBar(context),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text("Home Page Feed Here"),
            const SizedBox(
              height: 15,
            ),
            SizedBox(
              width: 400,
              child: SwitchListTile(
                title: TextWidget(
                  text: "Theme",
                  color: color,
                  textSize: 22,
                ),
                secondary: Icon(
                  themeState.getDarkTheme
                      ? Icons.dark_mode_outlined
                      : Icons.light_mode_outlined,
                ),
                value: themeState.getDarkTheme,
                onChanged: (bool value) {
                  setState(() {
                    themeState.setDarkTheme = value;
                  });
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
