# Detection 02 – Suspicious Parent Child Process Relationship

## Overview

This detection engineering project focuses on identifying suspicious parent-child process relationships involving `fodhelper.exe` spawning `powershell.exe`.

Parent-child process analysis is a fundamental threat hunting and detection engineering technique used to identify abnormal process execution chains that may indicate malicious activity.

The detection was developed after identifying multiple Sysmon process creation events within the BOTSv3 dataset where `fodhelper.exe` launched `powershell.exe`, a relationship commonly associated with privilege escalation and User Account Control (UAC) bypass techniques.

---

## Detection Objective

Detect PowerShell execution where the parent process is:

```text
fodhelper.exe
```

This behavior is uncommon in normal enterprise environments and may indicate:

* Privilege Escalation
* User Account Control (UAC) Bypass
* Malicious PowerShell Execution
* Post-Exploitation Activity

---

## Why This Detection Was Created

During analysis of BOTSv3 Sysmon telemetry, multiple process creation events were identified where:

```text
fodhelper.exe
        ↓
powershell.exe
```

This process relationship occurred six times within the dataset and warranted further investigation.

Unlike common PowerShell launches from:

```text
explorer.exe
cmd.exe
services.exe
```

the use of `fodhelper.exe` is unusual and often associated with attacker tradecraft.

The identified events also contained encoded PowerShell execution, increasing the likelihood that the activity represented malicious or post-exploitation behavior.

---

## Sigma Detection Logic

The detection searches for:

* Parent Process = `fodhelper.exe`
* Child Process = `powershell.exe`

This combination is uncommon in normal enterprise environments and may indicate:

* Privilege Escalation
* User Account Control (UAC) Bypass
* Malicious PowerShell Execution
* Post-Exploitation Activity

### Sigma Rule

See:

```text
sigma-rule.yml
```

### Sigma ATT&CK Tags

The detection uses the following Sigma ATT&CK mappings:

| Sigma Tag        | MITRE ATT&CK Mapping              |
| ---------------- | --------------------------------- |
| attack.execution | Execution                         |
| attack.t1059.001 | PowerShell                        |
| attack.t1548     | Abuse Elevation Control Mechanism |
| attack.t1548.002 | Bypass User Account Control       |

---

## Splunk Validation

The detection was validated against BOTSv3 Sysmon telemetry within Splunk Enterprise.

Validation confirmed multiple matching events where:

```text
fodhelper.exe
        ↓
powershell.exe
```

occurred within the dataset.

To validate the detection, Sysmon Event ID 1 process creation events were analyzed and parent-child process relationships were extracted from the event data.

Validation confirmed six matching events.

---

## Detection Results

Observed activity included:

* PowerShell execution
* Encoded PowerShell commands
* Suspicious parent-child relationships
* Potential privilege escalation behavior
* UAC bypass indicators
* Process execution anomalies

The detection successfully identified process chains that would warrant investigation within a production SOC environment.

---

## MITRE ATT&CK Mapping

| Tactic               | Technique | Description                       |
| -------------------- | --------- | --------------------------------- |
| Execution            | T1059.001 | PowerShell                        |
| Privilege Escalation | T1548     | Abuse Elevation Control Mechanism |
| Defense Evasion      | T1548.002 | Bypass User Account Control       |

### ATT&CK Interpretation

The observed process chain:

```text
fodhelper.exe
        ↓
powershell.exe
```

may indicate an attempt to execute PowerShell through a trusted Windows binary capable of bypassing User Account Control (UAC).

This technique is frequently associated with attacker privilege escalation and defense evasion activity and should be investigated by SOC analysts when observed in enterprise environments.

---

## Detection Engineering Workflow

```text
Suspicious Parent Process Observed
                ↓
Sysmon Event Identified
                ↓
Parent-Child Relationship Analyzed
                ↓
Sigma Rule Created
                ↓
PySigma Conversion
                ↓
Splunk Validation
                ↓
Detection Confirmed
```

---

## Analyst Assessment

This detection demonstrates how parent-child process analysis can identify suspicious execution chains that may be missed by simple command-line monitoring.

The observed `fodhelper.exe → powershell.exe` relationship represents behavior that should be investigated by SOC analysts due to its association with privilege escalation and defense evasion techniques.

This project demonstrates the complete Detection Engineering lifecycle:

* Identifying suspicious behavior
* Creating a Sigma rule
* Mapping detections to MITRE ATT&CK
* Validating detections against real telemetry
* Investigating suspicious process relationships
* Developing reusable detection content

The detection successfully identified suspicious parent-child process activity within the BOTSv3 dataset and demonstrates how Sigma can be used to detect abnormal execution chains commonly leveraged by attackers.
