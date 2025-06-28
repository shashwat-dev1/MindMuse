function formatMarkdown(text) {
  // Convert markdown-like formatting to HTML
  return text
    .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
    .replace(/\n- /g, "<li>")
    .replace(/\n\d+\. /g, "<br><strong>$&</strong>") // Optional: number highlighting
    .replace(/\n/g, "<br>");
}

function runAction(action) {
  const topic = document.getElementById("topicInput").value;
  const output = document.getElementById("output");
  const loader = document.getElementById("loader");
  output.innerHTML = "";
  loader.style.display = "flex";

  fetch("/process", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ action, topic })
  })
    .then(res => res.json())
    .then(data => {
      loader.style.display = "none";
      const formatted = formatMarkdown(data.result);
      output.innerHTML = formatted;
    })
    .catch(err => {
      loader.style.display = "none";
      output.innerHTML = "<span style='color:red'>Error: Something went wrong. Please try again.</span>";
    });
}
