# SPL Searches - Investigation 01

## Search 1 - Identify Frequently Accessed HTTP Sites

```spl
index=botsv3 sourcetype=stream:http
| stats count by site
| sort -count
| head 30
```

### Purpose

Identify frequently accessed websites and detect unusual IP-based destinations.

---

## Search 2 - Investigate Suspicious HTTP Site

```spl
index=botsv3 sourcetype=stream:http site="34.227.100.38:80"
| stats count by src_ip uri_path http_method status
| sort -count
```

### Purpose

Determine which source IPs interacted with the target site and identify suspicious URI requests.

---

## Search 3 - Identify Source IP Activity

```spl
index=botsv3 sourcetype=stream:http site="34.227.100.38:80"
| stats count by src_ip
| sort -count
```

### Purpose

Identify the most active source IPs targeting the web server.

---

## Search 4 - Enumerate Requested Files

```spl
index=botsv3 sourcetype=stream:http site="34.227.100.38:80"
| stats count by uri_path
| sort -count
```

### Purpose

Identify filenames requested by the attacker and detect web-shell discovery activity.

---

## Search 5 - Analyze HTTP Methods and Status Codes

```spl
index=botsv3 sourcetype=stream:http src_ip="61.75.35.114"
| stats count by http_method status
```

### Purpose

Validate scanning behavior and determine server responses.

---

## Search 6 - Investigate Source IP Across Dataset

```spl
index=botsv3 ("61.75.35.114" OR "45.7.231.174")
| stats count by sourcetype
| sort -count
```

### Purpose

Determine whether attacker IPs appear elsewhere in the environment.

---

## Search 7 - Identify Target Asset

```spl
index=botsv3 172.16.0.109
| stats count by host sourcetype
| sort -count
```

### Purpose

Identify the internal asset targeted during the activity.

---

## Search 8 - Identify Sites Hosted on Target Asset

```spl
index=botsv3 sourcetype=stream:http dest_ip=172.16.0.109
| stats count by site
| sort -count
```

### Purpose

Determine which web services were hosted on the target server.

```
```
