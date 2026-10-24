const { useState } = React;

function App() {
  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      content: 'FastOne here—ready to race through your questions with a sharp, first-person answer.'
    }
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
      const response = await fetch('http://127.0.0.1:8000/chat', {
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

  const bubbles = messages.map((msg, index) =>
    React.createElement(
      'div',
      { key: index, className: `bubble ${msg.role}` },
      React.createElement('div', { className: 'bubble-tag' }, msg.role === 'user' ? 'You' : 'FastOne'),
      React.createElement('p', null, msg.content)
    )
  );

  return React.createElement(
    'div',
    { className: 'fastone-shell' },
    React.createElement('div', { className: 'hero-blur top-left' }),
    React.createElement('div', { className: 'hero-blur bottom-right' }),
    React.createElement(
      'div',
      { className: 'grid-board' },
      React.createElement(
        'section',
        { className: 'hero-panel' },
        React.createElement('div', { className: 'hero-tag' }, 'RACING AI CO-PILOT'),
        React.createElement('h1', null, 'FastOne'),
        React.createElement('p', { className: 'hero-copy' }, 'I’m your first-person F1 bot, built by Sachin to keep the pace sharp and the answers quick.'),
        React.createElement(
          'div',
          { className: 'hero-metrics' },
          React.createElement(
            'div',
            null,
            React.createElement('span', null, 'DRIVER:'),
            React.createElement('strong', null, 'Sachin')
          ),
          React.createElement(
            'div',
            null,
            React.createElement('span', null, 'CAR:'),
            React.createElement('strong', null, 'FastOne')
          ),
          React.createElement(
            'div',
            null,
            React.createElement('span', null, 'MODE:'),
            React.createElement('strong', null, 'Qualifying')
          )
        )
      ),
      React.createElement(
        'section',
        { className: 'chat-panel' },
        React.createElement(
          'div',
          { className: 'panel-header' },
          React.createElement('div', { className: 'panel-title' }, 'Pit Stop Chat'),
          React.createElement('div', { className: 'panel-badge' }, 'FastOne Live')
        ),
        React.createElement('div', { className: 'messages' }, bubbles),
        React.createElement(
          'form',
          { onSubmit: sendMessage, className: 'composer' },
          React.createElement('input', {
            value: input,
            onChange: (e) => setInput(e.target.value),
            placeholder: 'Type a question for FastOne',
            disabled: loading
          }),
          React.createElement('button', { type: 'submit', disabled: loading }, loading ? 'Racing...' : 'Send')
        )
      )
    )
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(
  React.createElement(React.StrictMode, null, React.createElement(App))
);
