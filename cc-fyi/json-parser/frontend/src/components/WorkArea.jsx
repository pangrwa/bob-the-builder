import CodeBox from "./CodeBox";

function WorkArea() {

    return (
        <div className="d-flex gap-5 align-center justify-content-center"> 
            <CodeBox />
            <button>Parse and Format</button>
            <CodeBox />
        </div>
    )
}

export default WorkArea;
