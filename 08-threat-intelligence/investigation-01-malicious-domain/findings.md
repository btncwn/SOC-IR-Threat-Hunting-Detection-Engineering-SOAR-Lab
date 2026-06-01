# Findings

## Detection

During review of HTTP traffic within the BOTS v3 dataset, suspicious web application activity was identified targeting an AWS EC2-hosted web server.

The activity consisted of repeated HTTP requests from external source IP addresses attempting to access PHP files commonly associated with web shells, backdoors, and automated exploitation tools.

---

## Evidence

### Target Server

* Public IP: 34.227.100.38
* Internal IP: 172.16.0.109
* Hostname: ip-172-16-0-109.ec2.internal

### Top Source IPs

| Source IP    | Requests |
| ------------ | -------- |
| 61.75.35.114 | 55       |
| 45.7.231.174 | 41       |

### Observed PHP Filenames

* /cmd.php
* /ak47.php
* /qq.php
* /qaq.php
* /9678.php
* /data.php
* /db.init.php
* /db__.init.php
* /db_session.init.php

### HTTP Methods Observed

| Method   | Status | Count |
| -------- | ------ | ----- |
| POST     | 404    | 54    |
| GET      | 404    | 1     |
| PROPFIND | 503    | 1     |

---

## Source IP Analysis

The primary source IP address (61.75.35.114) generated repeated POST requests against numerous PHP files.

The naming convention of the requested files is consistent with web-shell discovery activity and automated scanning tools used by threat actors to identify previously compromised web servers.

Examples include:

* cmd.php
* ak47.php
* qq.php

The activity appears automated rather than interactive due to the number of requests and the sequential probing pattern.

---

## Target Analysis

The targeted system was identified as:

ip-172-16-0-109.ec2.internal

The server was hosted within an AWS EC2 environment and exposed web services over HTTP.

Observed activity suggests the attacker was attempting to locate known web shells or vulnerable PHP applications.

No successful access attempts were identified.

---

## Assessment

The activity is assessed as:

**Automated Web-Shell Discovery / Web Application Reconnaissance**

Evidence supporting this assessment includes:

* Multiple external source IPs
* Repeated POST requests
* Requests for suspicious PHP filenames
* WebDAV probing activity
* Consistent scanning behavior

All requests returned HTTP 404 responses indicating the requested resources were not present.

No evidence of successful compromise was observed during this investigation.

---

## MITRE ATT&CK Mapping

### TA0043 - Reconnaissance

* T1595 - Active Scanning

### TA0001 - Initial Access

* T1190 - Exploit Public-Facing Application

The observed behavior is consistent with adversaries identifying exposed web resources and attempting to locate vulnerable or previously compromised applications.

---

## Recommendations

1. Monitor public-facing web applications for unusual POST requests.
2. Alert on requests to common web-shell filenames.
3. Monitor WebDAV methods such as PROPFIND.
4. Implement Web Application Firewall (WAF) protections.
5. Review web server logs for additional scanning activity.
6. Block known malicious source IPs where appropriate.
