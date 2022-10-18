import 'package:flutter/material.dart';

import '../services/theme_preferences.dart';

class ThemeProvider with ChangeNotifier {
  bool _darkTheme = false;
  bool get getDarkTheme => _darkTheme;
  DarkThemePrefs themePrefs = DarkThemePrefs();

  set setDarkTheme(bool value) {
    _darkTheme = value;
    themePrefs.setDarkTheme(value);
    notifyListeners();
  }
}
