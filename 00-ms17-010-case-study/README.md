# MS17-010 (EternalBlue) – Full Adversary Emulation Case Study

## One-Sentence Summary

Discovered MS17-010 via Nessus, exploited it from Kali to Windows 7, captured Sysmon telemetry in Splunk, mapped to MITRE ATT&CK, and produced an incident report.

## Case Study Navigation (Click any link)

| Phase | Content | Link |
|-------|---------|------|
| 1. Vulnerability Discovery | Nessus scan findings | [01-nessus-scan-readme.md](./01-nessus-scan-readme.md) |
| 2. Attack Simulation | SMB enumeration from Kali | [02-attack-simulation-readme.md](./02-attack-simulation-readme.md) |
| 3. Endpoint Telemetry | Sysmon events | [03-sysmon-telemetry-readme.md](./03-sysmon-telemetry-readme.md) |
| 4. SIEM Detection | Splunk searches | [04-splunk-detection-readme.md](./04-splunk-detection-readme.md) |
| 5. MITRE ATT&CK Mapping | TTP mapping | [05-mitre-mapping-readme.md](./05-mitre-mapping-readme.md) |
| 6. Incident Response | Full IR investigation | [06-incident-response-readme.md](./06-incident-response-readme.md) |
| 7. Sigma Rule (Persistence) | Scheduled task detection | [07-sigma-rule-readme.md](./07-sigma-rule-readme.md) |
| 8. Sigma Rule (Lateral) | SMB lateral movement (NEW) | [08-sigma-rule-lateral-readme.md](./08-sigma-rule-lateral-readme.md) |

## Detection Coverage

| Phase | Detected? |
|-------|-----------|
| Vulnerability scan | ✅ |
| SMB enumeration | ⚠️ (manual, no alert) |
| Exploit execution | ✅ |
| Reverse shell | ✅ |
| Lateral movement | ✅ (new Sigma rule) |
| Persistence | ✅ |

**Overall Coverage: 83% (5 of 6 phases detected)**

## How to Present This in an Interview

> *"I built a complete MS17-010 emulation chain. I found the vulnerability with Nessus, exploited it with Metasploit, captured Sysmon telemetry in Splunk, mapped everything to MITRE ATT&CK, and wrote an incident report. My detection coverage is now 83% after adding a Sigma rule for lateral movement. The full case study is in my repo with direct links to every phase."*

## Last Updated

2026-06-07
