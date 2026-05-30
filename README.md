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