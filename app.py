from flask import Flask, render_template, request, send_file
from io import BytesIO
from datetime import date

app = Flask(__name__)

def build_policy(org_name, industry, employees, email, devices, remote_work, backup, training):
    policy = f"""INFORMATION SECURITY POLICY
{org_name}
Generated on: {date.today().strftime('%d %B %Y')}

1. PURPOSE
This policy explains the minimum security practices that {org_name} must follow
to protect business information, systems, and devices.

2. SCOPE
This policy applies to all employees, contractors, temporary staff, and approved
third parties who access {org_name}'s information or technology resources.
Organisation type: {industry}
Approximate number of employees: {employees}

3. ACCESS CONTROL
- Each user must have an individual account. Account sharing is prohibited.
- Use strong, unique passwords and a password manager where possible.
- Enable multi-factor authentication (MFA) for email, administrator accounts,
  and important business services wherever available.
- Give users only the access required for their job.
- Remove or disable access promptly when a person leaves the organisation.

4. EMAIL AND INTERNET SAFETY
- Check the sender and destination before opening links or attachments.
- Never provide passwords or verification codes in response to unexpected
  messages.
- Report suspicious emails to the designated IT contact: {email}.
- Download software only from trusted and approved sources.

5. DEVICES AND SOFTWARE
- Approved devices: {devices}.
- Keep operating systems, applications, browsers, and security software updated.
- Lock screens when devices are unattended.
- Do not install unapproved applications or connect unknown USB devices.
- Lost or stolen devices must be reported immediately to {email}.

6. REMOTE WORK
{remote_work_text(remote_work)}

7. BACKUP AND RECOVERY
{backup_text(backup)}
- Backups should be protected from unauthorised access.
- Test restoration periodically and document the results.

8. SECURITY AWARENESS
{training_text(training)}
- Staff must report suspected phishing, malware, data loss, or unauthorised
  access immediately to {email}.

9. INCIDENT RESPONSE
If a security incident is suspected:
1. Report it immediately to {email}.
2. Do not delete relevant messages, files, or logs.
3. Disconnect an affected device from the network if safe to do so.
4. The responsible IT person should assess, contain, and document the incident.
5. Notify affected people and authorities when required by applicable law.

10. DATA HANDLING
- Collect and retain only information needed for legitimate business purposes.
- Share confidential information only with authorised recipients.
- Use approved secure methods when transferring sensitive information.
- Dispose of paper records and digital data securely when no longer needed.

11. POLICY REVIEW
The organisation should review this policy at least once a year and after a
significant security incident, technology change, or legal requirement change.

12. ACKNOWLEDGEMENT
All staff are expected to read, understand, and follow this policy.

Approved by: __________________________
Role: __________________________________
Date: __________________________________

IMPORTANT
This generated document is a starter template, not legal or compliance advice.
Have management and a qualified security professional review it and adapt it
to local laws, contracts, and the organisation's actual risks.
"""
    return policy

def remote_work_text(value):
    if value == "Yes":
        return ("Remote work is allowed. Staff must use trusted networks, secure "
                "home Wi-Fi with a strong password, and MFA. Avoid public Wi-Fi "
                "for sensitive work; if unavoidable, use an organisation-approved VPN.")
    return "Remote work is not currently authorised. Any exception requires written approval."

def backup_text(value):
    if value == "Daily":
        return "Important business data must be backed up daily."
    if value == "Weekly":
        return "Important business data must be backed up at least weekly."
    return "A regular backup schedule must be established and documented."

def training_text(value):
    if value == "Yes":
        return "Employees must complete security awareness training at onboarding and at least annually."
    return "The organisation should introduce basic security awareness training for all employees."

@app.route("/", methods=["GET", "POST"])
def index():
    policy = None
    if request.method == "POST":
        fields = {
            "org_name": request.form.get("org_name", "").strip(),
            "industry": request.form.get("industry", "").strip(),
            "employees": request.form.get("employees", "").strip(),
            "email": request.form.get("email", "").strip(),
            "devices": request.form.get("devices", "").strip(),
            "remote_work": request.form.get("remote_work", "No"),
            "backup": request.form.get("backup", "Weekly"),
            "training": request.form.get("training", "Yes"),
        }
        if all(fields[k] for k in ("org_name", "industry", "employees", "email", "devices")):
            policy = build_policy(**fields)
            return render_template("index.html", policy=policy, org_name=fields["org_name"])
        return render_template("index.html", error="Please complete all required fields.")
    return render_template("index.html", policy=policy)

@app.route("/download", methods=["POST"])
def download():
    policy = request.form.get("policy", "")
    if not policy:
        return "No policy content provided.", 400
    buffer = BytesIO(policy.encode("utf-8"))
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="security-policy.txt",
                     mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True)
