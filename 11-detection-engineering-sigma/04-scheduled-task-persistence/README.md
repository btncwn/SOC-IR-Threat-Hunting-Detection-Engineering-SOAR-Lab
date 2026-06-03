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

# Sigma Rule Development

After identifying suspicious scheduled task creation activity, a Sigma detection rule was developed to detect PowerShell spawning `schtasks.exe` for task creation.

The objective was to create a platform-independent detection that could later be translated into SIEM-specific query languages.

The Sigma rule focused on three behavioral indicators:

* Parent Process = PowerShell
* Child Process = schtasks.exe
* Command Line contains `/Create`

This behavioral approach is more resilient than simple keyword matching because it focuses on process relationships and attacker actions.

---

# Sigma Rule

See:

```text
sigma-rule.yml
```

Core Detection Logic:

```yaml
title: Suspicious Scheduled Task Creation via PowerShell
id: 7d2c5b41-5f67-4f2c-8e2a-9d4a8f2e1c11
status: experimental

description: Detects PowerShell spawning schtasks.exe to create a scheduled task.

logsource:
  product: windows
  category: process_creation

detection:
  selection_parent:
    ParentImage|endswith:
      - '\powershell.exe'

  selection_child:
    Image|endswith:
      - '\schtasks.exe'

  selection_command:
    CommandLine|contains:
      - '/Create'

  condition: selection_parent and selection_child and selection_command
```

---

# Sigma to Splunk Conversion

After creating the Sigma rule, the rule was converted into Splunk SPL using PySigma.

Command used:

```bash
sigma convert -t splunk --without-pipeline \
11-detection-engineering-sigma/04-scheduled-task-persistence/sigma-rule.yml
```

---

# Why "--without-pipeline" Was Used

PySigma normally uses processing pipelines to translate Sigma field names into SIEM-specific schemas.

Examples include:

```text
Image
ParentImage
CommandLine
ProcessGuid
```

For this project, the goal was to observe the raw Splunk query generated directly from the Sigma rule before any field mapping transformations were applied.

Using:

```bash
--without-pipeline
```

allowed validation of:

* Sigma detection logic
* Query translation accuracy
* Field mapping assumptions
* Detection engineering workflow

This approach is commonly used in laboratory environments when learning and validating Sigma detections.

---

# Generated Splunk Query

PySigma successfully generated the following Splunk SPL:

```spl
ParentImage="*\\powershell.exe" Image="*\\schtasks.exe" CommandLine="*/Create*"
```

This demonstrated successful translation of Sigma detection logic into Splunk search syntax.

---

# Splunk Validation Challenges

Although the Sigma conversion was successful, the generated SPL did not immediately return results within the BOTSv3 dataset.

Investigation revealed that Sysmon process creation events within BOTSv3 were stored as raw XML rather than fully extracted process creation fields.

As a result, fields such as:

```text
ParentImage
Image
CommandLine
```

were embedded within XML event structures and could not be queried directly using the generated SPL.

This is a common challenge encountered during SIEM implementation and detection engineering activities.

---

# Detection Tuning for BOTSv3

To validate the detection against BOTSv3 telemetry, the Sigma-generated query was adapted to search raw XML data directly.

Validation search:

```spl
index=botsv3 "powershell.exe" "schtasks.exe" "/Create"
| rex field=_raw "<Data Name='Image'>(?<Image>[^<]+)</Data>"
| rex field=_raw "<Data Name='CommandLine'>(?<CommandLine>[^<]+)</Data>"
| rex field=_raw "<Data Name='ParentImage'>(?<ParentImage>[^<]+)</Data>"
| rex field=_raw "<Data Name='ParentCommandLine'>(?<ParentCommandLine>[^<]+)</Data>"
| table _time host Image CommandLine ParentImage ParentCommandLine
```

This approach extracted process creation fields directly from raw Sysmon XML events and allowed successful validation of the detection.

---

# Detection Engineering Workflow

This project demonstrates a realistic Detection Engineering workflow:

```text
Threat Hunting
      ↓
Hypothesis Generation
      ↓
Telemetry Analysis
      ↓
Sigma Rule Development
      ↓
PySigma Conversion
      ↓
Splunk Validation
      ↓
Detection Tuning
      ↓
Final Detection
```

Rather than relying solely on automated rule generation, the detection required manual validation and tuning to account for the structure of the underlying telemetry.

