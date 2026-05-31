# 🤖 SpotIt Agents Documentation

## 📍 Project Name

**SpotIt – Anonymous Civic Issue Reporting Platform**

> **See It. Spot It. Report It.**

---

## 🧠 Purpose of Agents

In SpotIt, **agents** represent the major human roles and software modules responsible for building and running the platform.

This agent-based structure helps the team work in a clean, organized, and professional way.

The agents make the project:

* 🧩 Modular
* 🤝 Easy to collaborate on
* 🛠️ Easy to develop
* 🧪 Easy to test
* 🚀 Easy to improve
* 📂 Easy to maintain

---

## 🏗️ System Overview

SpotIt allows citizens to anonymously report civic and public safety issues.

The system collects:

* 🏷️ Issue category
* 📝 Issue description
* 📸 Photo evidence
* 📍 Location
* 📌 Report status
* 🕒 Timestamp

The collected information is stored and displayed through dashboards and interactive maps to help communities identify local issue hotspots.

---

# 👥 Human Team Agents

## 1️⃣ Frontend/UI Agent

### 👤 Assigned To

**Jyotsna**

### 🎯 Responsibility

The Frontend/UI Agent is responsible for designing and building the user-facing interface of SpotIt.

### 🛠️ Main Tasks

* 🏠 Build the Home Page
* 📸 Build the Report Issue Page
* 🔍 Build the Issue Tracking Page
* 🧭 Create navigation structure
* 🎨 Improve page layout and design
* 📱 Ensure a user-friendly experience
* ✨ Make the interface clean and easy to understand

### 📂 Main Files

```text
app.py
pages/report_issue.py
pages/track_issue.py
```

### 📥 Inputs

* User actions
* Form data
* Uploaded image input
* Location input
* Issue category selection

### 📤 Output

A clean and simple Streamlit interface where citizens can report and track civic issues.

---

## 2️⃣ Database & Backend Agent

### 👤 Assigned To

**Mansi**

### 🎯 Responsibility

The Database & Backend Agent is responsible for managing data storage, retrieval, and report status handling.

### 🛠️ Main Tasks

* 🗄️ Create SQLite database
* 📋 Design reports table
* 🆔 Generate unique report IDs
* 💾 Store submitted issue reports
* 🔍 Retrieve report details
* 🔄 Manage report status updates
* 🧾 Support backend functions for dashboard and tracking

### 📂 Main Files

```text
database.py
```

### 📥 Inputs

* Report ID
* Issue category
* Description
* Location
* Image path
* Status
* Timestamp

### 📤 Output

A reliable backend system that stores, retrieves, and manages civic issue reports.

---

## 3️⃣ Image Handling Agent

### 👤 Assigned To

**Pooja**

### 🎯 Responsibility

The Image Handling Agent manages uploaded images and ensures they are stored properly.

### 🛠️ Main Tasks

* 📸 Accept uploaded images
* ✅ Validate image format
* 🗂️ Store images in the uploads folder
* 🆔 Generate unique file names
* 🔗 Link image paths with report records
* 🛡️ Handle invalid or missing image files

### 📂 Main Files

```text
image_utils.py
uploads/
```

### 📥 Inputs

* Uploaded image file
* File name
* File type

### 📤 Output

A safe and organized image storage system linked with civic reports.

---

## 4️⃣ Dashboard & Analytics Agent

### 👤 Assigned To

**Yogesh**

### 🎯 Responsibility

The Dashboard & Analytics Agent is responsible for displaying public insights and report statistics.

### 🛠️ Main Tasks

* 📊 Show total number of reports
* 🏷️ Show reports by category
* 📌 Show reports by status
* 🕒 Display recent reports
* 📈 Create charts and summary metrics
* 🔥 Highlight issue trends and hotspots
* 👥 Support community visibility

### 📂 Main Files

```text
pages/dashboard.py
```

### 📥 Inputs

* Stored report data
* Issue categories
* Report status
* Location details
* Timestamp data

### 📤 Output

A public dashboard that helps communities understand civic issue patterns and priorities.

---

## 5️⃣ Maps & Integration Agent

### 👤 Assigned To

**Venkat Sai**

### 🎯 Responsibility

The Maps & Integration Agent handles map visualization, location features, system integration, and deployment preparation.

### 🛠️ Main Tasks

* 🗺️ Create interactive maps
* 📍 Display issue markers
* 🧾 Add issue details in map popups
* 🔗 Connect map with report data
* 🧪 Test complete application flow
* 🚀 Support deployment
* 🧩 Integrate modules from all team members

### 📂 Main Files

```text
maps.py
```

### 📥 Inputs

* Location data
* Issue category
* Description
* Report status

### 📤 Output

An interactive map that visually displays reported civic issues and community hotspots.

---

# ⚙️ Software Functional Agents

## 1️⃣ Report Collection Agent

### 🎯 Purpose

Collects civic issue details from users through the report form.

### 📥 Inputs

* 🏷️ Issue category
* 📝 Description
* 📍 Location
* 📸 Image

### ⚙️ Process

* Receives user input
* Validates required fields
* Sends report data to backend
* Triggers image storage process

### 📤 Output

A structured civic issue report ready to be saved.

---

## 2️⃣ Image Storage Agent

### 🎯 Purpose

Handles image uploads and stores them securely.

