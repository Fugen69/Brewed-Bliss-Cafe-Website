const btn10 = document.getElementById("btn-10") as HTMLButtonElement;
const btn15 = document.getElementById("btn-15") as HTMLButtonElement;
const btn20 = document.getElementById("btn-20") as HTMLButtonElement;
const customInput = document.getElementById("custom-tip") as HTMLInputElement;

let currentTip = 0;

function sendValue(val: number) {
  currentTip = val;
  window.parent.postMessage({
    isStreamlitMessage: true,
    type: "streamlit:setComponentValue",
    value: val,
  }, "*");
}

function updateSelection(selectedBtn: HTMLButtonElement | null) {
  [btn10, btn15, btn20].forEach(btn => {
    btn.style.background = "#16213E";
    btn.style.color = "#E8D5B7";
  });
  if (selectedBtn) {
    selectedBtn.style.background = "#C8A27A";
    selectedBtn.style.color = "#1A1A2E";
  }
}

btn10.addEventListener("click", () => {
  updateSelection(btn10);
  customInput.value = "";
  sendValue(10);
});

btn15.addEventListener("click", () => {
  updateSelection(btn15);
  customInput.value = "";
  sendValue(15);
});

btn20.addEventListener("click", () => {
  updateSelection(btn20);
  customInput.value = "";
  sendValue(20);
});

customInput.addEventListener("input", (e) => {
  updateSelection(null);
  const val = parseFloat((e.target as HTMLInputElement).value) || 0;
  sendValue(val);
});

window.addEventListener("message", (event) => {
  if (event.data.type === "streamlit:render") {
    window.parent.postMessage({
      isStreamlitMessage: true,
      type: "streamlit:setFrameHeight",
      height: document.body.scrollHeight,
    }, "*");
  }
});

// Tell Streamlit we are ready
window.parent.postMessage({
  isStreamlitMessage: true,
  type: "streamlit:componentReady",
  apiVersion: 1,
}, "*");
