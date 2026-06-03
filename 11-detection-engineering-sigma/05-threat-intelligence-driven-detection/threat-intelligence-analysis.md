# Threat Intelligence Analysis

## Overview

This project demonstrates how threat intelligence can be transformed into actionable detection engineering content.

Rather than focusing solely on static indicators such as IP addresses, domains, or file hashes, the project focuses on identifying attacker behaviors and translating those behaviors into reusable detections.

The intelligence source for this project was a published MISP event associated with the Space Pirates threat actor.

Event:

```text
1723 - OSINT - Space Pirates: analyzing the tools and connections of a new hacker group
```

Threat Level:

```text
High
```

Analysis Status:

```text
Completed
```

Published:

```text
Yes
```

---

# Intelligence Findings

Analysis of the threat intelligence identified the use of PlugX RAT.

PlugX is a Remote Access Trojan (RAT) commonly used by advanced threat actors to establish long-term access to compromised systems.

Capabilities associated with PlugX include:

* Remote command execution
* Process management
* Service manipulation
* Registry modification
* System discovery
* Network discovery
* Keylogging
* Screen capture
* Data collection

These capabilities provide multiple opportunities for behavioral detection.

---

# Detection Engineering Mindset

A key lesson from this investigation is:

> Hashes change. IPs change. Domains change. Behaviors persist.

Threat actors frequently modify infrastructure and malware samples to evade indicator-based detections.

Behavioral detections remain effective because they focus on attacker actions rather than individual indicators.

For this reason, the project emphasizes:

* PowerShell execution
* Scheduled task creation
* Service manipulation
* Network discovery activity

instead of relying solely on hashes, domains, or IP addresses.

---

# Detection Strategy

The overall workflow used throughout this project is shown below:

```text
Threat Intelligence
        ↓
Adversary Analysis
        ↓
MITRE ATT&CK Mapping
        ↓
Behavior Identification
        ↓
Sigma Rule Development
        ↓
PySigma Conversion
        ↓
Splunk Validation
        ↓
Detection Tuning
```

This approach mirrors the workflow used by Detection Engineers, Threat Hunters, and SOC Analysts in operational environments.

---

# Intelligence-Driven Behaviors

The following behaviors were selected for detection development:

### PowerShell Execution

PowerShell is frequently used by attackers to execute commands, download payloads, and perform post-exploitation activities.

### Scheduled Task Creation

Scheduled tasks are commonly used to establish persistence and maintain access across reboots.

### Service Manipulation

Attackers often create, modify, or start Windows services to execute malicious code.

### Network Discovery

Discovery activity is frequently observed during post-compromise reconnaissance and lateral movement preparation.

---

# Project Objective

The objective of this project is to transform threat intelligence associated with Space Pirates and PlugX RAT into behavioral Sigma detections that can be converted into Splunk searches and validated against available telemetry.

The result is a set of reusable detections that remain effective even when attacker infrastructure or malware samples change over time.
