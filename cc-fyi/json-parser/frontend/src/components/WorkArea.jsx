import { useState } from "react";
import CodeBox from "./CodeBox";

const api_url = import.meta.env.VITE_API_URL;

function WorkArea() {
    const [rawValue, setRawValue] = useState("{\n  \"Hello\": \"World\"\n}");   
    const [formattedValue, setFormattedValue] = useState("{\n  \"Hello\": \"World\"\n}");
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    async function handleParse() {
        setIsLoading(true);
        setError(null);
        try {
            const response = await fetch(`${api_url}/parse`, {
                method: "POST",
                headers: {
                    "Content-Type": "text/plain"
                },
                body: rawValue
            })

            console.log(response);
            if (!response.ok) {
                const error = await response.json(); 
                setError("Error: " + "Look on the right code box for more details"); 
                setFormattedValue(error.detail);
            }
            
            const result = await response.json();
            setFormattedValue(result);
        } catch (error) {
            console.error("Error:")
        } finally {
            setIsLoading(false);
        }
    }

    return (
        <div className="d-flex justify-content-center">
            <div className="d-flex gap-5 align-center justify-content-center"> 
                <CodeBox value={rawValue} setValue={setRawValue}/>
                <div className="d-flex flex-column align-center  max-width-1">
                    <button
                        onClick={handleParse}
                        className="btn btn-primary"
                        disabled={isLoading}
                    >Parse and Format</button>
                    {error&&<div className="text-danger">{error}</div>}
                </div>
                <CodeBox value={formattedValue} setValue={setFormattedValue}/>
            </div>
        </div>
    )
}

export default WorkArea;
