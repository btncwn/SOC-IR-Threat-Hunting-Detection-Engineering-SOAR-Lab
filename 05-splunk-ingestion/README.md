# Log Ingestion & SIEM Pipeline

## Overview

This phase focused on collecting Windows endpoint telemetry and successfully ingesting it into Splunk Enterprise for security monitoring and analysis.

The objective was to establish a reliable SIEM pipeline capable of receiving, parsing, indexing, and searching Sysmon-generated security events.


## Architecture

Windows 7 Endpoint
↓
Sysmon
↓
Splunk Universal Forwarder
↓
Splunk Enterprise
↓
SOC Dashboard & Threat Hunting

## Environment

### Endpoint

* Windows 7 Professional SP1 x64
* Sysmon Installed
* Splunk Universal Forwarder Installed

### SIEM Platform

* Splunk Enterprise
* Local Deployment (macOS)


## Data Sources

The following telemetry was collected and forwarded:

### Sysmon Operational Logs

Source:

Microsoft-Windows-Sysmon/Operational

Key Event Types:

* Event ID 1 – Process Creation
* Event ID 2 – File Creation Time Change
* Event ID 3 – Network Connections
* Event ID 5 – Process Termination


## Ingestion Challenges

One of the most significant challenges encountered during the project was ingesting Sysmon XML events from a legacy Windows 7 environment.

### Legacy Operating System Constraints

Windows 7 introduced compatibility and telemetry collection challenges including:

* Legacy event logging behavior
* Unsupported operating system limitations
* Sysmon deployment validation
* Forwarder configuration troubleshooting

### XML Parsing Issues

Although events were successfully reaching Splunk, many important fields were not automatically extracted.

Examples included:

* Image
* ParentImage
* CommandLine
* EventID

Initial searches returned incomplete results despite thousands of events being present.

### Field Extraction Troubleshooting

To solve this issue, custom extraction techniques were used during searches.

Examples included:

* EventID extraction
* Image extraction
* Parent process extraction
* Command-line extraction

This enabled meaningful threat hunting and dashboard creation.

## Telemetry Validation

The ingestion pipeline was validated by confirming:

* Successful Sysmon event collection
* Forwarding to Splunk Enterprise
* Event indexing
* Search visibility
* Dashboard population

More than 18,988 Sysmon events were successfully indexed and analyzed.
## Ingestion Validation

Sysmon telemetry generated on the Windows 7 endpoint was successfully forwarded to Splunk Enterprise using the Splunk Universal Forwarder.

Data ingestion was validated by confirming the presence of Sysmon Operational events within Splunk.

### Evidence

![Splunk Sysmon Ingestion Validation](screenshots/01-splunk-sysmon-ingestion-validation.png)
---

## Detection Engineering Benefits

The completed ingestion pipeline enabled:

* Threat Hunting
* Process Monitoring
* PowerShell Monitoring
* Attack Timeline Analysis
* Parent-Child Process Analysis
* SOC Dashboard Development


## Lessons Learned

Building a SIEM pipeline in a legacy Windows environment required significantly more troubleshooting than expected.

The project demonstrated the importance of:

* Data validation
* Field extraction verification
* Log pipeline troubleshooting
* Endpoint telemetry quality assurance

A successful ingestion pipeline is the foundation of effective threat detection and security monitoring.

## Outcome

A fully operational Windows telemetry pipeline was established using Sysmon, Splunk Universal Forwarder, and Splunk Enterprise.

The environment successfully generated, forwarded, indexed, and visualized endpoint telemetry, enabling subsequent threat hunting and SOC monitoring activities.
