import { json } from "@codemirror/lang-json";
import { useCallback } from "react";
import CodeMirror from '@uiw/react-codemirror';

function CodeBox({ value, setValue }) {
    const onChange = useCallback((val, viewUpdate) => {
        console.log('val:', val);
        setValue(val);
    }, []);
    return (
        <CodeMirror 
            value={value} height="850px" extensions={[json()]} onChange={onChange}
            width="550px"
        />
    )
}

export default CodeBox;
