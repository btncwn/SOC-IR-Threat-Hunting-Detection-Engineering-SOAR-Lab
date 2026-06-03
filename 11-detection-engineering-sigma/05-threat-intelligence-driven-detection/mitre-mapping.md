# MITRE ATT&CK Mapping

## Overview

Threat intelligence analysis of the Space Pirates campaign and PlugX RAT identified multiple attacker behaviors associated with execution, persistence, discovery, and service manipulation.

The following ATT&CK techniques were selected based on observed adversary capabilities and the detection opportunities available within the laboratory environment.

---

# ATT&CK Mapping Matrix

| ATT&CK ID | Technique                            | Tactic          | Detection Focus                             |
| --------- | ------------------------------------ | --------------- | ------------------------------------------- |
| T1059.001 | PowerShell                           | Execution       | Encoded and suspicious PowerShell activity  |
| T1053.005 | Scheduled Task                       | Persistence     | Creation of scheduled tasks                 |
| T1046     | Network Service Discovery            | Discovery       | Enumeration of listening ports and services |
| T1049     | System Network Connections Discovery | Discovery       | Inspection of active network connections    |
| T1018     | Remote System Discovery              | Discovery       | Enumeration of remote hosts                 |
| T1543.003 | Windows Service                      | Persistence     | Service creation and modification           |
| T1027     | Obfuscated Files or Information      | Defense Evasion | Encoded PowerShell and obfuscated commands  |

---

# Technique: T1059.001 - PowerShell

## Description

PowerShell is one of the most commonly abused Windows administration tools.

Threat actors use PowerShell to:

* Execute payloads
* Download malware
* Establish persistence
* Perform reconnaissance
* Execute encoded commands

## Detection Focus

```text
powershell.exe
-enc
-encodedcommand
IEX
-W hidden
```

## Related Sigma Rule

```text
powershell-encoded-command.yml
```

---

# Technique: T1053.005 - Scheduled Task

## Description

Scheduled tasks provide a reliable persistence mechanism and allow malware to execute automatically.

Threat actors frequently use:

```text
schtasks.exe
```

to create tasks that execute malicious payloads.

## Detection Focus

```text
schtasks.exe /Create
```

## Related Sigma Rule

```text
suspicious-scheduled-task.yml
```

---

# Technique: T1046 - Network Service Discovery

## Description

Attackers often enumerate listening ports and services after gaining access to a system.

Common tools include:

```text
netstat
findstr
```

## Detection Focus

```text
netstat -nao
LISTENING
```

## Related Sigma Rule

```text
network-enumeration.yml
```

---

# Technique: T1049 - System Network Connections Discovery

## Description

Adversaries inspect active network connections to identify communication paths and discover additional targets.

## Detection Focus

```text
netstat
network connections
open sessions
```

## Related Sigma Rule

```text
network-enumeration.yml
```

---

# Technique: T1018 - Remote System Discovery

## Description

Attackers identify other systems on the network to support lateral movement and post-compromise reconnaissance.

## Detection Focus

```text
Host enumeration
IP range scanning
Network discovery
```

## Related Sigma Rule

```text
service-discovery.yml
```

---

# Technique: T1543.003 - Windows Service

## Description

Threat actors frequently abuse Windows services to establish persistence or execute malware.

Common utilities include:

```text
sc.exe
```

## Detection Focus

```text
sc create
sc config
sc start
```

## Related Sigma Rule

```text
service-discovery.yml
```

---

# Key Detection Engineering Lesson

A central lesson from this project is:

> Hashes change. IPs change. Domains change. Behaviors persist.

For this reason, the project prioritizes behavioral ATT&CK-based detections rather than detections based solely on static indicators of compromise.

Behavior-focused detections provide greater resilience against attacker infrastructure changes and remain effective across multiple campaigns and malware variants.
