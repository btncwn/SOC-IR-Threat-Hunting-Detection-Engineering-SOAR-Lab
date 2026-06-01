# MITRE ATT&CK Mapping

## Overview

This phase maps the activities observed during the lab exercises to the MITRE ATT&CK framework.

The objective is to understand attacker behavior, align detections with industry-standard techniques, and validate security monitoring coverage across the attack lifecycle.

---

## Assessment Scope

The mapping was performed using evidence collected from:

* Nessus Vulnerability Assessment
* SMB Enumeration Activities
* Sysmon Endpoint Telemetry
* Splunk Threat Hunting Investigations
* SOC Dashboard Analysis

---

## ATT&CK Technique Mapping

| Tactic           | Technique ID | Technique                       |
| ---------------- | ------------ | ------------------------------- |
| Discovery        | T1046        | Network Service Discovery       |
| Discovery        | T1018        | Remote System Discovery         |
| Lateral Movement | T1021.002    | SMB / Windows Admin Shares      |
| Execution        | T1059.001    | PowerShell                      |
| Execution        | T1059.003    | Windows Command Shell           |
| Exploitation     | T1210        | Exploitation of Remote Services |

---

## Technique Analysis

### T1046 – Network Service Discovery

Observed during SMB enumeration activities conducted from the Kali Linux attacker workstation.

Evidence:

* SMB enumeration
* Service discovery
* TCP/445 identification

---

### T1018 – Remote System Discovery

The Windows 7 endpoint was identified and profiled through reconnaissance activities.

Evidence:

* Host identification
* Operating system fingerprinting
* SMB banner information

---

### T1021.002 – SMB / Windows Admin Shares

SMB services were successfully identified and evaluated.

Evidence:

* SMBv1 Enabled
* SMB Signing Disabled
* Accessible SMB service on TCP/445

---

### T1059.001 – PowerShell

PowerShell activity was captured through Sysmon telemetry and monitored within Splunk.

Evidence:

* PowerShell execution events
* PowerShell monitoring dashboard panels
* Threat hunting investigations

---

### T1059.003 – Windows Command Shell

Command-line execution activity was collected and analyzed.

Evidence:

* cmd.exe execution
* Command-line activity monitoring
* Process creation telemetry

---

### T1210 – Exploitation of Remote Services

The Nessus assessment identified the Windows 7 endpoint as vulnerable to MS17-010 (EternalBlue).

Evidence:

* SMBv1 exposure
* Missing KB4012212 / KB4012215
* MS17-010 vulnerability detection
* Remote code execution risk

---

## Detection Coverage

The following telemetry sources provided visibility into mapped ATT&CK techniques:

* Sysmon Event ID 1 (Process Creation)
* Sysmon Event ID 3 (Network Connections)
* Sysmon Event ID 5 (Process Termination)
* PowerShell Activity Monitoring
* Splunk Threat Hunting Queries
* SOC Dashboard Visualizations

---

## Outcome

The lab successfully mapped observed attack behaviors and identified vulnerabilities to multiple MITRE ATT&CK techniques.

This process improved understanding of attacker methodology and validated the effectiveness of endpoint telemetry and SIEM-based detection workflows.
