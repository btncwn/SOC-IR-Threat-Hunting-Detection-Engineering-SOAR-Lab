# Detection 04 – Suspicious Scheduled Task Creation via PowerShell

## Overview

This detection focuses on identifying suspicious scheduled task creation activity initiated through PowerShell.

During threat hunting activities within the BOTSv3 dataset, multiple potential lateral movement and persistence techniques were investigated. The objective was to identify a realistic attacker technique that could be converted into a Sigma detection and validated within Splunk.

Several candidate techniques were analyzed before a high-confidence detection opportunity was identified involving PowerShell spawning `schtasks.exe` to create scheduled tasks.

---

# Detection Objective

Detect suspicious scheduled task creation activity where:

```text
powershell.exe
        ↓
schtasks.exe
        ↓
Task Creation
```

This execution chain is frequently associated with:

* Persistence
* Automated payload execution
* Malware execution
* Defense evasion
* PowerShell abuse

---

# Threat Hunting Methodology

The investigation began with a hypothesis-driven hunting process.

Several potential attacker techniques were investigated and validated against telemetry before selecting the final detection.

---

## Investigation 1 – WMIC Activity

Initial hunting identified approximately 3,947 WMIC-related events.

Analysis revealed that the overwhelming majority of events consisted of:

```text
wmic os get LocalDateTime /value
```

This activity represented normal operating system behavior rather than remote execution or lateral movement.

### Result

```text
Not Selected
Legitimate Activity
```

---

## Investigation 2 – WinRM Activity

Further hunting identified approximately 204 WinRM-related events.

Analysis revealed:

* 203 service inventory records
* 1 security-related event

The events represented inventory and monitoring data rather than active remote administration activity.

### Result

```text
Not Selected
Inventory Data
```

---

## Investigation 3 – Service Installation Events

Windows Event ID 7045 was investigated.

Only two service installation events were identified.

Analysis revealed legitimate Microsoft Defender driver installations.

Example:

```text
MpKsl*.sys
```

### Result

```text
Not Selected
Legitimate Service Installation
```

---

## Investigation 4 – Network Logon Activity

Successful logon events (Event ID 4624) were analyzed.

Logon type distribution revealed:

| Logon Type | Count |
| ---------- | ----- |
| 5          | 413   |
| 2          | 8     |
| 0          | 2     |
| 11         | 2     |
| 7          | 2     |

Further investigation showed that the majority of activity involved:

* SYSTEM
* Computer accounts
* Service logons

No meaningful evidence of attacker lateral movement was identified.

### Result

```text
Not Selected
Normal Authentication Activity
```

---

## Investigation 5 – Scheduled Task Creation

Threat hunting identified suspicious scheduled task creation activity involving:

```text
powershell.exe
        ↓
schtasks.exe
```

Example activity included:

```text
schtasks.exe /Create /F /RU system
```

Additional command-line analysis revealed indicators including:

```text
-NonI
-W hidden
IEX
```

These behaviors are frequently associated with:

* Malicious PowerShell execution
* Persistence mechanisms
* Obfuscated payload execution
* Automated attacker actions

This represented the strongest detection opportunity identified during the investigation.

### Result

```text
Selected for Detection Development
```

---

# Sigma Detection Logic

The Sigma rule detects:

* PowerShell launching schtasks.exe
* Scheduled task creation activity
* Suspicious parent-child process relationships

The detection focuses on process behavior rather than simple keyword matching.

---

# Sigma Rule

See:

```text
sigma-rule.yml
```

---

# Sigma to Splunk Conversion

After creating the Sigma rule, the rule was converted into Splunk SPL using Sigma CLI.

Command used:

```bash
sigma convert -t splunk --without-pipeline sigma-rule.yml
```

This conversion process demonstrates how Sigma rules can be written once and translated into SIEM-specific detection logic.

Detection workflow:

```text
Threat Hunt
      ↓
Sigma Rule
      ↓
Sigma Conversion
      ↓
Splunk Query
      ↓
Validation
      ↓
Detection Tuning
```

---

# Splunk Validation

The detection was validated against the BOTSv3 dataset.

Threat hunting searches included:

```spl
index=botsv3 schtasks
```

Additional searches were performed to validate:

* Parent-child process relationships
* PowerShell execution
* Scheduled task creation behavior
* Process command-line activity

The detection successfully identified suspicious scheduled task activity associated with PowerShell execution.

---

# Screenshots

## 01-sigma-rule-creation.png

Demonstrates:

* Sigma rule development
* Detection logic
* ATT&CK mapping
* Parent-child process analysis

---

## 02-detection-validation.png

Demonstrates:

* Splunk validation
* Matching telemetry
* Scheduled task creation activity
* Detection results

---

# MITRE ATT&CK Mapping

| Tactic          | Technique | Description                     |
| --------------- | --------- | ------------------------------- |
| Persistence     | T1053.005 | Scheduled Task                  |
| Execution       | T1059.001 | PowerShell                      |
| Defense Evasion | T1027     | Obfuscated Files or Information |

---

# Analyst Assessment

This project demonstrates a realistic Detection Engineering workflow.

Rather than creating a detection from a predefined signature, the detection was developed through iterative threat hunting and evidence-based investigation.

Multiple candidate techniques were investigated and ruled out before identifying a high-confidence detection opportunity.

The final detection demonstrates:

* Threat Hunting
* Detection Engineering
* Sigma Development
* Splunk Validation
* ATT&CK Mapping
* Process Analysis
* Parent-Child Relationship Analysis
* SOC Investigation Methodology

---

# Conclusion

This detection demonstrates how threat hunting can be used to identify suspicious scheduled task creation activity and transform investigative findings into a reusable Sigma detection.

The project showcases the complete detection engineering lifecycle from hypothesis generation and telemetry analysis through Sigma rule creation, Splunk conversion, validation, and ATT&CK mapping.
