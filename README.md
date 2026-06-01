# SOC Detection Engineering, Threat Hunting & DFIR Lab

## Overview

This repository documents a complete blue-team security lab designed to simulate a realistic attack lifecycle and demonstrate the workflow of a SOC Analyst, Threat Hunter, Detection Engineer, and Incident Responder.

The environment combines vulnerability assessment, attack simulation, endpoint telemetry collection, SIEM monitoring, threat hunting, threat intelligence enrichment, digital forensics, and MITRE ATT&CK mapping.

The goal is to generate real security telemetry, detect adversary activity, investigate incidents, and document findings using industry-standard security tools.



Key Lab Achievement

A credentialed Nessus assessment identified a critical MS17-010 (EternalBlue) vulnerability on a Windows 7 endpoint. The exposed SMB attack surface was validated through SMB enumeration, monitored using Sysmon telemetry, and analyzed through a custom Splunk SOC dashboard.





---

# Lab Environment

```text
Attacker Infrastructure
───────────────────────
Kali Linux

Target Environment
───────────────────────
Windows 7 Endpoint
(Sysmon)

Security Stack
───────────────────────
Splunk Enterprise
Splunk Universal Forwarder
Nessus
MISP
Velociraptor
```

---

# Attack Flow

```text
1. Vulnerability Assessment
           ↓
2. Attack Simulation
           ↓
3. Endpoint Telemetry Collection
           ↓
4. SIEM Ingestion
           ↓
5. Threat Hunting
           ↓
6. SOC Dashboard Monitoring
           ↓
7. Threat Intelligence Enrichment
           ↓
8. DFIR Investigation
           ↓
9. MITRE ATT&CK Mapping
           ↓
10. Incident Reporting
```

---

# Technologies Used

| Technology                 | Purpose                            |
| -------------------------- | ---------------------------------- |
| Splunk Enterprise          | SIEM, threat hunting, dashboarding |
| Sysmon                     | Endpoint telemetry                 |
| Splunk Universal Forwarder | Log collection and forwarding      |
| Kali Linux                 | Adversary simulation               |
| Nessus                     | Vulnerability assessment           |
| MISP                       | Threat intelligence platform       |
| Velociraptor               | DFIR and endpoint investigation    |
| MITRE ATT&CK               | Adversary behavior mapping         |

---

# Repository Structure

```text
SOC-Detection-Engineering-Threat-Hunting-Lab/

├── 01-lab-architecture
│
├── 02-vulnerability-assessment
│   ├── nessus-scans
│   ├── vulnerability-analysis
│   └── remediation-recommendations
│
├── 03-attack-simulation
│   ├── smb-enumeration
│   ├── network-reconnaissance
│   ├── powershell-execution
│   ├── remote-execution-simulation
│   └── attack-scenarios
│
├── 04-endpoint-telemetry
│   ├── sysmon-installation
│   ├── sysmon-configuration
│   └── event-analysis
│
├── 05-splunk-ingestion
│   ├── universal-forwarder
│   ├── inputs-conf
│   ├── index-configuration
│   └── data-validation
│
├── 06-threat-hunting
│   ├── process-analysis
│   ├── powershell-hunting
│   ├── parent-child-analysis
│   ├── suspicious-activity
│   └── spl-searches
│
├── 07-soc-dashboard
│   ├── attack-timeline
│   ├── kpis
│   ├── visualizations
│   └── dashboard-screenshots
│
├── 08-threat-intelligence
│   ├── misp
│   ├── ioc-enrichment
│   └── threat-context
│
├── 09-dfir
│   ├── velociraptor
│   ├── triage
│   ├── artifact-collection
│   └── investigations
│
├── 10-mitre-attack-mapping
│   ├── tactics
│   ├── techniques
│   └── detections
│
├── 11-incident-report
│   ├── executive-summary
│   ├── timeline
│   ├── findings
│   └── lessons-learned
│
├── screenshots
└── reports
```

---

# Phase 1 – Vulnerability Assessment

Nessus is used to identify weaknesses within the Windows endpoint.

Assessment activities include:

* Missing security patches
* Legacy operating system exposure
* SMB misconfigurations
* Unsupported software
* Security hardening recommendations

Deliverables:

* Nessus scan reports
* Vulnerability prioritization
* Remediation recommendations

---

# Phase 2 – Attack Simulation

Attack activity is generated from Kali Linux to create realistic security telemetry.

Examples include:

### Discovery

* Host discovery
* Service enumeration
* SMB reconnaissance

### Execution

* Command shell execution
* PowerShell activity
* Process creation events

### Lateral Movement Simulation

* SMB authentication attempts
* Remote execution patterns
* PsExec-style behavioral simulations

---

# Phase 3 – Endpoint Telemetry

Sysmon provides detailed endpoint visibility including:

* Process creation
* Process termination
* File creation
* Network connections
* Parent-child relationships
* PowerShell execution

---

# Phase 4 – SIEM Ingestion

Splunk Enterprise receives and analyzes telemetry through Splunk Universal Forwarder.

Collected logs include:

* Sysmon Operational Logs
* Security Logs
* System Logs

---

# Phase 5 – Threat Hunting

Threat hunting scenarios include:

* Suspicious PowerShell execution
* Parent-child process anomalies
* Living-off-the-Land Binary activity
* Unexpected process relationships
* Behavioral investigations

---

# Phase 6 – SOC Dashboard

A custom Splunk SOC Dashboard was developed to visualize attack activity.

Features include:

* Total Sysmon Events
* Process Creation Monitoring
* Attack Timeline
* PowerShell Activity
* Top Executed Processes
* Parent → Child Process Relationships
* Suspicious Process Activity
* Event Volume Monitoring

---

# Phase 7 – Threat Intelligence

MISP is used to enrich investigations with threat intelligence.

Capabilities include:

* IOC management
* Threat enrichment
* ATT&CK alignment
* Investigation context

---

# Phase 8 – Digital Forensics & Incident Response

Velociraptor supports endpoint investigations through:

* Rapid triage
* Artifact collection
* Host analysis
* Incident response workflows

---

# Phase 9 – MITRE ATT&CK Mapping

Detections and attack simulations are mapped to MITRE ATT&CK techniques.

Examples:

| Tactic            | Technique                             |
| ----------------- | ------------------------------------- |
| Discovery         | T1046 Network Service Discovery       |
| Discovery         | T1087 Account Discovery               |
| Execution         | T1059 PowerShell                      |
| Execution         | T1059.003 Windows Command Shell       |
| Credential Access | T1003 Credential Dumping (Simulation) |
| Lateral Movement  | T1021 SMB                             |
| Lateral Movement  | T1569 Service Execution               |

---

# Skills Demonstrated

* SOC Operations
* Detection Engineering
* Threat Hunting
* Incident Response
* Digital Forensics
* Vulnerability Management
* Threat Intelligence
* MITRE ATT&CK Mapping
* SIEM Engineering
* Endpoint Monitoring
* Security Investigation

---

# Disclaimer

This repository was created for cybersecurity education, portfolio development, detection engineering practice, and defensive security research.

All testing was performed within authorized and isolated laboratory environments.
