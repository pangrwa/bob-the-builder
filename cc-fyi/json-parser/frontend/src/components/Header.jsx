
import { FaGithub } from "react-icons/fa";

function Header() {
    return (
        <div className="d-flex flex-column align-items-center justify-content-center"> 
            <h1>JSON-Parser</h1>
            <div>
                <span className="text-primary">Find out more over here: </span><a target="_blank" href="https://pangrwa.github.io/bob-the-builder/cc-fyi/json-parser/"><FaGithub /></a>
            </div>
            <h3>Working on some features currently...</h3>
            <ul>
                <li>Trailing commas maybe possible, have to edit my CFG rules, working on that</li>
                <li>Negative and decimal numbers may not yet be supported, working on the DFA</li>
                <li>Formatting can be improved such as empty objet and empty array, shouldn't have a new line</li>
                <li>Error detection can be improved</li>
            </ul>
        </div>
    )
}

export default Header
