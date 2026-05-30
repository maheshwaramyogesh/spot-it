# 🤝 Contributing to Spot-it

Thank you for contributing to **Spot-it**! 🚀

SpotIt is a CivicTech project that helps citizens anonymously report civic and public safety issues, making communities safer and more responsive.

---

## 👥 Team Workflow

Each team member is responsible for a specific module:

| Member   | Responsibility               |
| -------- | ---------------------------- |
| Jyotsna | Frontend & UI                |
| Mansi | Database & Backend           |
| Pooja | Image Upload & File Handling |
| Yogesh | Dashboard & Analytics        |
| Venkat Sai | Maps & Integration           |

---

## 🌿 Branching Strategy

Do **not** work directly on the main branch.

Create a feature branch:

```bash
git checkout -b feature-name
```

Examples:

```bash
git checkout -b frontend
git checkout -b database
git checkout -b dashboard
git checkout -b maps
```

---

## 📥 Getting the Latest Changes

Before starting work:

```bash
git pull origin main
```

---

## 💻 Making Changes

After completing your task:

```bash
git add .
git commit -m "Add meaningful commit message"
```

Example:

```bash
git commit -m "Add complaint submission form"
```

---

## 📤 Pushing Changes

Push your branch:

```bash
git push origin branch-name
```

Example:

```bash
git push origin frontend
```

Then create a Merge Request on GitLab.

---

## ✅ Code Guidelines

* Write clean and readable code.
* Use meaningful variable names.
* Add comments where necessary.
* Avoid duplicate code.
* Test features before pushing.

---

## 📂 Project Structure

```text
spotit/
│
├── app.py
├── database.py
├── image_utils.py
├── maps.py
│
├── pages/
│   ├── home.py
│   ├── report_issue.py
│   ├── track_issue.py
│   └── dashboard.py
│
├── uploads/
├── assets/
├── requirements.txt
├── README.md
└── CONTRIBUTING.md
```

---

## 🧪 Testing Checklist

Before submitting changes:

* [ ] Application runs successfully
* [ ] No errors in terminal
* [ ] Database operations work correctly
* [ ] Images upload properly
* [ ] Maps load successfully
* [ ] Dashboard displays correct information

---

## 🎯 Project Goal

Our goal is to build a platform that empowers citizens to:

* 📍 Report civic issues
* 📸 Share evidence through photos
* 🗺️ Visualize community issues
* 📊 Identify problem hotspots
* 🤝 Encourage civic participation

---

## ❤️ Thank You

Every contribution helps improve SpotIt and makes communities safer and more connected.

Happy Coding! 🚀