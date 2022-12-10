// ignore_for_file: deprecated_member_use

import 'dart:ffi';

import 'package:flutter/material.dart';

class Answer extends StatelessWidget {
  final VoidCallback handler;
  String btnName;
  Answer(this.handler, this.btnName);
  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      // ignore: prefer_const_constructors
      child: RaisedButton(
        onPressed: handler,
        color: Colors.blue,
        child: Text(
          btnName,
          // ignore: unnecessary_const
          style: const TextStyle(
            color: Colors.white,
          ),
        ),
      ),
    );
  }
}
