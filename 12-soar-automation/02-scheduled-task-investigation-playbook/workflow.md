# Scheduled Task Investigation Workflow

## Objective

Provide a repeatable analyst workflow for investigating suspicious scheduled task creation activity.

---

## Step 1 – Review Alert

Detection triggered:

```text
schtasks.exe /Create
```

Questions:

* What created the task?
* Who created the task?
* What command will execute?

---

## Step 2 – Analyze Parent Process

Identify the process responsible for launching:

```text
schtasks.exe
```

Examples:

```text
cmd.exe
powershell.exe
wmic.exe
```

Review command-line arguments and execution context.

---

## Step 3 – Investigate PowerShell Activity

Determine whether PowerShell was involved.

Review:

* CommandLine
* Encoded Commands
* Hidden Windows
* Download Activity
* Child Processes

---

## Step 4 – Assess Persistence

Determine whether the task provides persistence.

Questions:

* Does the task execute automatically?
* Does it run at startup?
* Does it run at logon?
* Does it execute under SYSTEM?

---

## Step 5 – Assign Risk

| Condition                  | Risk Impact |
| -------------------------- | ----------- |
| PowerShell Present         | Medium      |
| Hidden Execution           | Medium      |
| SYSTEM Context             | High        |
| Scheduled Task Persistence | High        |
| Encoded Commands           | High        |

---

## Step 6 – Analyst Decision

Possible outcomes:

### Close Alert

Activity determined to be legitimate administration.

### Continue Investigation

Additional host telemetry required.

### Escalate Incident

Evidence suggests persistence, malicious execution, or attacker activity.

---

## Investigation Summary

```text
PowerShell
      ↓
schtasks.exe
      ↓
/Create
      ↓
SYSTEM
      ↓
Hidden PowerShell
```

This workflow demonstrates how scheduled task detections can be transformed into structured SOC investigations supporting incident response and threat hunting operations.



# Scheduled Task Investigation Workflow

```text
SOC Alert
      ↓
Scheduled Task Created
      ↓
Command Line Review
      ↓
PowerShell Analysis
      ↓
Persistence Assessment
      ↓
Risk Scoring
      ↓
Analyst Decision
```

## Investigation Questions

### Was a scheduled task created?

```text
schtasks.exe /Create
```

### Was PowerShell involved?

```text
powershell.exe
```

### Was SYSTEM used?

```text
/ru system
```

### Was execution hidden?

```text
-W hidden
```

### Was code downloaded?

```text
DownloadString()
```

### Was code executed dynamically?

```text
IEX
```

## Possible Outcomes

### Low Risk

Legitimate administration.

### Medium Risk

Requires analyst review.

### High Risk

Potential persistence mechanism.

### Critical

Escalate for incident response.
