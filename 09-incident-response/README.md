# Incident Response

## Overview

This section documents hands-on Incident Response investigations conducted within the SOC Detection Engineering, Threat Hunting, and Incident Response Lab.

The projects focus on identifying, investigating, analyzing, and responding to suspicious activity using Windows telemetry, Sysmon data, Splunk investigations, threat intelligence, and MITRE ATT&CK techniques.

The objective is to develop practical incident response skills aligned with real-world SOC and Incident Response workflows.

---

## Incident Response Lifecycle

```text
Alert Detected
      ↓
Triage
      ↓
Investigation
      ↓
Analysis
      ↓
Containment
      ↓
Eradication
      ↓
Recovery
      ↓
Lessons Learned
```

---

## Projects

### 01 – Windows Event Log Investigation

Investigation of Windows Security Event Logs including:

* Event ID 4624 (Successful Logon)
* Event ID 4625 (Failed Logon)
* Event ID 4688 (Process Creation)

Focus Areas:

* Authentication Analysis
* User Activity Investigation
* Log Correlation
* Timeline Creation

MITRE ATT&CK:

* T1110 – Brute Force
* T1550 – Use Alternate Authentication Material

---

### 02 – PowerShell Incident Investigation

Investigation of suspicious PowerShell activity.

Focus Areas:

* Encoded Commands
* Download Cradles
* Invoke-Expression (IEX)
* Fileless Malware Techniques

MITRE ATT&CK:

* T1059.001 – PowerShell
* T1027 – Obfuscated Files or Information

---

### 03 – Lateral Movement Investigation

Investigation of remote execution and lateral movement activity.

Focus Areas:

* WMI Activity
* PsExec Activity
* Remote Command Execution
* Host-to-Host Correlation

MITRE ATT&CK:

* T1021 – Remote Services
* T1047 – Windows Management Instrumentation

---

### 04 – Sysmon Process Investigation

Investigation of process execution telemetry collected through Sysmon.

Focus Areas:

* Event ID 1 (Process Creation)
* Event ID 3 (Network Connections)
* Event ID 13 (Registry Modifications)
* Parent-Child Process Analysis

MITRE ATT&CK:

* T1036 – Masquerading
* T1055 – Process Injection

---

### 05 – Incident Response Playbook

Development of a structured incident response workflow.

Focus Areas:

* Alert Triage
* Investigation Procedures
* Containment Actions
* Escalation Decisions
* Lessons Learned

MITRE ATT&CK:

* Multi-Technique Response Workflow

---

## Skills Demonstrated

* Incident Response
* Threat Hunting
* Log Analysis
* PowerShell Investigation
* Sysmon Analysis
* Windows Event Analysis
* Process Investigation
* Timeline Reconstruction
* MITRE ATT&CK Mapping
* SOC Operations

---

## Technologies Used

* Splunk Enterprise
* Sysmon
* Windows
* Kali Linux
* Sigma
* MISP
* MITRE ATT&CK
* BOTSv3 Dataset

---

## Key Learning Outcome

> Effective incident response is built upon visibility, investigation methodology, and evidence-based decision making.
