# SOC Detection Engineering, Threat Hunting & DFIR Lab

## Overview

This repository documents an end-to-end Security Operations Center (SOC) lab built to simulate a realistic cyber attack lifecycle and demonstrate blue-team security operations.

The project combines vulnerability management, attack simulation, endpoint telemetry collection, SIEM engineering, threat hunting, MITRE ATT&CK mapping, threat intelligence, and digital forensics to provide practical experience across multiple cybersecurity disciplines.

The lab was developed using real telemetry collected from a Windows 7 environment and analyzed through Splunk Enterprise.

---

## Key Achievement

Designed and built a complete SOC Detection Engineering, Threat Hunting, Threat Intelligence, and DFIR lab from the ground up using Splunk Enterprise, Sysmon, Nessus Essentials, MISP, Sigma, and the BOTSv3 dataset.

During the project, multiple technical challenges were encountered and resolved. Initial attempts to forward Windows event logs from a Windows 11 UTM virtual machine to a Splunk Enterprise instance running on macOS were unsuccessful, requiring redesign of the lab architecture. To overcome compatibility and telemetry collection issues, the environment was rebuilt using a dedicated Windows 7 endpoint and a Kali Linux attacker system.

Successfully deployed and configured Sysmon and Splunk Universal Forwarder on legacy Windows infrastructure, generated endpoint telemetry, and validated successful ingestion into Splunk Enterprise for security monitoring and threat hunting activities.

Conducted vulnerability assessments using Nessus Essentials, identified a critical MS17-010 (EternalBlue) exposure, validated the findings through SMB enumeration activities, and analyzed resulting telemetry through Splunk-based investigations.

Developed structured threat hunting investigations covering malicious domains, malicious IP addresses, malware hashes, suspicious PowerShell activity, and attacker behavior analysis. Enhanced investigations through MISP integration, IOC enrichment, and threat intelligence-driven hunting workflows.

Mapped observed adversary activity to the MITRE ATT&CK framework, performed DFIR analysis, documented incident response findings, and developed Sigma-based detections that were validated against real telemetry within the lab environment.

The project demonstrates the ability to design, build, troubleshoot, and operate an end-to-end SOC environment while integrating vulnerability management, telemetry engineering, threat hunting, threat intelligence, detection engineering, DFIR, and security operations workflows.


---

## Lab Environment


### Attacker Infrastructure

* Kali Linux
* Attack Simulation & Adversary Emulation

### Endpoint Infrastructure

* Windows 7
* Sysmon Telemetry Collection
* Splunk Universal Forwarder

### Security Monitoring & Detection Stack

* Splunk Enterprise
* Sysmon
* Sigma Detection Rules
* Splunk Universal Forwarder

### Vulnerability Management

* Nessus Essentials
* Vulnerability Assessment & Remediation Workflows

### Threat Intelligence Platform

* MISP
* IOC Management & Threat Intelligence Enrichment

### Security Automation (SOAR)

* Shuffle SOAR
* Automated Investigation & Response Workflows

### DFIR & Investigation

* Incident Response Playbooks
* Endpoint Investigation Workflows
* Digital Forensics & Evidence Analysis

### Detection Engineering

* Sigma Rule Development
* Splunk Detection Development
* MITRE ATT&CK Mapping
* Detection Validation & Tuning

---


## Technologies Used

| Technology                 | Purpose                            |
| -------------------------- | ---------------------------------- |
| Splunk Enterprise          | SIEM, Threat Hunting, Dashboarding |
| Sysmon                     | Endpoint Telemetry                 |
| Splunk Universal Forwarder | Log Collection & Forwarding        |
| Kali Linux                 | Attack Simulation                  |
| Nessus Essentials          | Vulnerability Assessment           |
| MITRE ATT&CK               | Adversary Behavior Mapping         |
| MISP                       | Threat Intelligence      |
| Velociraptor               | DFIR Investigations (Planned)      |

---

## Repository Structure

```text
SOC-Detection-Engineering-Threat-Hunting-DFIR-Lab
01-lab-architecture
02-vulnerability-assessment
03-attack-simulation
04-endpoint-telemetry
05-splunk-ingestion
06-threat-hunting
07-mitre-attack-mapping
08-threat-intelligence
09-dfir
10-soc-investigations
11-detection-engineering-sigma
12-soar-automation
```

---

## Project Highlights

### Vulnerability Assessment

* Credentialed Nessus Scan
* 550 Findings Identified
* 52 Critical Vulnerabilities
* 326 High Vulnerabilities
* MS17-010 (EternalBlue) Detection

### Attack Simulation

* SMB Enumeration
* Service Discovery
* Exposure Validation
* Attack Surface Analysis

### Endpoint Telemetry

* Sysmon Deployment
* Process Monitoring
* PowerShell Monitoring
* Parent-Child Process Analysis

### SIEM Engineering

* Splunk Enterprise Deployment
* Splunk Universal Forwarder Configuration
* Sysmon Log Ingestion
* XML Event Parsing & Field Extraction

### Threat Hunting

* Process Analysis
* PowerShell Hunting
* Command-Line Investigation
* Behavioral Analysis

### MITRE ATT&CK Mapping

Mapped Techniques Include:

* T1046 – Network Service Discovery
* T1018 – Remote System Discovery
* T1021.002 – SMB / Windows Admin Shares
* T1059.001 – PowerShell
* T1059.003 – Windows Command Shell
* T1210 – Exploitation of Remote Services

---

## Skills Demonstrated

* SOC Operations
* Detection Engineering
* Threat Hunting
* SIEM Administration
* Vulnerability Management
* Endpoint Monitoring
* Security Investigation
* Incident Response
* MITRE ATT&CK Mapping
* Log Analysis

---

## Future Enhancements

* MISP Threat Intelligence Integration
* IOC Enrichment Workflows
* Velociraptor DFIR Investigations
* ATT&CK Coverage Expansion
* Additional Detection Engineering Use Cases

---

## Disclaimer

This repository was created for cybersecurity education, portfolio development, detection engineering practice, and defensive security research.

All testing was performed within authorized and isolated laboratory environments.

