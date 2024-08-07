import { json } from "@codemirror/lang-json";
import { useCallback, useState } from "react";
import CodeMirror from '@uiw/react-codemirror';

function CodeBox() {
    const [value, setValue] = useState("{\n  \"Hello\": \"World\"\n}");   
    const onChange = useCallback((val, viewUpdate) => {
        //console.log('val:', val);
        setValue(val);
    }, []);
    return (
        <CodeMirror 
            value={value} height="200px" extensions={[json()]} onChange={onChange}
            width="750px"
        />
    )
}

export default CodeBox;
