# Executive Summary

A Sysmon Event ID 1 process creation event triggered the Sigma detection for suspicious scheduled task creation via PowerShell.

Investigation identified a PowerShell process spawning schtasks.exe and creating a scheduled task configured to execute with SYSTEM privileges.

The task configuration included hidden PowerShell execution and the use of Invoke-Expression (IEX), both of which are commonly associated with malicious persistence and defense evasion techniques.

The event was assessed as a high-confidence persistence mechanism requiring further investigation.

---

# Detection Trigger

The detection was triggered by the following process relationship:

PowerShell
        ↓
schtasks.exe
        ↓
Scheduled Task Creation

The activity matched all Sigma detection conditions:

✓ Parent Process = powershell.exe

✓ Child Process = schtasks.exe

✓ Command Line contains /Create

Detection Status:

VALIDATED

---

# Technical Analysis

## Process Creation

Sysmon Event ID 1 recorded execution of:

C:\Windows\System32\schtasks.exe

The command line contained:

schtasks.exe /Create /F /RU system /SC DAILY /ST 18:45 /TN Updater

Analysis confirmed creation of a scheduled task configured to:

- Execute daily
- Run as SYSTEM
- Persist across user logoff and system restart
- Operate independently of the initiating user session

---

## PowerShell Execution

The scheduled task was configured to launch:

powershell.exe

Observed parameters included:

-NonI
-W hidden
IEX(...)

These parameters indicate an attempt to execute PowerShell code without user visibility.

Particularly concerning was the presence of:

IEX

which is frequently used by attackers to execute dynamically generated or downloaded PowerShell content.

---

# Adversary Tradecraft Assessment

From an ATT&CK perspective, the activity demonstrates characteristics commonly associated with attacker persistence.

The observed execution chain enables:

PowerShell
      ↓
Task Creation
      ↓
SYSTEM Execution
      ↓
Persistence

An attacker successfully deploying this technique could maintain execution capability even after user logoff or system reboot.

The use of hidden PowerShell execution further increases confidence that the activity was designed to avoid user awareness.

---

# Detection Validation

Validation confirmed all Sigma conditions were satisfied:

| Condition | Result |
|------------|---------|
| ParentImage = powershell.exe | PASS |
| Image = schtasks.exe | PASS |
| CommandLine contains /Create | PASS |

The detection successfully identified the target behavior within the BOTSv3 dataset.

---

# Risk Assessment

Risk Level: HIGH

Reasons:

- Scheduled task creation
- Execution as SYSTEM
- Hidden PowerShell execution
- Invoke-Expression usage
- Persistence mechanism established

Potential Impact:

- Long-term persistence
- Privilege abuse
- Payload execution
- Defense evasion

---

# Incident Response Considerations

If observed within a production environment, the following actions would be recommended:

1. Identify the created scheduled task.
2. Review task action and payload.
3. Determine task creation source.
4. Investigate PowerShell command history.
5. Review additional persistence mechanisms.
6. Assess endpoint for signs of compromise.
7. Validate whether the activity was authorized.

---

# MITRE ATT&CK Mapping

Persistence

T1053.005 – Scheduled Task

Execution

T1059.001 – PowerShell

Defense Evasion

T1027 – Obfuscated Files or Information

Privilege Escalation

Potentially Present – Requires Additional Investigation

---

# Analyst Conclusion

This event represents a high-confidence detection of suspicious scheduled task creation initiated through PowerShell.

The combination of scheduled task creation, SYSTEM-level execution, hidden PowerShell execution, and Invoke-Expression usage significantly increases the likelihood of malicious intent.

The event demonstrates how process creation telemetry can be leveraged to identify persistence mechanisms and highlights the value of Sigma-based detection engineering combined with ATT&CK-driven analysis.
