A simple CLI app written in Dart that composes the exercise code for you.

> Use only for exercises of type 1

This is pretty useful to try if a code works before submitting a new question.

To run use the following command:
```sh
dart run cli/src/cli.dart -p $PATH
```

where `$PATH` is the exercise path, e.g:
```
dart run cli/src/cli.dart -p ./en/python/variables/1.md
```

given that you run this command from the root of the `codigo-questions` folder.

To test your code, you can simply go to https://ide.judge0.com/, select the programming language and run to check the output.
