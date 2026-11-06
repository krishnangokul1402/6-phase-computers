# 6 Phase Computers — GitHub Pages + Streamlit App

Modern, bright and responsive technology-company portfolio for **6 Phase Computers** in **Kilpauk, Chennai**. Uses the original business logo supplied by the owner, custom product/service graphics and the provided Google Maps location.

## ✨ Features

- Interactive products and service descriptions for computers, laptops, printers, CCTV, Wi-Fi, software, components and accessories.
- Bright graphics, animated backgrounds, scroll effects, filters, FAQs, mobile navigation, and a store location map.
- **GitHub Pages**: full HTML/CSS/JavaScript site hosted at a normal URL.
- **Streamlit**: same visual design embedded via `st.iframe` with `height="content"`, using a self-contained HTML asset bundle.
- **Demo-only enquiry generator**: validates the enquiry and prepares a **copyable draft**, but **does not send, save or collect messages**. A real customer enquiry service requires a verified official business email / WhatsApp number and a secure backend.

## 🚀 Part 1 — Upload project to GitHub

1. Download and extract the project ZIP. The extracted folder contains `index.html`, `streamlit_app.py`, `requirements.txt`, `streamlit_site.html`, and the `static` folder.
2. Sign in at **https://github.com/**. Select **New repository** and call it `6-phase-computers` (or a name of your choice). Public works with free GitHub Pages.
3. Select **Add file → Upload files** on the repository (or use the GitHub Desktop app).
4. Upload the **contents inside** the extracted folder to the **repository root**, so `index.html` and `streamlit_app.py` are at top level. Upload `static` and `.streamlit` folders too. Commit changes to `main`.
5. Confirm the repository shows `index.html` and `streamlit_app.py` directly, *not* inside an extra `6-phase-computers-github-streamlit/` subfolder.

For a reliable way to include hidden files and folder structures, use Git command line:

```bash
cd 6-phase-computers-github-streamlit
git init
git add .
git commit -m "Initial 6 Phase Computers website"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/6-phase-computers.git
git push -u origin main
```

Create the empty repository on GitHub **before** running these commands. Replace `YOUR_USERNAME` with your own GitHub username. GitHub authentication may be required; use GitHub's supported sign-in methods instead of entering a password into the terminal.

## 🌐 Part 2 — Publish GitHub Pages website (optional)

1. Open your repository → **Settings → Pages**.
2. Under *Build and deployment*, choose **Deploy from a branch**.
3. Select branch `main`, folder `/ (root)`, then **Save**.
4. GitHub will display your published link, usually:
   `https://YOUR_USERNAME.github.io/6-phase-computers/`.
5. The `index.html` uses relative `static/` asset URLs, so it works under your GitHub project path.

GitHub Pages is **static hosting**. It does **not** run Python or save customer enquiries.

## ☁️ Part 3 — Publish Streamlit Community Cloud app

1. Open **https://share.streamlit.io/** and sign in (link GitHub if prompted).
2. Choose **Create app → Yup, I have an app** (the exact UI may change).
3. Repository: `YOUR_USERNAME/6-phase-computers`.
4. Branch: `main`.
5. Main file path: **`streamlit_app.py`**.
6. Optionally choose your app subdomain (example: `six-phase-computers`).
7. Click **Deploy**. Streamlit reads `requirements.txt` and installs version 1.60.0.
8. Share the URL Streamlit gives you (example format `https://six-phase-computers.streamlit.app/`). Your actual URL is assigned by Streamlit.

### Local Streamlit test in PyCharm

```bash
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

Or right-click `streamlit_app.py` in PyCharm and run it with those command line parameters.

## 📂 Project structure

```text
6-phase-computers-github-streamlit/
├── index.html                 # GitHub Pages homepage
├── streamlit_app.py           # Streamlit Cloud entrypoint
├── streamlit_site.html        # All-in-one page embedded by Streamlit
├── requirements.txt           # Streamlit dependency
├── static/
│   ├── css/style.css
│   ├── js/main.js
│   └── images/                 # Original company logo + custom illustrations
├── .streamlit/config.toml     # Streamlit theme
├── tools/build_streamlit_site.py
├── .gitignore
├── .nojekyll
└── README.md
```

## 🔁 Updating your website

Edit text in `index.html`, colors in `static/css/style.css`, functionality in `static/js/main.js`, or replace the existing logo in `static/images/6-phase-original-logo.jpg`. After making changes, rebuild the Streamlit version:

```bash
python tools/build_streamlit_site.py
```

Then commit and push changes to GitHub. Both deployments update based on your repo settings.

## ⚠️ Before using this as a live customer contact website

- Supply and verify company **email**, **WhatsApp or phone number**, opening hours, and actual street address before publishing them.
- Integrate a verified email / CRM backend and spam prevention; don't collect personal details using a demo form.
- Don't commit private API keys, customer data, credentials or `.streamlit/secrets.toml` to GitHub.
- Avoid relying on Streamlit Community Cloud local files for permanent storage: app instances are not persistent databases.

**Google Maps:** https://maps.app.goo.gl/8j6JtUzoUuzYGTiq6

---
*6 Phase Computers — Your Hardware, Solutions Simplified.*
