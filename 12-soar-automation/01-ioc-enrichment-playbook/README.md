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
* PT Expert Security Center

---

## Investigation Background

During development of a MISP enrichment automation workflow, a SHA256 hash was selected from Event 1723 for testing purposes.

Subsequent investigation revealed that the indicator was associated with MyKLoadClient and documented within a public threat intelligence report on the Space Pirates threat actor.

The exercise evolved from API testing into a threat intelligence correlation case study.

---

## Investigated IOC

```text
14b03ac41b5ef44ca31790fefb23968f2525c3aabfe11e96b9b1ccb6215eb8be
```

### Enrichment Workflow

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
      ↓
Analyst Assessment
```

---

# Source 1 – MISP Intelligence Enrichment

The SHA256 hash was searched within MISP using both manual investigation techniques and a Python-based automation script developed using PyMISP.

### Result

```text
Event ID: 1723

OSINT - Space Pirates:
Analyzing the Tools and Connections
of a New Hacker Group

Comment:
MyKLoadClient
```

### Assessment

The hash was associated with a threat intelligence report documenting activity linked to the Space Pirates threat actor.

MISP enrichment provided campaign context and malware-related intelligence that would not be visible through reputation-based searches alone.

### Screenshots

```text
01-misp-hash-enrichment.png
02-python-misp-enrichment.png
```

---

# Source 2 – Python MISP Automation

The IOC was successfully enriched through a Python-based automation script using the MISP API and PyMISP.

### Workflow

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

This demonstrated how threat intelligence enrichment can be automated to reduce analyst investigation time.

---

# Source 3 – External Intelligence Validation

To validate the intelligence obtained from MISP, the indicator was researched using additional intelligence platforms.

## VirusTotal

### Result

```text
No security vendors flagged this file as malicious.
```

### Assessment

Although VirusTotal did not identify the hash as malicious, the absence of antivirus detections does not indicate the absence of risk.

Threat intelligence investigations frequently identify malware samples, tooling, and campaign infrastructure that may not be detected by commercial antivirus vendors.

### Screenshot

```text
03-virustotal-no-detection.png
```

---

## Hybrid Analysis

### Result

```text
No results returned.
```

### Assessment

No behavioral analysis or sandbox reports were available for the sample.

This demonstrates a common challenge faced during investigations where intelligence may exist in one platform but not another.

### Screenshot

```text
04-hybrid-analysis-no-result.png
```

---

# Source 4 – PT Expert Security Center Correlation

Further investigation led to the discovery of a detailed threat intelligence report published by PT Expert Security Center (Positive Technologies):

```text
Space Pirates:
Analyzing the Tools and Connections
of a New Hacker Group
```

The report documented malware, infrastructure, and tradecraft associated with the Space Pirates threat actor.

Most importantly, the investigated SHA256 hash was directly listed within the report's IOC section under:

```text
MyKLoadClient
```

This independently validated the intelligence originally discovered through MISP enrichment.

Reference:

```text
https://global.ptsecurity.com/en/research/pt-esc-threat-intelligence/space-pirates-tools-and-connections/
```

### Screenshot

```text
05-space-pirates-ioc-confirmation.png
```

---

# Infrastructure Correlation

The PT Expert Security Center report also documented the use of PlugX malware within the Space Pirates ecosystem.

Researchers identified the following command-and-control infrastructure:

```text
micro.dns04.com
microft.dynssl.com
api.microft.dynssl.com
www.0077.x24hr.com
```

The report noted that this infrastructure directly intersected with MyKLoadClient command-and-control infrastructure.

This demonstrates how a single IOC can be used to pivot into broader malware families, campaign infrastructure, and threat actor activity.

---

# Final Analyst Assessment

| Source                           | Result        |
| -------------------------------- | ------------- |
| MISP                             | Match Found   |
| Python MISP Automation           | Match Found   |
| VirusTotal                       | No Detection  |
| Hybrid Analysis                  | No Result     |
| PT Expert Security Center Report | IOC Confirmed |

The investigation demonstrated the importance of correlating indicators across multiple intelligence sources.

A single hash value provided a path from IOC enrichment to malware analysis, infrastructure correlation, and threat intelligence validation.

While the investigation identified intelligence associated with the Space Pirates threat actor, it does not attribute activity within the BOTSv3 dataset to Space Pirates.

The project demonstrates intelligence correlation rather than threat attribution.

---

## Skills Demonstrated

* Threat Intelligence Enrichment
* IOC Analysis
* Security Operations
* Incident Triage
* Investigation Methodology
* Risk Assessment
* Python Automation
* MISP API Integration
* Intelligence Correlation
* Threat Intelligence Validation

---

## Key Lessons Learned

* Threat intelligence enrichment extends beyond reputation checks.
* Intelligence sources frequently provide different levels of visibility.
* Campaign context often provides greater value than individual indicators.
* Threat actor infrastructure can be identified through IOC pivoting.
* Python automation can significantly reduce enrichment time.
* Intelligence correlation improves analyst confidence during investigations.

> Threat intelligence provides context. Telemetry provides evidence. Analyst judgment provides understanding.

> Threat intelligence should support investigation, not replace analysis.

> Hashes change. IPs change. Domains change. Behaviors persist.
