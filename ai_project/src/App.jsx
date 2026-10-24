import { useState } from 'react';

const API_URL = 'http://127.0.0.1:8000/chat';

function App() {
  const [messages, setMessages] = useState([
    { role: 'assistant', content: 'FastOne here—ready to race through your questions with a sharp, first-person answer.' }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { role: 'user', content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input })
      });

      const data = await response.json();
      setMessages((prev) => [...prev, { role: 'assistant', content: data.reply }]);
    } catch (error) {
      setMessages((prev) => [...prev, { role: 'assistant', content: 'FastOne hit a pit stop. Please try again.' }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-shell">
      <div className="track-card">
        <header className="track-header">
          <div>
            <p className="eyebrow">Formula 1 AI Chat</p>
            <h1>FastOne</h1>
          </div>
          <div className="pill">Creator: Sachin</div>
        </header>

        <div className="messages">
          {messages.map((msg, index) => (
            <div key={index} className={`bubble ${msg.role}`}>
              <strong>{msg.role === 'user' ? 'You' : 'FastOne'}</strong>
              <p>{msg.content}</p>
            </div>
          ))}
          {loading && <div className="bubble assistant"><strong>FastOne</strong><p>On the grid...</p></div>}
        </div>

        <form onSubmit={sendMessage} className="composer">
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask FastOne something..."
          />
          <button type="submit" disabled={loading}>Send</button>
        </form>
      </div>
    </div>
  );
}

export default App;
