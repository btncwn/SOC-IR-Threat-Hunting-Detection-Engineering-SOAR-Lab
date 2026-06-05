# Incident Response

## Overview

This section documents hands-on Incident Response investigations performed within the lab environment.

Projects focus on identifying malicious activity, collecting evidence, validating attacker behavior, and mapping findings to the MITRE ATT&CK framework.

The investigations combine Windows Event Logs, Sysmon telemetry, PowerShell analysis, persistence detection, lateral movement validation, and incident response methodologies.

---

## Incident Response Workflow

```text
Alert or Suspicious Activity
            ↓
Evidence Collection
            ↓
Log Analysis
            ↓
Threat Identification
            ↓
Investigation & Validation
            ↓
Containment Strategy
            ↓
Incident Response Assessment
```

---

## Projects

### 01 – Lateral Movement Investigation

Investigation of remote activity between Windows and Kali Linux systems.

Focus Areas:

* Windows Event ID 4688 Analysis
* WMI Remote Execution
* SSH Activity Validation
* Reverse Tunnel Investigation
* MITRE ATT&CK Mapping

Key Techniques:

* T1021 – Remote Services
* T1047 – Windows Management Instrumentation
* T1572 – Protocol Tunneling

---

### 02 – Windows Persistence Investigation

Investigation of Registry Run Key persistence using Atomic Red Team and custom hunting automation.

Focus Areas:

* Registry Persistence Analysis
* Atomic Red Team Simulation
* PowerShell Event ID 4104 Analysis
* Python Persistence Hunting
* Registry Validation

Key Techniques:

* T1547.001 – Registry Run Keys / Startup Folder
* T1112 – Modify Registry

---

### 03 – Windows Event Log Investigation

Investigation of Windows Security and Operational logs to identify suspicious activity and validate security events.

Focus Areas:

* Security Event Analysis
* Event Correlation
* Log Validation
* Evidence Collection
* Investigation Workflow

---

### 04 – Sysmon Process Investigation

Investigation of process creation activity using Sysmon telemetry.

Focus Areas:

* Process Creation Analysis
* Parent-Child Relationships
* Command-Line Review
* Process Execution Validation
* Sysmon Event Analysis

---

### 05 – Incident Response Playbook

Standardized incident response workflow used throughout the lab.

Focus Areas:

* Detection
* Investigation
* Evidence Collection
* Containment
* Eradication
* Recovery
* Lessons Learned

---

## Skills Demonstrated

* Incident Response
* Security Monitoring
* Windows Event Log Analysis
* Sysmon Investigation
* PowerShell Analysis
* Persistence Detection
* Lateral Movement Investigation
* Evidence Collection
* MITRE ATT&CK Mapping
* Threat Hunting
* Security Operations

---

## Technologies Used

* Splunk Enterprise
* Sysmon
* Windows 7
* Windows 11
* Kali Linux
* Atomic Red Team
* PowerShell
* Python
* MITRE ATT&CK

---

## Key Lesson

> Effective incident response depends on accurate evidence collection, thorough investigation, and the ability to correlate activity across multiple data sources.

These projects demonstrate practical incident response workflows used to identify, investigate, and validate malicious activity within a controlled lab environment.
