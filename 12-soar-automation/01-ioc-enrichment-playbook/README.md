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

# Multi-Source Enrichment Results

To validate the effectiveness of the IOC enrichment workflow, the SHA256 hash below was investigated across multiple threat intelligence platforms.

## Investigated IOC

```text
14b03ac41b5ef44ca31790fefb23968f2525c3aabfe11e96b9b1ccb6215eb8be
```

---

## Source 1 – MISP

### Result

Match Found

```text
Event ID: 1723
Report: OSINT - Space Pirates: analyzing the tools and connections of a new hacker group
Comment: MyKLoadClient
Category: Payload Delivery
Type: SHA256
```

### Assessment

The hash was associated with a threat intelligence report documenting activity linked to the Space Pirates threat actor.

MISP enrichment provided campaign context and malware-related intelligence that would not be visible through reputation-based searches alone.

Screenshot:

```text
02-misp-hash-enrichment.png
```

---

## Source 2 – Python MISP Automation

### Result

Match Found

The IOC was successfully enriched through a Python-based automation script using the MISP API and PyMISP.

Workflow:

```text
SHA256 Hash
        ↓
Python Script
        ↓
MISP API
        ↓
Threat Intelligence Result
```

The script automatically identified:

* Event ID
* Threat Intelligence Report
* Malware Component
* Threat Context

Screenshot:

```text
03-python-misp-enrichment.png
```

---

## Source 3 – VirusTotal

### Result

No security vendors flagged this file as malicious.

### Assessment

Although VirusTotal did not identify the hash as malicious, the absence of antivirus detections does not indicate the absence of risk.

Threat intelligence investigations frequently identify malware samples, tooling, and campaign infrastructure that may not be detected by commercial antivirus vendors.

Screenshot:

```text
04-virustotal-no-detection.png
```

---

## Source 4 – Hybrid Analysis

### Result

No results returned.

### Assessment

No behavioral analysis or sandbox reports were available for the sample.

This demonstrates a common challenge faced during investigations where intelligence may exist in one platform but not another.

Screenshot:

```text
05-hybrid-analysis-no-result.png
```

---

## Analyst Assessment

Results obtained from multiple intelligence sources:

| Source                 | Result       |
| ---------------------- | ------------ |
| MISP                   | Match Found  |
| Python MISP Automation | Match Found  |
| VirusTotal             | No Detection |
| Hybrid Analysis        | No Result    |

The investigation demonstrated that intelligence sources often provide different levels of visibility.

A single source should not be used as the sole basis for security decisions.

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
## Key Lesson

> Threat intelligence provides context. Telemetry provides evidence. Analyst judgment provides understanding.

The IOC was successfully identified within MISP threat intelligence data despite the absence of detections within VirusTotal and Hybrid Analysis.

This reinforces the importance of correlating intelligence from multiple sources rather than relying solely on reputation-based detections.
> Threat intelligence should support investigation, not replace analysis.
