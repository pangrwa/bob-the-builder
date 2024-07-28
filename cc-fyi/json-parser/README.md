# JSON Parser

## Deterministic Finite Automata
![dfa_state-diagram](out/state-diagram/state-diagram.png)

## Context Free Grammar
**Rules**
$$
\begin{align}
\text{object} &\rightarrow \text{LBRACE statements RBRACE} \\
\text{statements} &\rightarrow \epsilon \\
\text{statements} &\rightarrow \text{prevStatements endStatement}\\
\text{endStatement} &\rightarrow \text{STRING COLON value} \\
\text{prevStatements} &\rightarrow \epsilon \\
\text{prevStatements} &\rightarrow \text{prevStatements statement} \\
\text{statement} &\rightarrow \text{STRING COLON value COMMA} \\
\text{value} &\rightarrow \text{object | array | keywords | STRING | NUM} \\
\text{array} &\rightarrow \text{LSQUARE items RSQUARE} \\
\text{items} &\rightarrow \epsilon \\
\text{items} &\rightarrow \text{prevItems endItem} \\
\text{endItem} &\rightarrow \text{value} \\
\text{prevItems} &\rightarrow \epsilon \\
\text{prevItems} &\rightarrow \text{prevItems item} \\
\text{item} &\rightarrow \text{value COMMA} \\
\text{keywords} &\rightarrow \text{NULL | FALSE | TRUE} \\
\end{align}
$$
- These rules shouldn't support traililng comma
- There are a compule of rules that start with the same terminal on the RHS, resulting in ambiguous grammar hence top-down parsing is not an option here
- 
## Notes
- To be able to parse JSON, we need to be able to read in data from somewhere, this includes from reading a file and from standard output. Both using a buffered reader. 
- We need someone to be able to parse the input, lets call this class `JSONParser` which contains a buffered reader
- A JSON object can be identifed with the curly brackets. Since there could be a recursive nature of JSON object 
- How do we know if the input is valid? Solving the issue of balancing parenthesis!
- How do we determine a key value pair? The use of a colon
- types: string
- Use simplified maxmimal munch algorithm to scan through input and create a list of tokens
- strings only support double quotes, once might get too complicated if i see another double quote
