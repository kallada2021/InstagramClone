import 'package:flutter/material.dart';

class Styles {
  static ThemeData themeData(bool isDarkTheme, BuildContext context) {
    return ThemeData(
      scaffoldBackgroundColor: isDarkTheme ? Colors.purple[900] : Colors.white,
      primaryColor: Colors.pink[600],
      colorScheme: ThemeData().colorScheme.copyWith(
            secondary: isDarkTheme ? Colors.deepPurple[900] : Colors.white70,
            brightness: isDarkTheme ? Brightness.dark : Brightness.light,
          ),
      cardColor: isDarkTheme ? Colors.purple[600] : Colors.blue[50],
      canvasColor: isDarkTheme ? Colors.black87 : Colors.white60,
      buttonTheme: Theme.of(context).buttonTheme.copyWith(
            colorScheme: isDarkTheme
                ? const ColorScheme.dark()
                : const ColorScheme.light(),
          ),
    );
  }
}
