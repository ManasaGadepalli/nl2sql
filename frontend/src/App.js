import React, {useState} from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState(null);

  const ask = async () => {
    const res = await fetch (`http://127.0.0.1:8000/ask?question=${encodeURIComponent(question)}`);
    const data = await res.json(); 
    setResponse(data);
  }; 

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>NL2SQL</h1>
      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask a question"
        style={{ marginRight: "0.5rem" }}
      />
      <button onClick={ask}>Ask</button>
      {response && (
        <pre style={{ marginTop: "1rem" }}>
          {JSON.stringify(response, null, 2)}
        </pre>
      )}
    </div>
  );
}
export default App;
