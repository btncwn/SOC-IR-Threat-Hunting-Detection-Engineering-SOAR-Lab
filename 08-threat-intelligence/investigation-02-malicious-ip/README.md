# Investigation 02 – Malicious IP Analysis

## Overview

This investigation was intended to identify and analyze potentially malicious IP address activity within the BOTSv3 dataset.

The objective was to develop threat intelligence investigation workflows, validate suspicious network communications, and enrich identified IP addresses using threat intelligence sources.


## Investigation Approach

The following activities were performed:

* Review of network telemetry within the BOTSv3 dataset
* Analysis of HTTP and DNS activity
* Identification of external source IP addresses
* Threat intelligence enrichment planning
* IOC investigation workflow development

## Findings

During the initial review of the BOTSv3 dataset, no sufficiently validated malicious IP activity was identified for a full investigation.

Several external IP addresses were observed during network analysis; however, the available evidence did not provide enough confidence to classify them as confirmed malicious indicators.

As a result, a formal malicious IP investigation was not completed at this stage.

## Lessons Learned

This activity highlighted the importance of validating indicators before classifying them as malicious.

Threat intelligence investigations should be evidence-driven and supported by multiple data sources whenever possible.

## Next Steps

Future investigations will revisit malicious IP analysis using:

* Additional BOTSv3 datasets
* Threat intelligence enrichment through MISP
* VirusTotal and external intelligence sources
* IOC correlation techniques
* Splunk-based threat hunting workflows

The goal is to develop a complete malicious IP investigation demonstrating identification, enrichment, validation, and analyst assessment processes.

## Status

**Current Status:** Research and Planning Complete

**Future Status:** Investigation to be expanded as additional threat intelligence data and validated indicators become available.

