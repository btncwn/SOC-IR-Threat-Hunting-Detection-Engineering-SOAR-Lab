# 08 - Threat Intelligence

## Overview

Threat Intelligence enables security teams to identify, analyze, and respond to threats using indicators of compromise (IOCs), adversary tactics, techniques, and procedures (TTPs), and external intelligence sources.

This section demonstrates how threat intelligence can be operationalized within a SOC environment using Splunk, MISP, Sysmon telemetry, and the BOTS v3 dataset.

---

## Objectives

* Understand IOC-based detection and analysis
* Perform threat hunting using threat intelligence
* Correlate indicators across multiple data sources
* Enrich events using threat intelligence platforms
* Investigate malicious domains, IP addresses, and file hashes
* Map findings to MITRE ATT&CK techniques
* Document analyst investigations and findings

---

## Lab Environment

### Infrastructure

* Windows 7 Endpoint
* Kali Linux Attack Platform
* Splunk Enterprise
* Sysmon Telemetry
* MISP Threat Intelligence Platform

### Data Sources

* Sysmon Events
* Windows Event Logs
* Splunk Indexes
* BOTS v3 Dataset

---

## Investigation Scenarios

### Investigation 01 – Malicious Domain Analysis

Focus Areas:

* DNS Analysis
* HTTP Traffic Analysis
* IOC Enrichment
* Threat Intelligence Correlation
* MITRE ATT&CK Mapping

### Investigation 02 – Malicious IP Analysis

Focus Areas:

* Network Traffic Analysis
* IOC Correlation
* Threat Intelligence Validation
* Host Impact Assessment

### Investigation 03 – Malware Hash Analysis

Focus Areas:

* Sysmon Process Analysis
* Hash Investigation
* Malware Triage
* Threat Intelligence Enrichment

---

## Threat Intelligence Components

### IOC Enrichment

* Domains
* IP Addresses
* URLs
* File Hashes

### Threat Intelligence Sources

* MISP
* VirusTotal
* AbuseIPDB
* AlienVault OTX
* Open Source Intelligence (OSINT)

---

## Skills Demonstrated

* Threat Intelligence Analysis
* IOC Enrichment
* Threat Hunting
* Detection Engineering
* Splunk Investigation
* MISP Operations
* MITRE ATT&CK Mapping
* Incident Analysis

---

## Outcome

This section demonstrates how threat intelligence can be integrated into SOC workflows to improve detection, investigation, and response capabilities through the use of IOC enrichment, threat hunting, and structured analyst investigations.

