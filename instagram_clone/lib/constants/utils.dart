import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/theme_provider.dart';

class Utils {
  BuildContext context;
  Utils(this.context);

  bool get getTheme => Provider.of<ThemeProvider>(context).getDarkTheme;
  Color get color => getTheme ? Colors.white : Colors.black;
  Size get screenSize => MediaQuery.of(context).size;

  static const kLineHeight = 30.0;
  static const kLineWidth = 40.0;
  static TextStyle kAppBarTextStyle =
      const TextStyle(color: Colors.white, fontSize: 16);

  static TextStyle kTechNameStyle = TextStyle(
    fontSize: 40,
    fontWeight: FontWeight.w900,
    color: Colors.deepPurple[900],
    fontFamily: "Arial",
  );

  static const TextStyle kTechPageTitleStyle = TextStyle(
    fontSize: 50,
    fontStyle: FontStyle.normal,
    color: Colors.black87,
  );
  static const TextStyle kFooterTextStyle = TextStyle(
    fontSize: 20,
    fontStyle: FontStyle.normal,
    color: Colors.black,
  );

  static const String s3Url =
      "https://portfolio-website-magnolia-bucket.s3.amazonaws.com/Images/";
}
