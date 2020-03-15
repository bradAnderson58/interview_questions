# Interview Questions
Some interview questions to ask. These questions are designed to be used as in-person Pair Programming exercises. Ideally, the candidate will be able to reach a solution in a reasonable amount of time, and discuss time complexity trade-offs in their solution.
Each question comes with a stubbed out implementation file, and a test file which exercises the stubbed function/method. I would consider it a positive if a candidate thought of a new corner case and wrote additional tests for it, but in general, the candidate should focus on fixing the implementation so that the tests pass, rather than changing the tests.
Currently, we have questions in Python, Java, and JavaScript - although not all questions are represented in each language. (consider this a TODO)

### Python
Note: Python questions use static type checking and must therefore be run using 3.6+
Tests can be run using the command `python -m unittest test_<name_of_question>.py` from the folder containing the question

### JavaScript
Note: JavaScript tests rely on mocha and therefore you must run `npm install` to download dependencies before running the tests
Tests can be run using the command `npm run test` from the folder containing the question.

### Java
Note: Java code is currently a pain to run from the command line. (TODO)
I included the .iml and .idea files so user should be able to just import it into IntelliJ and then run the tests from there

#### TODO:

We should refactor the directory structure to be by language first, then by question. Will make things easier since probably (besides JavaScript) user would probably only be interested in using questions for one language.