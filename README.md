# 🛡️ Security Monitoring Agent – Log Compression & Anomaly Detection

## Project Overview
This project implements a **Cybersecurity Security Monitoring Agent** that compresses large-scale system logs and applies **machine learning–based anomaly detection** to identify suspicious activities efficiently.

The goal is to **reduce log processing cost**, **improve detection speed**, and **highlight unusual security events**, similar to real-world Security Operations Center (SOC) workflows.

---

##  Key Objectives
- Compress high-volume security logs to reduce storage and processing cost
- Detect anomalous (unusual) security behavior using machine learning
- Identify time-based attack patterns (e.g., late-night suspicious activity)
- Provide human-readable anomaly reports for analysts

---

##  How It Works (Simple Explanation)

### 1️⃣ Log Compression
- Raw logs are grouped by:
  - User
  - Event type
  - IP address
- Repeated events are **compressed into a single record with a count**
- This simulates large-scale log reduction used in SIEM systems

###  Feature Encoding
- Text fields (user, event, IP) are converted into numerical form using label encoding
- This allows machine learning models to process categorical data

###  Anomaly Detection (Machine Learning)
- **Isolation Forest** is used to detect anomalies
- The model flags **rare or unusual patterns**, not confirmed attacks
- Examples of anomalies:
  - Repeated login failures
  - Rare security events (password change, file delete)
  - Activity during unusual hours (night-time)

###  Time-Based Analysis
- Anomalies are grouped by hour of the day
- Helps identify suspicious time windows (e.g., late-night attacks)

---

##  Tech Stack
- **Python**
- **Pandas**
- **Scikit-learn**
- **Matplotlib**
- **CSV-based log simulation**


---

##  Why This Project Is Valuable
- Simulates real SOC log processing
- Demonstrates **ML + cybersecurity concepts**
- Shows understanding of **false positives & analyst review**


---

##  Future Improvements
- Integrate real SIEM log formats
- Add alert severity scoring
- Automate response actions
- Deploy as a real-time monitoring service

---

##  Author
**Harshini Perumal**  
GenAI & Cybersecurity Trainee  

