# Investigation 04 – MISP Threat Intelligence Enrichment

## Overview

This investigation extends the findings from Investigation 03 by enriching a suspicious SHA256 hash using MISP.

During Investigation 03, the executable:

```text
C:\Windows\Temp\hdoor.exe
```

was identified executing from a temporary directory and performing internal network enumeration.

The investigation extracted the following SHA256 hash:

```text
99925199059EE049F7AEDA8904C2F5BDFBA86671FD7A5989BD60B72F26EF737C
```

The objective of this investigation is to determine whether the hash is known to threat intelligence sources, assess its reputation, and demonstrate how MISP can support SOC investigations through indicator enrichment and intelligence-driven analysis.

---

## Investigation Hypothesis

A suspicious executable identified during threat hunting may correspond to a known malicious indicator.

Threat intelligence enrichment may provide:

* Additional context
* Threat attribution
* Related indicators
* Detection opportunities
* Investigation leads




## Investigation Outcome

Threat intelligence enrichment was performed against indicators collected during Investigation 03.

The SHA256 hash associated with hdoor.exe was searched within MISP after enabling and synchronizing multiple threat intelligence feeds, including:

* CIRCL OSINT Feed
* Botvrij.eu OSINT Feed

Additional searches were performed using:

* SHA256 hash
* hdoor.exe
* hdoor

No matching events, attributes, malware families, campaigns, or threat actor references were identified.

### Assessment

The absence of matches across multiple threat intelligence sources indicates that the observed indicator was not present within the synchronized MISP intelligence feeds at the time of investigation.

This does not indicate that the executable is benign. Instead, it demonstrates a common investigative scenario in which threat intelligence enrichment does not provide attribution or reputation data for an observed indicator.

As a result, the investigation relied on behavioral evidence collected during Investigation 03, including:

* Encoded PowerShell execution
* Execution from a temporary directory
* Internal subnet enumeration
* Network service discovery activity
* SMB and SSH connectivity

### Analyst Conclusion

No threat intelligence matches were identified for the investigated hash or filename.

Behavioral telemetry remains the primary basis for assessing hdoor.exe as suspicious.

This investigation demonstrates that threat intelligence enrichment supports investigative workflows but should not be considered a replacement for endpoint, process, and network analysis.


## Investigation Outcome

Threat intelligence enrichment was performed against indicators collected during Investigation 03.

The SHA256 hash associated with hdoor.exe was searched within MISP following synchronization of the CIRCL OSINT feed.

Additional searches were performed using:

* hdoor.exe
* hdoor

No matching events, attributes, malware families, or threat actor references were identified.

As a result, no threat intelligence attribution could be established for the observed executable.

The investigation therefore relied on behavioral evidence collected through Sysmon, Cisco NVM telemetry, and Splunk analysis.

The absence of threat intelligence matches does not indicate benign activity. Instead, the executable should be treated as an unknown indicator requiring behavioral analysis and continued monitoring.


