:root {
  --bg: #f2f5f8;
  --panel: #ffffff;
  --ink: #0e1b2b;
  --muted: #54657a;
  --line: #dfe8ee;
  --primary: #114a7a;
  --primary-soft: #eaf3ff;
  --conform: #1d8f5a;
  --nonconform: #b33d3d;
  --indeterminate: #c38b2c;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  background: linear-gradient(180deg, #eef4f8 0%, #edf2f7 100%);
  color: var(--ink);
  font-family: "Segoe UI", Tahoma, sans-serif;
}

.page-shell {
  max-width: 1200px;
  margin: 0 auto;
  padding: 32px 24px 48px;
}

.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 0 20px;
  border-bottom: 1px solid var(--line);
  margin-bottom: 24px;
}

.eyebrow {
  color: var(--muted);
  letter-spacing: 0.12em;
  font-size: 0.72rem;
  font-weight: 700;
}

h1 {
  margin: 6px 0 0;
  font-size: clamp(1.8rem, 3vw, 3rem);
}

.lang-badges {
  display: flex;
  gap: 8px;
}

.lang-badges span {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 38px;
  height: 28px;
  border-radius: 999px;
  background: var(--primary-soft);
  color: var(--primary);
  font-size: 0.72rem;
  font-weight: 700;
}

.grid {
  display: grid;
  grid-template-columns: 1.3fr 0.7fr;
  gap: 24px;
}

.panel {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 16px;
  box-shadow: 0 8px 30px rgba(10, 39, 62, 0.06);
  padding: 24px;
}

.panel h2 {
  margin-top: 0;
}

.form-panel form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.field-row {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.field-row.two-col {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}

label {
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--muted);
}

input {
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 12px 14px;
  background: #f9fbfd;
  font-size: 0.96rem;
  color: var(--ink);
}

input:focus {
  outline: 2px solid rgba(17, 74, 122, 0.18);
  border-color: var(--primary);
}

button {
  border: none;
  border-radius: 10px;
  background: linear-gradient(135deg, #114a7a, #1a5d95);
  color: white;
  padding: 14px 18px;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
}

button:hover {
  filter: brightness(1.04);
}

.result-card {
  border-radius: 16px;
  padding: 22px 18px;
  margin-bottom: 18px;
}

.result-card.neutral {
  background: #f6f8fa;
  border: 1px solid #e2e8ee;
}

.result-card.conforme {
  background: rgba(29, 143, 90, 0.08);
  border: 1px solid rgba(29, 143, 90, 0.25);
}

.result-card.non_conforme {
  background: rgba(179, 61, 61, 0.08);
  border: 1px solid rgba(179, 61, 61, 0.2);
}

.result-card.indetermine {
  background: rgba(195, 139, 44, 0.08);
  border: 1px solid rgba(195, 139, 44, 0.2);
}

.status-label {
  font-size: 0.72rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
}

.status-value {
  margin-top: 6px;
  font-size: clamp(1.8rem, 3vw, 2.6rem);
  font-weight: 800;
}

#reasonText {
  margin: 12px 0 0;
  line-height: 1.5;
  color: var(--ink);
}

.meta-block {
  margin-top: 8px;
}

.meta-block h3 {
  margin-bottom: 10px;
}

.meta-block ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 8px;
  color: var(--muted);
}

.demo-panel {
  margin-top: 24px;
}

.demo-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
  margin-top: 16px;
}

.demo-card {
  background: #f8fafc;
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 16px;
}

.demo-name {
  font-weight: 700;
  margin-bottom: 10px;
}

.demo-metadata {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  font-size: 0.72rem;
  color: var(--muted);
}

.demo-range {
  margin-top: 12px;
  color: var(--ink);
  font-weight: 600;
}

@media (max-width: 860px) {
  .grid {
    grid-template-columns: 1fr;
  }

  .topbar {
    align-items: flex-start;
    flex-direction: column;
    gap: 12px;
  }
}
