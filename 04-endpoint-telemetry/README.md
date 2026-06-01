# Endpoint Telemetry Collection & Analysis

## Overview

This phase focused on collecting, forwarding, and analyzing endpoint telemetry from a Windows 7 SP1 x64 system using Sysmon and Splunk Enterprise.

The objective was to establish endpoint visibility, validate log collection pipelines, and generate telemetry suitable for threat hunting, detection engineering, and incident response activities.

---

## Lab Environment

### Endpoint

* Windows 7 Professional SP1 x64
* Sysmon Installed
* Splunk Universal Forwarder Installed

### Security Monitoring Platform

* Splunk Enterprise
* Custom SOC Dashboard

---

## Telemetry Collection Architecture

Windows endpoint activity was captured using Sysmon and forwarded to Splunk through the Splunk Universal Forwarder.

Telemetry sources included:

* Process Creation Events
* Process Termination Events
* Command-Line Activity
* PowerShell Execution
* Parent-Child Process Relationships
* System Process Activity

This provided detailed visibility into endpoint behavior and attack simulation activities performed throughout the lab.

---

## Telemetry Validation

Telemetry collection was validated through:

* Normal Windows operating system activity
* Administrative command execution
* PowerShell execution monitoring
* SMB enumeration exercises
* Attack simulation activities
* Service and process monitoring

All events were successfully ingested into Splunk and used for detection engineering and threat hunting workflows.

---

## Security Monitoring Outcomes

The collected endpoint telemetry enabled:

* Threat Hunting Investigations
* Process Activity Monitoring
* PowerShell Visibility
* Parent-Child Process Analysis
* Attack Timeline Construction
* SOC Dashboard Development
* Incident Investigation Workflows

---

## Evidence

The collected telemetry was analyzed and visualized through a custom Splunk SOC dashboard.

Evidence is provided in:

**SOC-Attack-Timeline-Dashboard.pdf**

The dashboard demonstrates:

* Sysmon Event Volume Monitoring
* Attack Timeline Visualization
* Process Activity Analysis
* Suspicious Process Monitoring
* Parent → Child Process Relationships
* PowerShell Execution Monitoring

---

## Security Value

Endpoint telemetry is one of the most valuable data sources available to SOC analysts.

By collecting detailed Sysmon events and forwarding them to Splunk, analysts gain visibility into attacker behavior, process execution chains, command activity, and potential indicators of compromise.

The telemetry collected during this phase served as the foundation for subsequent threat hunting, ATT&CK mapping, and incident response activities.

---

## Outcome

A complete endpoint telemetry pipeline was successfully implemented using Sysmon and Splunk Enterprise.

The generated telemetry provided the visibility required to support SOC monitoring, threat hunting, detection engineering, and DFIR investigations within the lab environment.



## Deployment Challenges on Legacy Windows 7

One of the most valuable lessons learned during this project was the difficulty of deploying modern security tooling on a legacy Windows 7 SP1 environment.

### Sysmon Deployment Challenges

Installing Sysmon on Windows 7 required additional troubleshooting due to the age of the operating system and the lack of modern security updates.

Challenges included:

* Legacy operating system compatibility issues
* Missing Microsoft updates
* Driver and service initialization troubleshooting
* Verification of successful event generation
* Validation of Sysmon Operational log collection

Additional testing was required to confirm that Sysmon events were being generated correctly and forwarded to the SIEM.

### Splunk Universal Forwarder Deployment Challenges

Deploying the Splunk Universal Forwarder on Windows 7 introduced further challenges due to the unsupported nature of the operating system.

Issues encountered included:

* Compatibility considerations with legacy Windows components
* Forwarder service configuration and validation
* WinEventLog collection troubleshooting
* XML event parsing challenges
* Verification of successful event transmission to Splunk Enterprise

Several iterations of testing and troubleshooting were required before endpoint telemetry was consistently visible within Splunk.

### Lessons Learned

While modern operating systems generally support security tooling with minimal effort, legacy environments often require additional troubleshooting and validation.

This experience highlighted the importance of:

* Endpoint telemetry validation
* Log pipeline verification
* Legacy system support considerations
* SIEM ingestion troubleshooting
* Security monitoring quality assurance

Successfully overcoming these challenges resulted in a fully operational telemetry pipeline consisting of:

Windows 7 Endpoint → Sysmon → Splunk Universal Forwarder → Splunk Enterprise → SOC Dashboard

