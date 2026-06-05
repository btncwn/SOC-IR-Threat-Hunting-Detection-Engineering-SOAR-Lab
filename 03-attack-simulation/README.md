# Attack Simulation

## SMB Enumeration and Service Discovery

A controlled attack simulation was performed from the Kali Linux attack host against the Windows target system.

### Investigation Evidence

![SMB Enumeration and Service Discovery](screenshots/01-smb-enumeration-and-service-discovery.png)

### Findings

The scan identified SMB-related services exposed on the target system.

### MITRE ATT&CK Mapping

| Technique | ID |
|------------|------|
| Network Service Discovery | T1046 |
| Remote Services | T1021 |# Attack Simulation – SMB Enumeration & Exposure Validation

## Overview

Following a credentialed Nessus vulnerability assessment, a controlled attack simulation was performed against a Windows 7 SP1 x64 endpoint.

The objective of this phase was to validate exposed services, identify attack surface characteristics, and generate realistic telemetry for SOC monitoring and threat hunting exercises.

---

## Lab Environment

### Attacker System

* Kali Linux

### Target System

* Windows 7 Professional SP1 x64
* Sysmon Installed
* Splunk Universal Forwarder Installed

### Monitoring Platform

* Splunk Enterprise

---

## Reconnaissance Activities

The following enumeration activities were performed from the Kali Linux workstation:

### SMB Service Discovery

SMB enumeration confirmed that the target exposed TCP/445 and provided operating system fingerprinting information.

Key findings:

* Operating System: Windows 7 Professional SP1 x64
* SMB Service Accessible
* SMBv1 Enabled
* SMB Signing Disabled

Observed Output:

```text
Windows 7 Professional SP1 x64
(signing: False)
(SMBv1: True)
```

### Anonymous SMB Enumeration

Anonymous SMB access testing was performed to identify available shares and assess exposure.

### RPC Enumeration Testing

RPC enumeration was attempted to evaluate remote information disclosure opportunities.

### Web Service Validation

HTTP connectivity validation was performed to identify additional exposed services.

---

## Security Observations

The enumeration phase identified multiple characteristics commonly associated with legacy Windows environments:

* SMBv1 enabled
* SMB signing disabled
* Windows 7 end-of-life operating system
* Exposed SMB service on TCP/445

These findings significantly increase attack surface exposure and align with vulnerabilities identified during the Nessus assessment.

---

## Relationship to Vulnerability Assessment

During the vulnerability assessment phase, Nessus identified the host as vulnerable to:

* MS17-010 (EternalBlue)
* WannaCry-related SMB vulnerabilities
* Multiple critical Microsoft security update deficiencies

The SMB enumeration results validated the exposed service configuration associated with these findings.

---

## Detection Engineering Value

This activity generated realistic reconnaissance telemetry that can be monitored using:

* Sysmon Process Creation Events
* PowerShell Activity Monitoring
* Network Connection Events
* Splunk Threat Hunting Queries
* SOC Dashboard Visualizations

---

## Evidence

### SMB Enumeration Results

screenshots/smb-enumeration-and-service-discovery.png

---

## Outcome

The attack simulation successfully validated the exposed SMB attack surface of the Windows 7 target and provided supporting evidence for the critical vulnerabilities identified during the Nessus assessment.

The generated telemetry was subsequently collected by Sysmon and analyzed through Splunk dashboards and threat hunting workflows.

