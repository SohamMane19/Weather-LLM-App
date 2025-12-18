import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!message.trim()) return;

    setLoading(true);
    setResponse("");

    try {
      const res = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message }),
      });

      const data = await res.json();
      setResponse(data.response);
    } catch (err) {
      setResponse("Error connecting to backend.");
    }

    setLoading(false);
  };

  return (
    <div style={styles.container}>
      <h2>🌦️ Weather Assistant</h2>

      <input
        type="text"
        placeholder="Ask about weather..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        style={styles.input}
      />

      <button onClick={sendMessage} style={styles.button}>
        Send
      </button>

      {loading && <p>Loading...</p>}

      {response && (
        <div style={styles.responseBox}>
          <b>Response:</b>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}

const styles = {
  container: {
    padding: "40px",
    fontFamily: "Arial",
    maxWidth: "500px",
    margin: "auto",
  },
  input: {
    width: "100%",
    padding: "10px",
    marginBottom: "10px",
    fontSize: "16px",
  },
  button: {
    padding: "10px 20px",
    fontSize: "16px",
    cursor: "pointer",
  },
  responseBox: {
    marginTop: "20px",
    backgroundColor: "#f4f4f4",
    padding: "15px",
    borderRadius: "5px",
  },
};

export default App;
