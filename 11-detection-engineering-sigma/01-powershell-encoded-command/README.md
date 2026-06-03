# Detection 01 – PowerShell Encoded Command

## Overview

This detection engineering project focuses on identifying suspicious PowerShell execution using encoded commands.

The detection was developed after observing PowerShell activity within the BOTSv3 dataset where `powershell.exe` executed with the `-enc` parameter and a long Base64-encoded command.

Encoded PowerShell is commonly used by attackers to hide command content, evade basic inspection, and execute payloads in a less readable format.

---

## Detection Objective

Detect PowerShell process creation events where the command line contains encoded command execution.

The detection focuses on:

* `powershell.exe`
* `-enc`
* `-encodedcommand`
* Long encoded command strings
* Suspicious parent-child process relationships

---

## Why This Detection Was Created

During analysis, Sysmon Event ID 1 recorded PowerShell executing with the `-enc` parameter.

Example evidence from the dataset:

```text
Time:
2018-08-20 12:57:15

Image:
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

CommandLine:
"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -enc aQBlAHgAIAAoAE4AZQB3...

ParentImage:
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
```

This behavior is suspicious because the command content is Base64 encoded and not immediately readable by an analyst. The event shows PowerShell launching another PowerShell process with an encoded payload, a technique frequently observed in malware execution and post-exploitation activity.

---

## Sigma Detection Logic

The Sigma rule searches for Windows process creation events where:

* The process image ends with `powershell.exe`
* The command line contains `-enc`
* The command line contains `-encodedcommand`

Sigma provides a portable detection format that can be converted into multiple SIEM query languages.

### Sigma Rule

```yaml
title: Suspicious PowerShell Encoded Command

id: 9f3b9c7e-0f1e-4c2a-9b7a-2f5a8b1d6c3e

status: experimental

description: Detects PowerShell execution using encoded commands.

logsource:
  product: windows
  category: process_creation

detection:
  selection:
    Image|endswith:
      - '\powershell.exe'
    CommandLine|contains:
      - '-enc'
      - '-encodedcommand'

  condition: selection

falsepositives:
  - Administrative scripts

level: medium
```

---

## PySigma Conversion

The Sigma rule was converted into Splunk SPL using PySigma.

Generated SPL:

```spl
Image="*\\powershell.exe" CommandLine IN ("*-enc*", "*-encodedcommand*")
```

This conversion demonstrates how Sigma can create SIEM-agnostic detections while automatically generating platform-specific search logic.

---

## Splunk Validation

The generated Sigma output did not immediately return results in BOTSv3 because Sysmon data was stored inside XML events and the required fields were not automatically extracted.

To validate the detection, field extraction was performed directly from `_raw` using `rex`.

Validated SPL:

```spl
index=botsv3 sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" "powershell.exe" "-enc"
| rex field=_raw "<Data Name='Image'>(?<Image>[^<]+)</Data>"
| rex field=_raw "<Data Name='CommandLine'>(?<CommandLine>[^<]+)</Data>"
| rex field=_raw "<Data Name='ParentImage'>(?<ParentImage>[^<]+)</Data>"
| search Image="*powershell.exe" CommandLine="*-enc*"
| table _time Image CommandLine ParentImage
```

---

## Detection Results

The detection successfully identified PowerShell executions containing encoded commands.

Observed activity included:

* PowerShell execution using `-enc`
* Long Base64 encoded payloads
* PowerShell spawning PowerShell
* Obfuscated command execution
* Suspicious command-line behavior

The identified event contained an encoded command that downloaded and executed content from an external source, a behavior commonly associated with malware delivery and command execution.

---

## MITRE ATT&CK Mapping

| Tactic              | Technique | Description                     |
| ------------------- | --------- | ------------------------------- |
| Execution           | T1059.001 | PowerShell                      |
| Defense Evasion     | T1027     | Obfuscated Files or Information |
| Command and Control | T1105     | Ingress Tool Transfer           |

---

## Validation Challenges

One of the main challenges encountered during validation was that the Sigma-generated SPL assumed fields such as:

```text
Image
CommandLine
ParentImage
```

were already extracted by Splunk.

However, within the BOTSv3 dataset these values existed inside raw Sysmon XML logs. As a result, additional field extraction was required before the detection could be validated.

This represents a realistic Detection Engineering scenario where portable detection logic must be adapted to the data structure of a specific environment.

---

## Detection Engineering Workflow

```text
Suspicious PowerShell activity observed
                ↓
Sysmon Event Identified
                ↓
Sigma Rule Created
                ↓
PySigma Conversion
                ↓
Splunk SPL Generated
                ↓
Field Extraction Challenge Identified
                ↓
BOTSv3 SPL Tuned
                ↓
Detection Validated
```

---

## Analyst Assessment

This project demonstrates the complete Detection Engineering lifecycle:

* Identifying suspicious behavior
* Creating a Sigma rule
* Converting the rule using PySigma
* Mapping fields to Splunk
* Tuning detections for the environment
* Validating detections against real telemetry

The detection successfully identified encoded PowerShell execution within the BOTSv3 dataset and demonstrates how Sigma can be used to build portable detections while still requiring environment-specific tuning and validation.

This project serves as a practical example of modern Detection Engineering workflows used by SOC analysts, Threat Hunters, and Detection Engineers.
