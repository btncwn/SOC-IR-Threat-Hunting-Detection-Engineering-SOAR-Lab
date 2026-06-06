# Lab Architecture

## Overview

This section documents the design and architecture of the Security Operations Center (SOC) lab environment used throughout this portfolio.

The environment was built to support Detection Engineering, Threat Hunting, Incident Response, Threat Intelligence, Vulnerability Assessment, and SOAR Automation activities.

The lab combines Windows and Linux systems, centralized logging, endpoint telemetry, threat intelligence platforms, and security monitoring technologies.

---

## Architecture Components

### Monitoring Platform

* Splunk Enterprise
* Splunk Universal Forwarder
* Sysmon

### Endpoint Systems

* Windows 7
* Windows 11

### Attack Platform

* Kali Linux

### Vulnerability Management

* Nessus Essentials

### Threat Intelligence Platform

* MISP
* Docker
* Docker Compose


## Data Flow

                Windows 7 + Sysmon
                         ↓
              Splunk Universal Forwarder
                         ↓
                   Splunk Enterprise
                         ↑
                         │
                    BOTSv3 Dataset
                         │
                         ↓
      ┌───────────────────────────────────┐
      │ Threat Hunting                    │
      │ Detection Engineering             │
      │ Incident Response                 │
      │ SOC Investigations                │
      └───────────────────────────────────┘
                         ↑
                         │
                       MISP
                         ↑
                         │
             Threat Intelligence Sources



## Security Capabilities

The architecture supports:

* Centralized Log Collection
* Endpoint Telemetry Monitoring
* Threat Hunting
* Vulnerability Assessment
* Threat Intelligence Enrichment
* MITRE ATT&CK Mapping
* Detection Engineering
* Security Investigations
* Incident Response Workflows
* SOAR Automation


## Purpose

The objective of the architecture is to provide a realistic SOC environment for developing practical cybersecurity skills and conducting hands-on security investigations.

The platform serves as the foundation for all projects contained within this portfolio.


