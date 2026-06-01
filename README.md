# SOC Detection Engineering, Threat Hunting & DFIR Lab

## Overview

This repository documents an end-to-end Security Operations Center (SOC) lab built to simulate a realistic cyber attack lifecycle and demonstrate blue-team security operations.

The project combines vulnerability management, attack simulation, endpoint telemetry collection, SIEM engineering, threat hunting, MITRE ATT&CK mapping, threat intelligence, and digital forensics to provide practical experience across multiple cybersecurity disciplines.

The lab was developed using real telemetry collected from a Windows 7 environment and analyzed through Splunk Enterprise.

---

## Key Achievement

A credentialed Nessus vulnerability assessment identified a critical **MS17-010 (EternalBlue)** exposure on a Windows 7 endpoint.

The vulnerability was subsequently validated through SMB enumeration activities, monitored through Sysmon telemetry, ingested into Splunk Enterprise, and analyzed through threat hunting and SOC monitoring workflows.

---

## Lab Environment

### Attacker Infrastructure

* Kali Linux

### Target Environment

* Windows 7 Professional SP1 x64
* Sysmon
* Splunk Universal Forwarder

### Security Monitoring Stack

* Splunk Enterprise
* Nessus Essentials
* Sysmon
* Splunk Universal Forwarder

### Planned Integrations

* MISP (Threat Intelligence)
* Velociraptor (DFIR)

---

## Attack Flow

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
6. MITRE ATT&CK Mapping
           ↓
7. Threat Intelligence Enrichment
           ↓
8. Digital Forensics & Incident Response
           ↓
9. Incident Reporting
```

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
| MISP                       | Threat Intelligence (Planned)      |
| Velociraptor               | DFIR Investigations (Planned)      |

---

## Repository Structure

```text
SOC-Detection-Engineering-Threat-Hunting-DFIR-Lab

├── 01-lab-architecture
├── 02-vulnerability-assessment
├── 03-attack-simulation
├── 04-endpoint-telemetry
├── 05-splunk-ingestion
├── 06-threat-hunting
├── 07-mitre-attack-mapping
├── 08-threat-intelligence
├── 09-dfir
├── 10-incident-report
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

