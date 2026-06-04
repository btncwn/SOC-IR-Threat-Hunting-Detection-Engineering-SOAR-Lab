# Scheduled Task Investigation Playbook

## Overview

This project documents a Security Operations Center (SOC) investigation workflow for suspicious scheduled task creation activity.

Scheduled tasks are commonly abused by attackers to establish persistence, execute malicious code, maintain access, and evade detection.

The objective of this playbook is to provide analysts with a structured process for investigating scheduled task alerts and determining whether activity is benign, suspicious, or malicious.

---

## Why Scheduled Tasks Matter

Scheduled tasks are legitimate Windows administrative functionality.

However, attackers frequently abuse them to:

* Establish persistence
* Execute malware
* Launch PowerShell payloads
* Maintain privileged access
* Evade user interaction

For this reason, scheduled task creation should be reviewed whenever suspicious command lines, PowerShell activity, or elevated privileges are involved.

---

## Investigation Scenario

During threat hunting activities within the BOTSv3 dataset, a scheduled task creation event was identified involving:

```text
PowerShell
      ↓
schtasks.exe
      ↓
/Create
      ↓
SYSTEM
      ↓
Hidden PowerShell
```

The activity was investigated to determine whether it represented legitimate administration or potential malicious persistence.

---

## Investigation Workflow

```text
SOC Alert
      ↓
Scheduled Task Created
      ↓
Command Line Review
      ↓
Parent Process Analysis
      ↓
PowerShell Investigation
      ↓
Persistence Assessment
      ↓
Risk Assessment
      ↓
Analyst Decision
```

---

## Investigation Findings

### Scheduled Task Creation

Evidence identified the use of:

```text
schtasks.exe /Create
```

Scheduled task creation is frequently associated with persistence mechanisms used by attackers.

Screenshot:

```text
01-detection-triggered.png
```

---

### Parent Process Analysis

Process analysis identified the following execution chain:

```text
PowerShell
      ↓
schtasks.exe
```

PowerShell launching scheduled task creation activity may indicate automated persistence or malicious execution.

Screenshot:

```text
02-command-line-analysis.png
```

---

### Persistence Analysis

Additional review identified:

```text
SYSTEM Execution
Hidden PowerShell
```

These characteristics increase the likelihood of malicious intent and warrant additional investigation.

Screenshot:

```text
03-persistence-analysis.png
```

---

## MITRE ATT&CK Mapping

### T1053.005 – Scheduled Task

Adversaries may create scheduled tasks to execute malware or maintain persistence.

### T1059.001 – PowerShell

PowerShell may be used to execute commands, scripts, or malicious payloads.

### T1027 – Obfuscated Files or Information

Hidden or encoded PowerShell execution may indicate attempts to evade detection.

---

## Risk Assessment

| Indicator               | Result |
| ----------------------- | ------ |
| Scheduled Task Creation | Yes    |
| PowerShell Usage        | Yes    |
| SYSTEM Context          | Yes    |
| Hidden Execution        | Yes    |
| Persistence Technique   | Yes    |
| Risk Level              | High   |

Screenshot:

```text
04-risk-assessment.png
```

---

## Analyst Assessment

The observed activity demonstrated multiple characteristics commonly associated with persistence mechanisms.

The combination of PowerShell execution, scheduled task creation, SYSTEM-level execution, and hidden activity significantly increased the risk profile of the event.

While additional host context would be required to determine intent conclusively, the activity warranted escalation and further investigation.

Screenshot:

```text
05-analyst-decision.png
```

---

## Skills Demonstrated

* Threat Hunting
* Detection Engineering
* SOC Investigation
* Process Analysis
* Persistence Analysis
* PowerShell Investigation
* MITRE ATT&CK Mapping
* Incident Triage
* Security Operations

---

## Key Lessons Learned

* Scheduled tasks are frequently abused by attackers.
* Parent-child process analysis provides valuable context.
* PowerShell activity should be reviewed carefully.
* Persistence mechanisms often combine multiple techniques.
* Analyst investigation is required to distinguish malicious activity from legitimate administration.

> Detection identifies activity. Investigation determines meaning.
