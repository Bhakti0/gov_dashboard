
import random

def monitor(prompt):
    log = {
        "prompt": prompt,
        "length": len(prompt),
        "contains_sensitive": any(w in prompt.lower() for w in ["password", "secret", "otp"])
    }
    return log

def risk_assessment(log):
    risk = 0
    if log["contains_sensitive"]:
        risk += 60
    if log["length"] > 200:
        risk += 20
    risk += random.randint(0, 20)
    return min(risk, 100)

def compliance_check(log, risk):
    rules = {
        "no_sensitive_data": not log["contains_sensitive"],
        "acceptable_risk": risk < 80
    }
    passed = all(rules.values())
    return {"rules": rules, "overall_pass": passed}

def governance_decision(prompt):
    log = monitor(prompt)
    risk = risk_assessment(log)
    compliance = compliance_check(log, risk)
    decision = "APPROVE" if compliance["overall_pass"] else "REJECT"
    return {
        "log": log,
        "risk_score": risk,
        "compliance_results": compliance,
        "final_decision": decision
    }
