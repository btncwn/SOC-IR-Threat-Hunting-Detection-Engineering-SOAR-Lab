# SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab

## Overview

This repository documents an end-to-end Security Operations Center (SOC) lab built to simulate a realistic cyber attack lifecycle and demonstrate blue-team security operations.

The project combines vulnerability management, attack simulation, endpoint telemetry collection, SIEM engineering, threat hunting, MITRE ATT&CK mapping, threat intelligence, to provide practical experience across multiple cybersecurity disciplines.

The lab was developed using real telemetry collected from a Windows 7 environment and analyzed through Splunk Enterprise.

## Key Achievements

✅ Built an end-to-end SOC lab covering Telemetry → Detection → Threat Hunting → Incident Response → Threat Intelligence → SOAR Automation

✅ Deployed and integrated Splunk Enterprise, Sysmon, MISP, Nessus, Docker, and Windows endpoints within a single security monitoring environment

✅ Created and validated Sigma detection rules using PySigma and Splunk

✅ Mapped observed attacker behaviours to MITRE ATT&CK techniques and tactics

✅ Performed Threat Intelligence investigations using MISP and IOC enrichment workflows

✅ Conducted Incident Response investigations including persistence, lateral movement, command and control, and data exfiltration scenarios

✅ Developed SOAR playbooks and security automation workflows using Python and threat intelligence enrichment processes

✅ Produced 30+ technical project write-ups supported by 49+ screenshots, validation artefacts, and investigation evidence



## Project Journey

Designed and built a complete SOC Detection Engineering, Threat Hunting, Threat Intelligence, and Incident Response lab from the ground up using Splunk Enterprise, Sysmon, Nessus Essentials, MISP, Sigma, and the BOTSv3 dataset.

During the project, multiple technical challenges were encountered and resolved. Initial attempts to forward Windows event logs from a Windows 11 UTM virtual machine to a Splunk Enterprise instance running on macOS were unsuccessful, requiring redesign of the lab architecture. To overcome compatibility and telemetry collection issues, the environment was rebuilt using a dedicated Windows 7 endpoint and a Kali Linux attacker system.

Successfully deployed and configured Sysmon and Splunk Universal Forwarder on legacy Windows infrastructure, generated endpoint telemetry, and validated successful ingestion into Splunk Enterprise for security monitoring and threat hunting activities.

Conducted vulnerability assessments using Nessus Essentials, identified a critical MS17-010 (EternalBlue) exposure, validated the findings through SMB enumeration activities, and analyzed resulting telemetry through Splunk-based investigations.

Developed structured threat hunting investigations covering malicious domains, malware hashes, suspicious PowerShell activity, attacker behaviour analysis, detection engineering, threat intelligence enrichment, and incident response workflows.

The project demonstrates the ability to design, build, troubleshoot, document, and operate an end-to-end SOC environment using real telemetry and industry-standard security technologies.




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

### Incident Response (IR)

* Incident Response Playbooks
* Endpoint Investigation Workflows


### Detection Engineering

* Sigma Rule Development
* Splunk Detection Development
* MITRE ATT&CK Mapping
* Detection Validation & Tuning

---


## Technologies Used


| Technology                     | Purpose                                                           |
| ------------------------------ | ----------------------------------------------------------------- |
| Splunk Enterprise              | SIEM Platform, Security Monitoring, Threat Hunting & Dashboarding |
| Sysmon                         | Endpoint Telemetry & Process Monitoring                           |
| Splunk Universal Forwarder     | Log Collection & Event Forwarding                                 |
| Kali Linux                     | Attack Simulation & Adversary Emulation                           |
| Windows 7 Professional SP1 x64 | Target Environment                                                |
| Nessus Essentials              | Vulnerability Assessment & Exposure Validation                    |
| MITRE ATT&CK                   | Adversary Behavior Mapping & Detection Coverage                   |
| MISP                           | Threat Intelligence Platform, IOC Enrichment & Threat Hunting     |
| BOTSv3 Dataset                 | Detection Validation & Threat Hunting Exercises                   |
| Sigma                          | Detection Engineering & Portable Detection Development            |
| GitHub Pages                   | Cybersecurity Portfolio & Project Documentation                   |
| SOAR Workflows                 | Security Automation & Playbook Development (In Progress)          

## Repository Structure

SOC-Detection-Engineering-Threat-Hunting-DFIR-Lab
01-lab-architecture
02-vulnerability-assessment
03-attack-simulation
04-endpoint-telemetry
05-splunk-ingestion
06-threat-hunting
07-mitre-attack-mapping
08-threat-intelligence
09-incident response
10-soc-investigations
11-detection-engineering-sigma
12-soar-automation


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


## Skills Demonstrated

* Security Operations Center (SOC) Operations
* Threat Hunting & Investigation
* Detection Engineering (Sigma)
* SIEM Administration (Splunk Enterprise)
* Vulnerability Assessment & Exposure Validation
* Endpoint Monitoring & Telemetry Analysis
* Threat Intelligence & IOC Enrichment (MISP)
* MITRE ATT&CK Mapping
* Incident Response Methodology
* Security Event Analysis & Correlation
* PowerShell & Process Analysis
* Log Collection, Parsing & Forwarding
* Detection Validation & Tuning
* Security Reporting & Documentation


 ## Version 1.1 Enhancements

• CSV upload support for Splunk investigations
• Automated telemetry summarization using Pandas
• AI-assisted threat intelligence analysis
• Detection of suspicious PHP endpoint activity
• IOC extraction from uploaded HTTP telemetry


## Future Enhancements
* SOAR Playbook Development & Automation
* Threat Intelligence Automated Enrichment Workflows
* Advanced Sigma Detection Engineering Use Cases
* Splunk Enterprise Security (ES) Use Cases
* Detection Coverage Expansion Across Additional ATT&CK Techniques
* Automated Alert Triage & Investigation Workflows
* Custom Threat Hunting Dashboards
* Elastic Security Detection & Threat Hunting Lab
* Microsoft Sentinel Detection Engineering Lab


## Disclaimer

This repository was created for cybersecurity education, portfolio development, detection engineering practice, and defensive security research.

All testing was performed within authorized and isolated laboratory environments.

