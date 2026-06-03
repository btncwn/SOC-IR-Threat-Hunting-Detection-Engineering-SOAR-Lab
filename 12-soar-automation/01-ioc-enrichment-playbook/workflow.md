# IOC Enrichment Workflow

## Purpose

This workflow provides SOC analysts with a repeatable process for enriching indicators of compromise and determining whether escalation is required.

---

# Trigger

An alert contains one or more indicators:

* IP Address
* Domain
* URL
* SHA256 Hash
* Hostname

Example:

```text
14b03ac41b5ef44ca31790fefb23968f2525c3aabfe11e96b9b1ccb6215eb8be
```

---

# Step 1 – Extract IOC

Review the alert and record all indicators.

Required Evidence:

* Alert ID
* IOC Value
* Alert Time
* Affected Host
* Associated User

Checklist:

```text
☐ IOC documented
☐ Alert documented
☐ Initial notes recorded
```

---

# Step 2 – Classify IOC

Identify the indicator type.

| Type       | Example             |
| ---------- | ------------------- |
| IP Address | 8.8.8.8             |
| Domain     | example.com         |
| URL        | https://example.com |
| SHA256     | a1b2c3...           |
| Hostname   | workstation-01      |

The IOC type determines which enrichment sources should be queried.

---

# Step 3 – Search MISP

Search the IOC in MISP.

Collect:

* Event ID
* Threat Level
* Tags
* Related Attributes
* Associated Campaigns

Checklist:

```text
☐ MISP searched
☐ Event reviewed
☐ Relevant findings documented
```

---

# Step 4 – Search Additional Intelligence Sources

Review:

* VirusTotal
* AbuseIPDB
* AlienVault OTX
* Internal Intelligence Sources

Collect:

* Reputation Information
* Detection Counts
* Threat Actor References
* Malware Associations

Checklist:

```text
☐ External enrichment completed
☐ Findings documented
```

---

# Step 5 – Review Local Telemetry

Validate whether the IOC appears within the environment.

Sources:

* Splunk
* Sysmon
* Windows Event Logs

Questions:

* Was the IOC observed?
* Which host generated the activity?
* Which process was involved?
* Which user account was involved?

Checklist:

```text
☐ Telemetry reviewed
☐ Relevant events identified
☐ Evidence collected
```

---

# Step 6 – Risk Assessment

Determine risk level.

| Risk     | Criteria                       |
| -------- | ------------------------------ |
| Low      | No malicious evidence          |
| Medium   | Suspicious activity            |
| High     | Confirmed malicious indicators |
| Critical | Active compromise observed     |

---

# Step 7 – Analyst Decision

### Close Alert

Conditions:

* Benign activity confirmed
* No malicious evidence identified

### Continue Investigation

Conditions:

* Additional evidence required
* Inconclusive intelligence results

### Escalate Incident

Conditions:

* IOC confirmed malicious
* Supporting telemetry observed
* Threat activity verified

---

# Investigation Outcome

Document:

* IOC Investigated
* Intelligence Sources Used
* Evidence Collected
* Risk Level
* Final Decision

---

# Analyst Note

Threat intelligence provides context.

Telemetry provides evidence.

Effective investigations require both.

```text
Threat Intelligence
        +
Telemetry
        +
Analyst Judgment
        =
Investigation Outcome
```

