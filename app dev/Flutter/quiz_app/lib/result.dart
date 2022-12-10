import 'package:flutter/material.dart';

class Result extends StatelessWidget {
  final int totalScore;
  final VoidCallback reset;

  Result(this.totalScore, this.reset);

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        children: [
          Container(
            margin: EdgeInsets.only(top: 200),
            child: Text(
              ("Your Score: $totalScore").toString(),
              style: const TextStyle(
                  fontSize: 30,
                  fontWeight: FontWeight.bold,
                  color: Color.fromARGB(255, 62, 62, 62)),
            ),
          ),
          const Text(
            'Nacho, karlia',
            style: TextStyle(fontSize: 20),
          ),
          ElevatedButton(
            onPressed: reset,
            child: Text("Restart the Quiz"),
          )
        ],
      ),
    );
  }
}
