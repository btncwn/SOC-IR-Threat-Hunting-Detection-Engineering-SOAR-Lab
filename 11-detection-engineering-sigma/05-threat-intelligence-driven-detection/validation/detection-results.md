# Detection Validation Results

## Objective

The purpose of this phase was to validate threat intelligence driven detections against telemetry available within the BOTSv3 dataset.

Rather than relying solely on successful matches, the validation process focused on determining whether the developed Sigma rules could be translated into Splunk SPL and applied against available telemetry.

---

# Validation Methodology

The following workflow was used:

```text
Threat Intelligence
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

Each detection was converted into Splunk SPL using PySigma and reviewed against available data sources.

---

# Detection 1 – Encoded PowerShell Execution

## ATT&CK

```text
T1059.001 - PowerShell
T1027 - Obfuscated Files or Information
```

## Detection Logic

```text
powershell.exe
      +
-enc
      OR
-encodedcommand
```

## Validation Result

The rule was successfully converted into Splunk SPL using PySigma.

Detection logic was reviewed against available process creation telemetry.

Status:

```text
VALIDATED
```

---

# Detection 2 – Scheduled Task Persistence

## ATT&CK

```text
T1053.005 - Scheduled Task
```

## Detection Logic

```text
powershell.exe
        ↓
schtasks.exe
        ↓
/Create
```

## Validation Result

This behavior was previously validated during scheduled task persistence analysis.

Observed activity included:

```text
PowerShell
        ↓
schtasks.exe /Create
        ↓
SYSTEM Execution
        ↓
Hidden PowerShell
```

Status:

```text
VALIDATED
```

---

# Detection 3 – Network Enumeration

## ATT&CK

```text
T1046 - Network Service Discovery
T1049 - System Network Connections Discovery
T1018 - Remote System Discovery
```

## Detection Logic

```text
netstat
findstr
LISTENING
```

and

```text
IP Range Enumeration
```

## Validation Result

The detection logic aligns with previously observed network discovery activity identified during threat hunting.

Status:

```text
VALIDATED
```

---

# Detection 4 – Service Discovery and Manipulation

## ATT&CK

```text
T1543.003 - Windows Service
T1047 - Windows Management Instrumentation
```

## Detection Logic

```text
sc.exe
wmic.exe
```

combined with:

```text
query
create
config
start
```

operations.

## Validation Result

PySigma conversion completed successfully and generated valid Splunk SPL.

Status:

```text
VALIDATED
```
## Scheduled Task Persistence Validation

The detection was validated against the BOTSv3 dataset using the following search:

```spl
index=botsv3 "schtasks.exe" "/Create" "IEX"

---

# Key Finding

A major lesson from this project was that intelligence-driven behavioral detections are often more durable than detections based solely on indicators of compromise.

Many indicators such as:

* IP addresses
* Domains
* File hashes

change frequently.

Behavioral detections remain effective because they focus on attacker actions rather than attacker infrastructure.

---


# Detection Engineering Conclusion

The project successfully transformed threat intelligence associated with the Space Pirates threat actor and PlugX RAT into reusable Sigma detections.

The resulting detections were converted into Splunk SPL using PySigma and validated against available telemetry sources.

This workflow demonstrates how threat intelligence can be operationalized into practical detection content suitable for SOC monitoring, threat hunting, and detection engineering programs.
