import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text("Expenses management"),
        ),
        body: Column(
          children: [
            Container(
              width: double.infinity,
              child: Card(
                color: Colors.amber.shade100,
                child: Text('mayank'),
              ),
            ),
            Card(
              child: Text('nacho'),
            )
          ],
        ),
      ),
    );
  }
}
