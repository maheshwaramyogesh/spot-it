# 📘 SpotIt User Manual

## 📍 SpotIt – See It. Spot It. Report It.

> **An anonymous civic reporting platform that helps citizens report local civic and public safety issues without revealing their identity.**

---

## 🌟 About SpotIt

**SpotIt** is a CivicTech web platform designed to make civic issue reporting simple, anonymous, and community-driven.

Citizens often notice issues around them, but many problems remain unreported because the reporting process is complicated, time-consuming, or requires personal identity details.

SpotIt allows citizens to report civic and public safety issues such as:

* 🛣️ Damaged roads
* 💡 Broken streetlights
* 🗑️ Illegal garbage dumping
* 🕳️ Open manholes
* 💧 Water leakage
* ⚠️ Unsafe public spaces
* 🚧 Other civic hazards

The platform helps communities identify local issue hotspots using reports, photos, locations, dashboards, and interactive maps.

---

## 🎯 Purpose of the Application

The purpose of SpotIt is to reduce the underreporting of civic issues by giving citizens a simple and anonymous way to raise public concerns.

SpotIt aims to:

* 🔒 Protect citizen privacy through anonymous reporting
* 🚀 Make civic issue reporting fast and simple
* 📸 Collect photo evidence for better clarity
* 📍 Capture issue locations for better visibility
* 📊 Display issue trends through public dashboards
* 🗺️ Identify civic hotspots using map-based visualization
* 🤝 Encourage community participation without barriers

---

## 👥 Target Users

SpotIt is designed for:

* 👨‍👩‍👧 Citizens
* 🎓 Students
* 🏘️ Local communities
* 🤝 Civic volunteers
* 🏛️ Municipal authorities
* 🚨 Public safety observers
* 🌍 CivicTech organizations

---

## 🛠️ Technologies Used

| Layer                 | Technology               |
| --------------------- | ------------------------ |
| 🎨 Frontend           | Streamlit                |
| 🧠 Backend            | Python                   |
| 🗄️ Database          | SQLite                   |
| 📊 Data Processing    | Pandas                   |
| 🗺️ Maps              | Folium + OpenStreetMap   |
| 🔁 Version Control    | Git                      |
| ☁️ Repository Hosting | GitLab / code.swecha.org |

---

## 🚀 How to Run SpotIt Locally

### 1️⃣ Clone the Repository

```bash
git clone <your-repository-link>
cd spotit
```

---

### 2️⃣ Create a Virtual Environment

```bash
python3 -m venv .venv
```

---

### 3️⃣ Activate the Virtual Environment

#### For Linux / Fedora

```bash
source .venv/bin/activate
```

#### For Windows

```bash
.venv\Scripts\activate
```

---

### 4️⃣ Install Required Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

After running the command, SpotIt will open in the browser.

---

## 🏠 Home Page

The Home Page introduces users to SpotIt and explains the purpose of the platform.

Users can understand:

* 📌 What SpotIt is
* 🔒 Why anonymous reporting matters
* 🧾 What issues can be reported
* 🌍 How SpotIt helps communities
* 🗺️ How dashboards and maps improve civic visibility

---

## 📸 Report an Issue

The **Report Issue** page allows citizens to submit a civic issue anonymously.

### Required Details

Users need to provide:

* 🏷️ Issue category
* 📝 Short description
* 📍 Location
* 📸 Image proof

---

## 🏷️ Supported Issue Categories

SpotIt supports the following issue types:

* 🛣️ Damaged Road
* 💡 Broken Streetlight
* 🗑️ Illegal Dumping
* 🕳️ Open Manhole
* 💧 Water Leakage
* ⚠️ Unsafe Area
* 📌 Other

---

## 📝 Steps to Report an Issue

1. Open the **Report Issue** page.
2. Select the issue category.
3. Add a short description of the problem.
4. Upload an image as proof.
5. Enter or mark the location.
6. Click **Submit Report**.

After submission, the report is stored in the system and can be viewed through the dashboard or map.

---

## 🔍 Track an Issue

The **Track Issue** page allows users to check the current status of a submitted report.

### Steps to Track

1. Open the **Track Issue** page.
2. Enter the report ID.
3. Click **Search**.
4. View the issue details and status.

---

## 📌 Possible Report Status Values

| Status          | Meaning                      |
| --------------- | ---------------------------- |
| 🟡 Reported     | The issue has been submitted |
| 🔵 Under Review | The issue is being checked   |
| 🟠 In Progress  | Action is being taken        |
| 🟢 Resolved     | The issue has been solved    |

---

## 📊 Public Dashboard

The dashboard provides community-level insights from submitted reports.

It can display:

* 📌 Total number of reports
* 🏷️ Reports by category
* 📈 Reports by status
* 🕒 Recently submitted reports
* 🔥 Most reported issue types
* 🌍 Area-wise civic concerns

The dashboard improves transparency and helps communities understand which problems need attention.

---

## 🗺️ Interactive Map

The map view helps users visually understand where civic issues are reported.

Users can:

* 📍 View issue markers
* 🔎 Identify local problem hotspots
* 🧾 See issue details through map popups
* 🌆 Understand affected areas
* 📊 Support data-driven civic awareness

---

## 👍 Community Validation

SpotIt can support community validation by allowing users to support or highlight existing reports.

This helps avoid duplicate reports and makes urgent issues more visible.

Community validation helps identify:

* 🚨 High-priority issues
* 🔁 Repeated civic problems
* 📍 Frequently affected locations
* 👥 Issues impacting many people

---

## 🔐 Privacy and Anonymity

SpotIt does not require users to create an account.

Users are not required to provide:

* ❌ Name
* ❌ Phone number
* ❌ Email address
* ❌ Personal identity details

This encourages more citizens to report issues without fear, hesitation, or privacy concerns.

---

## ⚠️ Current PoC Limitations

This Proof of Concept focuses on demonstrating the core workflow of anonymous civic reporting.

Current limitations include:

* 🚫 No real government department integration
* 🚫 No official complaint forwarding
* 🚫 No advanced user authentication
* 🚫 Manual category selection
* 🚫 Basic location input
* 🚫 Limited analytics in the initial version

---

## 🔮 Future Enhancements

Future versions of SpotIt can include:

* 🤖 AI-assisted issue categorization
* 🔁 Duplicate report detection
* 🏛️ Department-wise automatic routing
* 🌐 Telugu and Hindi language support
* 👍 Community upvotes
* 🔥 Live civic issue heatmaps
* 📩 SMS or email status updates
* 🧑‍💼 Official authority dashboard
* 📊 Advanced analytics for civic planning
* 📍 Automatic location detection

---

## ✅ Expected Impact

SpotIt aims to:

* 🚀 Increase civic participation
* 🔒 Encourage anonymous reporting
* 📍 Improve visibility of local issues
* 🗺️ Help identify civic hotspots
* 🤝 Support community-driven problem solving
* 🏙️ Contribute to safer and better-maintained public spaces

---

## 💬 Project Motto

> **See It. Spot It. Report It.**

---

## 🏆 Built For

**CivicTech Hackathon 2026**

### ❤️ Empowering Communities Through Civic Participation