This mirrors real-world SOC operations where detections often require refinement before deployment into production monitoring environments.

---

# Screenshots

## 01-sigma-rule-creation.png

Demonstrates:

* Sigma rule development
* Detection logic creation
* ATT&CK mapping
* Parent-child process analysis

---

## 02-pysigma-splunk-conversion.png

Demonstrates:

* PySigma conversion process
* Sigma to Splunk translation
* Generated SPL query
* Detection engineering workflow

---

## 03-detection-validation.png


Detection validation returned 1 high-confidence event matching all Sigma conditions:

ParentImage = powershell.exe  
Image = schtasks.exe  
CommandLine contains /Create

This confirmed that the Sigma detection logic successfully identified suspicious scheduled task creation initiated by PowerShell.

Demonstrates:

* Splunk validation
* BOTSv3 telemetry analysis
* XML field extraction
* Detection tuning and validation

---

# MITRE ATT&CK Mapping

| Tactic          | Technique | Description                     |
| --------------- | --------- | ------------------------------- |
| Persistence     | T1053.005 | Scheduled Task                  |
| Execution       | T1059.001 | PowerShell                      |
| Defense Evasion | T1027     | Obfuscated Files or Information |

---

# Analyst Assessment

This detection demonstrates how threat hunting findings can be transformed into reusable Sigma detections and validated within a SIEM platform.

The project showcases:

* Threat Hunting
* Detection Engineering
* Sigma Development
* PySigma Conversion
* Splunk Validation
* Detection Tuning
* Process Analysis
* ATT&CK Mapping
* SOC Investigation Methodology

Multiple candidate techniques were investigated and ruled out before identifying a high-confidence detection opportunity involving PowerShell-driven scheduled task creation.

# Key Detection Engineering Takeaways

This project demonstrates the complete lifecycle of a detection engineering workflow.

The investigation progressed through the following stages:

### 1. Threat Hunting

Initial Splunk searches were used to identify suspicious scheduled task creation activity within the BOTSv3 dataset.

Threat hunting identified an event involving:

```text
PowerShell
      ↓
schtasks.exe
      ↓
Scheduled Task Creation
```

This activity was selected as a candidate detection.

---

### 2. Sigma Rule Development

The observed behavior was translated into a Sigma detection rule.

Rather than creating a Splunk-specific search, the detection was written using Sigma's platform-independent format.

The Sigma rule focused on:

* Parent Process = powershell.exe
* Child Process = schtasks.exe
* Command Line contains /Create

This transformed a single threat hunting finding into a reusable detection.

---

### 3. PySigma Conversion

The Sigma rule was converted into Splunk SPL using PySigma.

Command used:

```bash
sigma convert -t splunk --without-pipeline \
11-detection-engineering-sigma/04-scheduled-task-persistence/sigma-rule.yml
```

Generated SPL:

```spl
ParentImage="*\\powershell.exe" Image="*\\schtasks.exe" CommandLine="*/Create*"
```

This demonstrated that the Sigma rule could successfully be translated into Splunk search syntax.

---

### 4. Splunk Validation

The generated detection was validated against real BOTSv3 telemetry.

During validation it was discovered that process creation fields were embedded within raw XML data rather than being extracted as searchable fields.

Additional tuning was required to validate the detection against the dataset.

Validation confirmed that all Sigma conditions matched a real Sysmon process creation event.

---

### 5. Detection Outcome

The final detection successfully identified:

```text
PowerShell
      ↓
schtasks.exe
      ↓
Task Creation
      ↓
SYSTEM Execution
      ↓
Hidden PowerShell Activity
```

The event was assessed as a high-confidence persistence mechanism consistent with attacker tradecraft.

---

## Summary

In simple terms:

```text
Splunk search found the event.
        ↓
Sigma rule transformed the finding into a reusable detection.
        ↓
PySigma converted the detection into Splunk SPL.
        ↓
Splunk validation proved the detection worked against real BOTSv3 telemetry.
```

This process represents the core workflow used by Detection Engineers when transforming threat hunting discoveries into production-ready security detections.


---

# Conclusion

This detection demonstrates the complete lifecycle of modern detection engineering, from threat hunting and hypothesis validation through Sigma development, PySigma conversion, Splunk integration, detection tuning, and ATT&CK mapping.

The resulting detection provides visibility into a common attacker persistence technique and forms part of a broader SOC Detection Engineering portfolio built using real-world telemetry and investigation workflows.

