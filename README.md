# argparser


Problem Statement:


You need to design an ArgsParser class that will handle command-line arguments for a tool. The class should support the following features:

Argument Types: Support for various argument types such as str, int, float, and bool.
Defaults and Required Arguments: Some arguments should have default values, and some should be mandatory.
Help Messages: Each argument should have an optional description/help message.
Error Handling: If the user provides invalid arguments, the class should raise appropriate errors with helpful messages.
Flag Arguments: There should be support for flags (e.g., --verbose) that toggle certain behaviors.
Parsing Logic: When the parse() method is called, it should return a dictionary with the parsed arguments.
Please think about how you might structure this class, what methods you'd use, and how you'd implement the argument validation, help, and parsing functionalities. You've got 45 minutes to implement the class.
