# IOC Enrichment Playbook

## Overview

This project demonstrates a Security Operations Center (SOC) workflow for enriching Indicators of Compromise (IOCs) using threat intelligence sources.

The objective is to reduce analyst investigation time by collecting intelligence from multiple sources and transforming raw indicators into actionable security context.

Rather than manually researching every IOC, analysts follow a structured enrichment process to determine risk, prioritize investigations, and support incident response activities.

---

## Why IOC Enrichment Matters

Modern SOCs process large numbers of alerts containing:

* IP Addresses
* Domains
* URLs
* File Hashes
* Hostnames

Without additional context, these indicators provide limited value.

Threat intelligence enrichment allows analysts to determine:

* Whether an IOC is known malicious
* Whether it is associated with malware
* Whether it is linked to threat actor activity
* Whether it has appeared in previous investigations
* Whether escalation is required

---

## Playbook Workflow

```text
SOC Alert
      ↓
IOC Extraction
      ↓
Threat Intelligence Lookup
      ↓
Context Collection
      ↓
Risk Assessment
      ↓
Analyst Decision
      ↓
Escalate / Continue Investigation / Close
```

---

## Intelligence Sources

### Current Lab Sources

* MISP
* CIRCL OSINT Feed
* Botvrij.eu Feed

### Common Industry Sources

* VirusTotal
* AbuseIPDB
* AlienVault OTX
* URLHaus
* MalwareBazaar

---

## Example Investigation

Indicator:

```text
14b03ac41b5ef44ca31790fefb23968f2525c3aabfe11e96b9b1ccb6215eb8be
```

Enrichment Process:

```text
IOC Identified
      ↓
Threat Intelligence Lookup
      ↓
Intelligence Correlation
      ↓
Behavior Analysis
      ↓
Risk Assessment
```

The investigation demonstrated that threat intelligence provides context, but analyst judgment remains critical.

---

## Skills Demonstrated

* Threat Intelligence Enrichment
* IOC Analysis
* Security Operations
* Incident Triage
* Investigation Methodology
* Risk Assessment
* SOC Workflow Design

---

## Key Lesson

> Threat intelligence should support investigation, not replace analysis.

Indicators may change over time, but understanding attacker behavior provides longer-term defensive value.
