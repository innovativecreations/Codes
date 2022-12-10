// ignore_for_file: deprecated_member_use, prefer_const_constructors, use_key_in_widget_constructors

import 'package:flutter/material.dart';
import 'package:quiz_app/quiz.dart';
import './result.dart';

// import './qna.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  State<MyApp> createState() => _MyApp();
}

class _MyApp extends State<MyApp> {
  var _qno = 0;
  var totalScore = 0;

  // ignore: prefer_final_fields
  var _questions = [
    {
      'questionText': 'What\'s your favourite colour?',
      'answers': [
        {"Text": 'Lal', "Score": 20},
        {"Text": 'Kala', "Score": 15},
        {"Text": 'Nila', "Score": 10},
        {"Text": 'Safed', "Score": 5}
      ]
    },
    {
      'questionText': 'What\'s your favourite animal?',
      'answers': [
        {"Text": 'Bhalu', "Score": 20},
        {"Text": 'Hathi', "Score": 15},
        {"Text": 'Bhash', "Score": 10},
        {"Text": 'Chuha', "Score": 5}
      ]
    },
  ];
  void reset() {
    setState(() {
      totalScore = 0;
      _qno = 0;
    });
  }

  void changeQ(int score) {
    totalScore += score;
    setState(() {
      if (_qno < _questions.length) {
        _qno++;
      }
      print(_qno);
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Center(child: Text('NAcho')),
        ),
        body: _qno < _questions.length
            ? Quiz(_questions, _qno, changeQ)
            : Result(totalScore, reset),
      ),
    );
  }
}