### 📥 Inputs

* Uploaded image file

### ⚙️ Process

* Checks image format
* Generates unique filename
* Saves image in uploads folder
* Returns stored image path

### 📤 Output

A stored image file linked to a report.

---

## 3️⃣ Database Agent

### 🎯 Purpose

Stores and manages submitted civic reports.

### 📥 Inputs

* Report ID
* Issue details
* Image path
* Location
* Status
* Timestamp

### ⚙️ Process

* Saves reports in SQLite
* Retrieves reports when needed
* Updates report status
* Sends data to dashboard and map modules

### 📤 Output

Stored and retrievable civic issue records.

---

## 4️⃣ Tracking Agent

### 🎯 Purpose

Allows users to check the status of submitted reports.

### 📥 Inputs

* Report ID

### ⚙️ Process

* Searches database
* Finds matching report
* Displays issue details and status

### 📤 Output

Current status and details of the submitted report.

---

## 5️⃣ Dashboard Agent

### 🎯 Purpose

Displays community insights and report statistics.

### 📥 Inputs

* Stored report data

### ⚙️ Process

* Counts total reports
* Groups reports by category
* Groups reports by status
* Generates summary metrics
* Displays trends visually

### 📤 Output

Dashboard statistics and community insights.

---

## 6️⃣ Map Visualization Agent

### 🎯 Purpose

Displays reported civic issues on an interactive map.

### 📥 Inputs

* Location
* Issue category
* Description
* Status

### ⚙️ Process

* Creates map markers
* Adds popup information
* Displays issue locations
* Helps identify hotspots

### 📤 Output

Interactive map showing civic issue locations.

---

## 🔄 Agent Workflow

```text
Citizen
  ↓
Frontend/UI Agent
  ↓
Report Collection Agent
  ↓
Image Storage Agent
  ↓
Database Agent
  ↓
Dashboard Agent + Map Visualization Agent
  ↓
Community View
```

---

## 📂 File Responsibility Mapping

```text
spotit/
│
├── app.py                  # Main Streamlit application
├── database.py             # Database & Backend Agent
├── image_utils.py          # Image Handling Agent
├── maps.py                 # Maps & Integration Agent
│
├── pages/
│   ├── report_issue.py     # Report Collection Agent
│   ├── track_issue.py      # Tracking Agent
│   └── dashboard.py        # Dashboard & Analytics Agent
│
├── uploads/                # Uploaded issue images
├── requirements.txt        # Project dependencies
├── README.md               # Project overview
├── CONTRIBUTING.md         # Contribution guidelines
├── USER_MANUAL.md          # User guide
└── AGENTS.md               # Agent documentation
```

---

# 🧪 Testing Responsibilities

Each agent must test their own module before pushing code to the repository.

---

## 🎨 Frontend/UI Agent Testing

* ✅ Check Home Page loads properly
* ✅ Check Report Issue Page opens correctly
* ✅ Check Track Issue Page opens correctly
* ✅ Check navigation works
* ✅ Check UI is readable and clean

---

## 🗄️ Database Agent Testing

* ✅ Check reports are saved
* ✅ Check report IDs are generated
* ✅ Check reports can be retrieved
* ✅ Check status updates work
* ✅ Check database does not crash on empty data

---

## 📸 Image Handling Agent Testing

* ✅ Check image upload works
* ✅ Check supported image formats are accepted
* ✅ Check images are saved in uploads folder
* ✅ Check invalid files are handled properly
* ✅ Check image path is returned correctly

---

## 📊 Dashboard Agent Testing

* ✅ Check total reports count
* ✅ Check category-wise statistics
* ✅ Check status-wise statistics
* ✅ Check charts display correctly
* ✅ Check dashboard updates after new reports

---

## 🗺️ Maps Agent Testing

* ✅ Check map loads successfully
* ✅ Check issue markers appear
* ✅ Check marker popups show correct details
* ✅ Check location data displays properly
* ✅ Check map integrates with report data

---

# 🌿 Git Collaboration Workflow

Each team member should work on their own branch.

## Branch Examples

```bash
git checkout -b frontend-ui
git checkout -b database-backend
git checkout -b image-handling
git checkout -b dashboard-analytics
git checkout -b maps-integration
```

---

## Basic Git Commands

```bash
git pull origin main
git add .
git commit -m "Add meaningful commit message"
git push origin branch-name
```

After pushing, create a Merge Request in GitLab / code.swecha.org.

---

# 🚀 Future AI Agent Possibilities

SpotIt does not require AI training for the current Proof of Concept.

Future versions can include AI-powered agents for:

* 🤖 Automatic issue category prediction
* 🔁 Duplicate report detection
* ⭐ Priority scoring
* 🌐 Language translation
* 📝 Report summarization
* 🏛️ Department routing
* 🔥 Hotspot prediction
* 📊 Civic trend forecasting

---

# ✅ Conclusion

SpotIt uses a modular agent-based structure to divide work clearly between team members and software components.

This structure helps the team build faster, collaborate better, test modules easily, and present the project professionally.

---

## 💬 Final Statement

> **SpotIt turns anonymous citizen reports into meaningful civic insights through dashboards, maps, and community-driven reporting.**

---

## 🏆 Built For

**CivicTech Hackathon 2026**

### ❤️ Empowering Communities Through Civic Participation
