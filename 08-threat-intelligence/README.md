# 08 - Threat Intelligence

## Overview

Threat Intelligence is the process of collecting, analyzing, and applying information about adversaries, indicators of compromise (IOCs), and attack techniques to improve detection and response capabilities.

This section demonstrates how threat intelligence can be operationalized within Splunk using both lab-generated telemetry and the BOTS v3 dataset.

The goal is to identify suspicious indicators, enrich events with threat intelligence data, and support investigations through IOC correlation and threat hunting activities.

---

## Objectives

* Understand IOC-based threat detection
* Analyze malicious IP addresses, domains, URLs, and file hashes
* Correlate threat intelligence with Splunk data
* Practice threat hunting using BOTS v3 data
* Perform IOC enrichment workflows
* Build analyst investigation procedures
* Simulate real-world SOC threat intelligence operations

---

## Lab Environment

### Data Sources

* Windows 11 Endpoint
* Sysmon Telemetry
* Splunk Enterprise
* MISP Threat Intelligence Platform
* BOTS v3 Dataset

### Threat Intelligence Sources

* MISP
* AlienVault OTX
* AbuseIPDB
* VirusTotal
* Open Source Intelligence (OSINT)

---

## IOC Categories

### Network Indicators

* Malicious IP Addresses
* Command and Control (C2) Infrastructure
* Suspicious Domains
* Malicious URLs

### Host Indicators

* File Hashes
* Registry Artifacts
* Suspicious Processes
* Persistence Mechanisms

### Email Indicators

* Malicious Senders
* Phishing Domains
* Malicious Attachments

---

# IOC Enrichment Workflow

1. Detect suspicious activity
2. Extract indicators
3. Query threat intelligence sources
4. Enrich Splunk events
5. Assess risk
6. Investigate affected systems
7. Document findings
8. Escalate or remediate

---

# BOTS v3 Threat Intelligence Investigation

## Scenario

An analyst receives an alert indicating suspicious outbound network communication from a workstation.

The objective is to:

* Identify suspicious destinations
* Extract indicators
* Validate indicators against threat intelligence
* Determine attack scope
* Document findings

---

## Example IOC Hunting Searches

### Suspicious External Connections

```spl
index=botsv3
| stats count by src_ip dest_ip
| sort -count
```

### DNS Activity

```spl
index=botsv3 sourcetype=stream:dns
| stats count by query
| sort -count
```

### HTTP Requests

```spl
index=botsv3 sourcetype=stream:http
| stats count by uri_host
| sort -count
```

### File Hash Investigation

```spl
index=botsv3
| search hash=*
| stats count by hash
```

### Threat Intelligence Correlation

```spl
index=botsv3
| lookup malicious_ips.csv ip AS dest_ip
OUTPUT threat_name confidence
| search threat_name=*
```

---

# Splunk Threat Intelligence Lookups

## malicious_ips.csv

Example:

```csv
ip,threat_name,confidence
185.220.101.1,TOR Exit Node,High
45.95.147.236,Known Malware Infrastructure,High
```

## malicious_domains.csv

Example:

```csv
domain,threat_name,confidence
evil-domain.com,C2 Domain,High
malicious-update.net,Malware Hosting,High
```

## malicious_hashes.csv

Example:

```csv
hash,malware_family
44d88612fea8a8f36de82e1278abb02f,EICAR
```

---

# MISP Integration

## Goals

* Import threat feeds
* Create custom events
* Store IOC intelligence
* Share indicators across investigations
* Support IOC enrichment workflows

## Example Workflow

1. Create IOC in MISP
2. Export IOC
3. Import into Splunk lookup
4. Correlate against telemetry
5. Generate alert
6. Investigate affected assets

---

# Investigation Notes

For each IOC investigation record:

* Detection Time
* Analyst Name
* Indicator Type
* Indicator Value
* Threat Intelligence Source
* Risk Level
* Impacted Assets
* Investigation Findings
* Recommended Actions

---

# Key Skills Demonstrated

* Threat Intelligence Analysis
* IOC Enrichment
* Splunk Threat Hunting
* MISP Operations
* Indicator Correlation
* Investigation Documentation
* SOC Analyst Workflow
* Detection Engineering

---

## Outcome

This project demonstrates how threat intelligence can be integrated into a SOC workflow to enrich telemetry, improve detection accuracy, and accelerate incident response through IOC-based investigations and threat hunting activities.
