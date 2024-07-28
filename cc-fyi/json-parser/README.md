# JSON Parser

## Deterministic Finite Automata
![dfa_state-diagram](out/state-diagram/state-diagram.png)

## Notes
- To be able to parse JSON, we need to be able to read in data from somewhere, this includes from reading a file and from standard output. Both using a buffered reader. 
- We need someone to be able to parse the input, lets call this class `JSONParser` which contains a buffered reader
- A JSON object can be identifed with the curly brackets. Since there could be a recursive nature of JSON object 
- How do we know if the input is valid? Solving the issue of balancing parenthesis!
- How do we determine a key value pair? The use of a colon
- types: string
- Use simplified maxmimal munch algorithm to scan through input and create a list of tokens
- strings only support double quotes, once might get too complicated if i see another double quote
