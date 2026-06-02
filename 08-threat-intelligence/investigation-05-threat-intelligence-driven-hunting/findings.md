# Findings

## Summary

Threat intelligence driven hunting was performed using indicators and behavioral observations collected during previous investigations.

The hunt focused on activity associated with:

* hdoor.exe
* PowerShell execution
* Internal network reconnaissance
* Host discovery behavior

---

## Key Findings

### Encoded PowerShell Activity

PowerShell execution was identified using encoded command parameters.

This behavior is commonly associated with script obfuscation, automated execution, and attacker tradecraft.

---

### Suspicious Process Creation

The executable:

C:\Windows\Temp\hdoor.exe

was observed executing from a temporary directory.

Execution from temporary directories is frequently associated with attacker tooling, staging activity, or unauthorized software execution.

---

### Internal Network Discovery

Command-line analysis revealed evidence of internal network enumeration activity.

Observed behavior included:

* Host discovery
* Network reconnaissance
* Service identification

This activity aligns with common Discovery techniques documented within the MITRE ATT&CK framework.

---

### Network Activity

Cisco Network Visibility Module (NVM) telemetry recorded outbound connections associated with hdoor.exe.

Observed activity included communication with internal systems over SSH-related network traffic.

---

## Analyst Assessment

Although threat intelligence enrichment did not produce attribution or known-malware matches, behavioral evidence identified activity consistent with internal reconnaissance and discovery operations.

The combination of:

* Encoded PowerShell execution
* Temporary directory execution
* Internal network discovery
* Network connectivity

supports continued investigation and monitoring.

---

## Conclusion

This investigation demonstrates a threat intelligence driven hunting methodology in which indicators and behavioral observations are used to proactively search telemetry for suspicious activity.

The investigation successfully identified multiple behaviors associated with attacker discovery techniques and validated the effectiveness of intelligence-guided threat hunting.
