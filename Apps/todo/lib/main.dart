import 'package:flutter/material.dart';

void main() {
  runApp(const Home());
}

class Home extends StatelessWidget {
  const Home({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'TODO',
      home: Scaffold(
          appBar: AppBar(
            title: const Text(
              "TODO",
              style: TextStyle(
                color: Colors.white,
                fontSize: 30,
                fontWeight: FontWeight.bold,
              ),
            ),
            centerTitle: true,
            backgroundColor: Colors.green,
          ),
          body: const Center(
            child: Text("Hello World!"),
          )),
    );
  }
}
