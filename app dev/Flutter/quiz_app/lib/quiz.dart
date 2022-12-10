import 'package:flutter/material.dart';
import './question.dart';
import './answer.dart';

class Quiz extends StatelessWidget {
  final List _questions;
  final int _qno;
  final Function changeQ;

  Quiz(this._questions, this._qno, this.changeQ);

  @override
  Widget build(BuildContext context) {
    return Column(children: [
      Questions(
        _questions[_qno]['questionText'].toString(),
      ),
      ...(_questions[_qno]['answers'] as List<Map<String, Object>>).map((ans) {
        return Answer(() => changeQ(ans["Score"]), ans['Text'] as String);
      }).toList(),
    ]);
  }
}
