# Threat Hunting Using Splunk & Sysmon

## Overview

This phase focused on proactive threat hunting using Sysmon telemetry collected from a Windows 7 endpoint and analyzed within Splunk Enterprise.

The objective was to identify suspicious activity, investigate process behavior, and validate endpoint visibility through custom SPL searches.

---

## Environment

### Endpoint

* Windows 7 Professional SP1 x64
* Sysmon Installed
* Splunk Universal Forwarder Installed

### Monitoring Platform

* Splunk Enterprise

### Telemetry Source

* Microsoft-Windows-Sysmon/Operational

---

## Threat Hunting Methodology

The hunting process followed a hypothesis-driven approach:

1. Collect endpoint telemetry
2. Identify abnormal behavior patterns
3. Investigate suspicious processes
4. Analyze parent-child process relationships
5. Review command-line activity
6. Validate findings using multiple data points

---

## Hunting Scenario 1: Process Creation Monitoring

Objective:

Identify processes commonly associated with attacker activity.

Examples:

* cmd.exe
* powershell.exe
* wmic.exe
* reg.exe
* rundll32.exe

Example SPL:

```spl
index=* sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational"
| rex field=_raw "<Data Name='Image'>(?<Image>[^<]+)</Data>"
| top limit=20 Image
```

---

## Hunting Scenario 2: PowerShell Activity

Objective:

Identify PowerShell execution that may indicate administrative activity, scripting, or attacker behavior.

Example SPL:

```spl
index=* sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational"
| search powershell
```

---

## Hunting Scenario 3: Parent → Child Process Analysis

Objective:

Identify suspicious process spawning behavior.

Example Investigation Questions:

* Did PowerShell launch cmd.exe?
* Did Office launch PowerShell?
* Did Explorer launch unexpected processes?

Example SPL:

```spl
index=* sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational"
| rex field=_raw "<Data Name='Image'>(?<Image>[^<]+)</Data>"
| rex field=_raw "<Data Name='ParentImage'>(?<ParentImage>[^<]+)</Data>"
| stats count by ParentImage Image
| sort -count
```

---

## Hunting Scenario 4: Command-Line Activity

Objective:

Investigate command execution behavior and identify potentially suspicious commands.

Example SPL:

```spl
index=* sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational"
| search whoami OR ipconfig OR net
```

---

## Hunting Scenario 5: SMB Exposure Investigation

Objective:

Investigate activity associated with SMB services following the discovery of the MS17-010 (EternalBlue) vulnerability.

Key Findings:

* SMBv1 Enabled
* SMB Signing Disabled
* TCP/445 Accessible
* Windows 7 SP1 x64

These findings were validated through both Nessus vulnerability assessment and SMB enumeration activities.

---

## Evidence

Evidence of hunting activities can be observed within:

* SOC Attack Timeline Dashboard
* Process Activity Monitoring Panels
* PowerShell Monitoring Panels
* Parent → Child Relationship Analysis

---

## Key Findings

Threat hunting activities successfully identified:

* Process creation events
* PowerShell execution activity
* Command-line execution activity
* Parent-child process relationships
* SMB exposure indicators
* Endpoint activity patterns

---

## Outcome

Threat hunting exercises demonstrated the value of Sysmon telemetry and Splunk analytics for identifying suspicious activity and improving endpoint visibility.

The collected telemetry enabled proactive investigation workflows and formed the foundation for ATT&CK mapping and incident response activities.
