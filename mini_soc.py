# Mini SOC Framework

# Simulated logs (multi-stage attack)
logs = [
    "LOGIN FAILED - admin - 45.33.32.1",
    "LOGIN FAILED - admin - 45.33.32.1",
    "LOGIN SUCCESS - admin - 45.33.32.1",
    "PRIVILEGE ESCALATION - admin",
    "FILE ACCESS - sensitive_data.txt"
]

# Detection thresholds
THRESHOLD = 2

# Tracking variables
failed_attempts = 0
successful_login = False
privilege_escalation = False
data_access = False

# Alerts storage
alerts = []

# Process logs
for log in logs:

    # Detect failed logins
    if "LOGIN FAILED" in log:
        failed_attempts += 1

    # Detect successful login
    elif "LOGIN SUCCESS" in log:
        successful_login = True

    # Detect privilege escalation
    elif "PRIVILEGE ESCALATION" in log:
        privilege_escalation = True

    # Detect data access
    elif "FILE ACCESS" in log:
        data_access = True

# Apply detection rules

# Rule 1: Brute force
if failed_attempts >= THRESHOLD:
    alerts.append("[SOC] Brute force attack detected")

# Rule 2: Suspicious login
if successful_login and failed_attempts >= THRESHOLD:
    alerts.append("[SOC] Suspicious login detected")

# Rule 3: Privilege escalation
if privilege_escalation:
    alerts.append("[SOC] Privilege escalation detected")

# Rule 4: Data access
if data_access:
    alerts.append("[SOC] Sensitive data access detected")

# Correlation: Full attack chain
if (failed_attempts >= THRESHOLD and successful_login 
    and privilege_escalation and data_access):
    alerts.append("[CRITICAL] Full attack chain detected")

# Display report
print("=== MINI SOC REPORT ===\n")

for alert in alerts:
    print(alert)
