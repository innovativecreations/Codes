import 'package:flutter/material.dart';

//////######### only shows text ////////////////////

// void main() {   //code starts here
//   runApp(
//     MaterialApp(
//       home: Center(  //center widget to center the items
//         child: Text("NAcho"),
//       ),
//     ),
//   );
// }

// ################# Action Bar start ############### //
void main() {
  //code starts here
  runApp(
    MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.blueGrey,
        appBar: AppBar(
          title: Center(
            child: Text('Hi! Aaradhya Bhash'),
          ),
          backgroundColor: Colors.blueGrey[900],
        ),
        body: Center(
          child: Image(
            image: NetworkImage("https://a-z-animals.com/media/animals/images/original/buffalo.jpg"),
          ),
        ),
      ),
    ),
  );
}
