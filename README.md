# 🏭 Smart QC Inspection & Traceability Dashboard

**An industry-level Quality Control automation system built with Python and Streamlit**

> Internship Project | Uno Minda Group | Quality Control Division  
> Built by: [Your Name] | Technology: Python · Streamlit · SQLite · Plotly

---

## 📋 Project Overview

This project replaces paper-based quality inspection records in automotive manufacturing with a 
digital dashboard that provides real-time defect tracking, SPC analysis, and full batch traceability.

**Problem Solved:** Manual paper-based QC records → delayed defect detection, no trend analysis, 
no searchable audit trail.

**Solution:** Digital inspection entry + automated PASS/FAIL logic + live analytics dashboard + 
SPC control charts + batch traceability search.

---

## 🎯 Key Features

| Feature | Description |
|---|---|
| 📋 Inspection Form | Digital entry form with auto PASS/FAIL logic |
| 📊 Analytics Dashboard | KPIs, Pareto charts, shift/machine analysis |
| 📉 SPC Charts | X-bar & R control charts with Cp calculation |
| 🔍 Traceability | Search by Batch ID, Machine, or Operator |
| 📄 Reports | Export to Excel (.xlsx) and CSV |

---

## 🚀 Quick Start (Setup in 5 Minutes)

### Step 1: Clone / Download the project
```bash
git clone https://github.com/yourusername/smart-qc-dashboard.git
cd smart-qc-dashboard
```

### Step 2: Create a virtual environment (recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the application
```bash
streamlit run app.py
```

### Step 5: Load sample data (for demo)
Click **"🎲 Load Sample Data"** in the sidebar to populate 300 synthetic inspection records.

The app will open at: **http://localhost:8501**

---

## 📁 Project Structure

```
smart_qc_dashboard/
├── app.py                          ← Main entry point (run this)
├── requirements.txt                ← Python dependencies
├── README.md                       ← This file
│
├── database/
│   ├── db_setup.py                 ← SQLite database creation & seeding
│   └── qc_data.db                  ← Auto-generated database file
│
├── modules/
│   ├── inspection_form.py          ← Inspection entry form
│   ├── dashboard.py                ← Analytics & charts
│   ├── spc_charts.py               ← X-bar & R control charts
│   ├── traceability.py             ← Batch search & history
│   └── reports.py                  ← Export to Excel/CSV
│
├── data/
│   └── generate_sample_data.py     ← Sample data generator
│
└── utils/
    ├── constants.py                ← Machine IDs, shifts, config
    └── helpers.py                  ← Shared utility functions
```

---

## 🏭 SPC Concepts Used

This project implements **Statistical Process Control** per **AIAG SPC Manual (2nd Edition)**:

- **X-bar Chart**: Monitors process mean — detects shifts
- **R Chart**: Monitors process variability — detects spread changes  
- **Control Limits**: Calculated as X̄ ± A₂R̄ (using AIAG A2, D3, D4 constants)
- **Process Capability (Cp)**: Cp = (USL-LSL)/(6σ) — automotive requirement: Cp ≥ 1.33
- **Pareto Analysis**: 80/20 rule — focus improvement on top defect sources

---

## 📊 Dashboard Screenshots

*(Add screenshots after running the app)*

---

## 🔧 Technology Stack

| Technology | Purpose | Version |
|---|---|---|
| Python | Core language | 3.9+ |
| Streamlit | Web dashboard framework | 1.28+ |
| Pandas | Data manipulation | 2.0+ |
| SQLite | Local database | Built-in |
| Plotly | Interactive charts | 5.15+ |
| NumPy | SPC calculations | 1.24+ |
| OpenPyXL | Excel export | 3.1+ |

---

## 📈 Future Enhancements (Phase 2+)

- [ ] Login authentication (operator-level access control)
- [ ] QR code scanning for batch ID entry
- [ ] Email alerts for out-of-control SPC signals
- [ ] Power BI integration via exported data
- [ ] Mobile-responsive design for shop floor tablets
- [ ] Integration with ERP (SAP) via API

---

## 📖 Standards & References

- **IATF 16949**: Automotive Quality Management System standard
- **AIAG SPC Manual**: Statistical Process Control reference
- **APQP**: Advanced Product Quality Planning methodology
- **8D Problem Solving**: Corrective action framework for defects

---

## 👤 Author

**[Your Name]**  
Intern, Quality Control Division  
Uno Minda Group | [Your Location]  

---

*Built during internship at Uno Minda Group as part of a QC process digitalization initiative.*
