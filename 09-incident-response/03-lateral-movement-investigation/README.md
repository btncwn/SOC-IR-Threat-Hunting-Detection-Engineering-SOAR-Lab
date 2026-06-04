# Lateral Movement Investigation

## Overview

This project documents an Incident Response investigation into simulated lateral movement activity between a Windows host and a Kali Linux host.

The investigation focuses on identifying remote execution, validating Windows Event Log evidence, reviewing SSH activity, and assessing whether a reverse tunnel attempt succeeded.

---

## Scenario

A lateral movement scenario was simulated from Windows to Kali using SSH and remote command execution techniques.

A reverse tunnel was then attempted from Kali back to Windows to test persistence capability.

The reverse tunnel failed because Windows SSH password authentication was disabled.

This project demonstrates both attacker tradecraft and defensive configuration validation.

---

## Investigation Workflow

```text
Remote Access Observed
      ↓
Audit Policy Enabled
      ↓
Remote Command Executed
      ↓
Windows Event ID 4688 Reviewed
      ↓
SSH Activity Validated
      ↓
Reverse Tunnel Attempt Reviewed
      ↓
Defensive Control Confirmed
      ↓
Incident Response Assessment
```

---

## Evidence Collected

| Screenshot                                 | Description                                                             |
| ------------------------------------------ | ----------------------------------------------------------------------- |
| `01_auditpol_commands.png`                 | Audit policy enabled for Logon, Process Creation, and File Share events |
| `02_wmi_command.png`                       | WMI command execution using `Invoke-WmiMethod`                          |
| `03_event_4688_lateral_movement_proof.png` | Windows Event ID 4688 showing process creation evidence                 |
| `04_csv_report.png`                        | Exported CSV report containing Event ID 4688 data                       |
| `05_event_viewer_manual.png`               | Manual Event Viewer validation for Event ID 4688                        |
| `06_reverse_tunnel_attempt.png`            | Reverse SSH tunnel attempt from Kali to Windows                         |
| `07_netstat_listening.png`                 | Windows `netstat` output showing SSH connection                         |
| `08_kali_ssh_active.png`                   | Kali SSH service active and running                                     |
| `09_kali_ssh_active_who.png`               | `who` output showing Windows IP connected to Kali                       |

---

## Key Findings

### 1. Remote Command Execution

A command was executed remotely using WMI:

```text
Invoke-WmiMethod -Class Win32_Process -Name Create
```

This created process execution evidence on the Windows host.

---

### 2. Windows Event Log Evidence

Windows Security Event ID 4688 was used to validate process creation activity.

Event ID 4688 provided evidence of:

* Process creation
* Creator process context
* Target process details
* User and host context

---

### 3. SSH-Based Lateral Movement

SSH activity confirmed connectivity between Windows and Kali.

Kali `who` output showed a Windows source IP connected to the Kali host.

---

### 4. Reverse Tunnel Attempt

A reverse SSH tunnel was attempted from Kali back to Windows.

The attempt failed because Windows SSH password authentication was disabled.

This demonstrated the value of secure SSH configuration as a defensive control.

---

## Defensive Control Validated

```text
PasswordAuthentication no
```

This setting blocks password-based SSH authentication.

Key-based SSH authentication may still be allowed unless `PubkeyAuthentication no` is also configured.

---

## MITRE ATT&CK Mapping

| Technique                          | ID    | Description                              |
| ---------------------------------- | ----- | ---------------------------------------- |
| Remote Services                    | T1021 | Lateral movement using remote services   |
| Windows Management Instrumentation | T1047 | Remote process execution using WMI       |
| Protocol Tunneling                 | T1572 | Reverse tunnel attempt                   |
| Command and Scripting Interpreter  | T1059 | Command execution through shell activity |

---

## Incident Response Assessment

The investigation confirmed successful remote activity from Windows to Kali and collected supporting evidence from Windows Event Logs and Linux SSH activity.

The reverse tunnel attempt did not succeed because password authentication was disabled on the Windows SSH server.

This reduced the attacker's ability to establish persistence through password-based SSH access.

---

## Skills Demonstrated

* Incident Response
* Lateral Movement Investigation
* Windows Event Log Analysis
* Event ID 4688 Analysis
* SSH Activity Review
* WMI Investigation
* Defensive Control Validation
* MITRE ATT&CK Mapping

---

## Key Lesson

> Lateral movement detection requires correlating endpoint telemetry, authentication activity, process creation logs, and network session evidence.

The investigation showed that lateral movement activity can be identified through Event ID 4688, SSH session validation, and defensive configuration review.
