// main.js
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("analyzeForm");
  const btn = document.getElementById("submitBtn");
  const load = document.getElementById("loading");
  const err = document.getElementById("errorAlert");
  const resCard = document.getElementById("resultCard");
  const themeBtn = document.getElementById("themeToggle");
  const exampleBtn = document.getElementById("exampleBtn");

  // Dark mode toggle (persist in localStorage)
  const setTheme = (t) => {
    document.body.classList.remove("light","dark");
    document.body.classList.add(t);
    themeBtn.textContent = (t==="dark") ? "☀️" : "🌙";
    localStorage.setItem("theme", t);
  };
  const saved = localStorage.getItem("theme") || "light";
  setTheme(saved);
  themeBtn.addEventListener("click", ()=> setTheme(document.body.classList.contains("dark") ? "light" : "dark"));

  // example JD loader
  exampleBtn.addEventListener("click", ()=> {
    document.getElementById("jd").value = "We are hiring a Software Engineer with 3+ years experience in Python, Flask, REST APIs, Docker, SQL, and machine learning understanding.";
  });

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    err.classList.add("d-none"); resCard.classList.add("d-none");
    btn.disabled = true; load.classList.remove("d-none");

    const fd = new FormData(form);
    try {
      const r = await fetch("/analyze", { method: "POST", body: fd });
      const j = await r.json();
      if (!j.success) throw new Error(j.error || "Unknown error");

      const out = j.result || {};
      // match score handling (try to get number)
      let score = out["JD Match"] ?? out["match_score"] ?? null;
      let pct = 0;
      if (score !== null) {
        if (typeof score === "string") {
          const m = score.match(/\\d+/);
          pct = m ? Number(m[0]) : 0;
        } else if (typeof score === "number") pct = Math.round(score);
      }
      pct = Math.max(0, Math.min(100, pct));
      document.getElementById("matchScoreBadge").innerHTML = `<span class="badge bg-info">${pct}%</span>`;
      document.getElementById("matchProgress").style.width = pct + "%";

      const missing = out["MissingKeywords"] || out["missing_keywords"] || [];
      document.getElementById("missingKeywords").textContent = (missing.length ? missing.join(", ") : "No critical keywords missing.");

      document.getElementById("profileSummary").innerHTML = out["Profile Summary"] || out["summary"] || "No summary available.";

      resCard.classList.remove("d-none");
    } catch (e2) {
      err.textContent = e2.message || "An error occurred"; err.classList.remove("d-none");
    } finally {
      btn.disabled = false; load.classList.add("d-none");
    }
  });
});
