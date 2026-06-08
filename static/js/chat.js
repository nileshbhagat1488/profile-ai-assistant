const chatWindow = document.getElementById("chatWindow");
const userInput = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");

function appendMessage(role, text) {
  const msg = document.createElement("div");
  msg.className = `message ${role}`;
  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = text;
  msg.appendChild(bubble);
  chatWindow.appendChild(msg);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function showTyping() {
  const msg = document.createElement("div");
  msg.className = "message assistant typing";
  msg.id = "typingIndicator";
  msg.innerHTML = `<div class="bubble"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>`;
  chatWindow.appendChild(msg);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function removeTyping() {
  const el = document.getElementById("typingIndicator");
  if (el) el.remove();
}

async function sendMessage() {
  const text = userInput.value.trim();
  if (!text) return;

  userInput.value = "";
  sendBtn.disabled = true;
  appendMessage("user", text);
  showTyping();

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });
    const data = await res.json();
    removeTyping();
    if (data.error) {
      appendMessage("assistant", "Error: " + data.error);
    } else {
      appendMessage("assistant", data.answer);
    }
  } catch (err) {
    removeTyping();
    appendMessage("assistant", "Network error. Is Flask running?");
  }

  sendBtn.disabled = false;
  userInput.focus();
}

function fillInput(text) {
  userInput.value = text;
  userInput.focus();
}

userInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") sendMessage();
});
