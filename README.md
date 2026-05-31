---
title: SpotIt
emoji: 📍
colorFrom: purple
colorTo: indigo
sdk: streamlit
sdk_version: "1.45.0"
app_file: app.py
pinned: false
---
# 📍 SpotIt

## See It. Spot It. Report It.

---

## 📌 Project Overview

**SpotIt** is a Streamlit-based civic issue reporting application where users can report local problems, upload image evidence, track report status, view dashboard analytics, and see report locations on a map.

The project is designed to make issue reporting simple, organized, and easy to track. Users can submit reports through a user-friendly interface and later track their reports using a unique report ID.

---

## 🎯 Project Goal

The main goal of **SpotIt** is to provide a simple digital platform for reporting and tracking local civic issues.

SpotIt helps users to:

- Report local problems
- Upload image evidence
- Track report status
- View dashboard analytics
- See report locations on a map

---

## 🏷️ Tagline

> **See It. Spot It. Report It.**

Live demo - https://spot-itwebsite.streamlit.app/
---

## 📌 Problem Statement

Many local issues are noticed by people, but they are not always reported or tracked properly.

Users may face problems such as:

- No simple platform to report local issues
- No proper tracking system after submitting a report
- No clear view of report locations
- Limited visibility of report status and analytics

Because of this, local problems may remain unorganized and difficult to monitor.

---

## 💡 Proposed Solution

**SpotIt** solves this problem by providing a simple civic issue reporting system.

The application allows users to:

- Submit issue reports
- Upload image evidence
- Generate a unique report ID
- Track report status
- View analytics on a dashboard
- View report locations on a map

This makes the reporting process simple, clear, and user-friendly.

---

## ✨ Key Features

### 📝 Report Issue

Users can report a local problem by entering the issue category, location, and description.

### 📸 Upload Image Evidence

Users can upload an image as supporting evidence for the report.

### 🆔 Report ID Generation

After submitting a report, the system generates a unique report ID.

### 🔎 Track Report Status

Users can track their submitted report using the generated report ID.

### 📊 Dashboard Analytics

The dashboard displays useful insights such as report count, category-wise reports, report status, and recent reports.

### 🗺️ Map View

Users can view report locations on a map and understand where issues are reported.

### 🗃️ Database Storage

Submitted reports are stored using SQLite for saving and retrieving report details.

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | Python |
| Database | SQLite |
| Data Processing | Pandas |
| Map View | Streamlit Map |
| Image Handling | Python File Handling |
| Version Control | Git |
| Collaboration | GitLab |

---

## 📁 Project Structure

```text
spot-it/
│
├── app.py
├── database.py
├── image_utils.py
├── requirements.txt
├── README.md
├── Contribution.md
├── agents.md
├── user_manual.md
├── test_image.py
│
├── pages/
│   ├── dashboard.py
│   ├── report_issue.py
│   ├── track_issue.py
│   └── map_view.py
│
└── .gitignore
```

---

## 📄 Module Overview

### 🏠 Home Page

Introduces the SpotIt application and helps users navigate through the project.

### 📝 Report Issue Page

Allows users to submit reports by entering issue details and uploading image evidence.

### 🔎 Track Issue Page

Allows users to track the current status of a submitted report using a report ID.

### 📊 Dashboard Page

Displays report analytics, report summary, status details, and recent reports.

### 🗺️ Map View Page

Displays report locations on a map and helps users understand location-based report data.

### 🗃️ Database Module

Handles storing and retrieving report information using SQLite.

### 🖼️ Image Utility Module

Handles image upload, image validation, and image storage.

---

## 🚀 How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://code.swecha.org/venkat_k10/spot-it.git
```

### 2. Open the Project Folder

```bash
cd spot-it
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

### 5. Open in Browser

After running the command, Streamlit will open the application in your browser.

---

## 👥 Team Members & Contributions

| Team Member | Role | Contribution |
|---|---|---|
| Jyotsna | Frontend & UI | Built the user interface, home page, report issue page, and tracking page |
| Mansi | Database & Backend | Added SQLite database, report saving, report retrieval, and backend functions |
| Pooja | Image Upload & File Handling | Implemented image upload, file validation, and image storage features |
| Yogesh | Dashboard & Analytics | Developed dashboard metrics, analytics, report summaries, and insights |
| Venkat Sai | Maps & Final Integration | Added map view, location-based report display, final integration, and project coordination |

---

## 📊 Dashboard Analytics

The dashboard helps users understand report data through:

- Total submitted reports
- Reports by category
- Reports by status
- Recent report activity
- Report insights

---

## 🗺️ Map View

The map view helps users see report locations visually.

It includes:

- Report location display
- Status-based filtering
- Category-based filtering
- Location-wise report details

---

## 🔮 Future Enhancements

Future improvements can include:

- Real-time location detection
- Admin panel
- Report verification system
- Email or SMS status updates
- Advanced dashboard filters
- Improved map visualization
- Cloud deployment

---

## 🚀 Expected Outcome

SpotIt helps users report, track, and understand local civic issues using one simple platform.

It improves:

- Report organization
- User accessibility
- Report tracking
- Location visibility
- Community awareness

---

## 🏆 Built For

### CivicTech Hackathon 2026

---

## ❤️ Final Note
"SpotIt transforms civic issue reporting by enabling users to instantly report problems, upload evidence, and monitor issue status in real time."

> **See It. Spot It. Report It.**