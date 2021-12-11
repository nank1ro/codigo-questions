A simple CLI app written in Dart that composes the exercise code for you.

> Use only for exercises of type 1

This is pretty useful to try if a code works before submitting a new question.

Before starting you need to install Dart in your local machine, following [this official guide](https://dart.dev/get-dart#install).

After you've installed Dart, you also need to clone the codigo-question project.

1. (Preferred for beginners) If you have the Github Desktop app installed, you can simply go to the [main page](https://github.com/nank1ro/codigo-questions) of the codigo questions, clicking on the _Code_ dropdown button, and clicking `Open with Github Desktop`.
2. If you don't have Github Desktop, assuming that you have `git` installed, you can simply run in your clones folder:
```sh
git clone https://github.com/nank1ro/codigo-questions.git
```

After you've cloned the project, cd into it to continue, eg:
```
cd codigo-questions
```

## Usage

To run the CLI use the following command:
```sh
dart run cli/src/cli.dart -p $PATH
```

where `$PATH` is the exercise path, e.g:
```
dart run cli/src/cli.dart -p ./en/python/variables/1.md
```

given that you run this command from the root of the `codigo-questions` folder.

To test your code, you can simply go to https://ide.judge0.com/, select the programming language and run to check the output.
For a list of supported programming languages, refer to the [CONTRIBUTING](../CONTRIBUTING.md#Q&A) file
