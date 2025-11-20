# backend/engine.py
import re

def detect_phishing(text):
    phishing_keywords = [
        "kyc", "update your account", "blocked", "verify", "login now",
        "click the link", "click here", "reset password",
        "account suspended", "urgent", "verify account"
    ]
    url_pattern = r"(http[s]?://\S+)"
    found_url = re.findall(url_pattern, text.lower())

    if any(k in text.lower() for k in phishing_keywords) or found_url:
        return True, found_url
    return False, None


def detect_scam(text):
    scam_patterns = [
        "you won", "lottery", "reward", "gift card", "prize", "cash bonus",
        "send your details", "claim now", "registration fee",
        "urgent money", "final notification"
    ]
    return any(word in text.lower() for word in scam_patterns)


def detect_extortion(text):
    extortion_patterns = [
        "i will leak", "send money", "pay me", "or else",
        "i will expose", "blackmail", "give me", "payment deadline"
    ]
    return any(word in text.lower() for word in extortion_patterns)


def detect_threat(text):
    threat_patterns = [
        "i will kill", "i'll kill", "hurt you", "beat you",
        "destroy you", "harm you"
    ]
    return any(word in text.lower() for word in threat_patterns)


def detect_abuse(text):
    abuse_words = [
        "idiot", "stupid", "useless", "loser", "bitch", "moron", "dumb",
        "worthless", "trash"
    ]
    return any(word in text.lower() for word in abuse_words)


def detect_bullying(text):
    bullying_patterns = [
        "no one likes you", "you should die", "everyone hates you",
        "you're a failure", "you are worthless"
    ]
    return any(word in text.lower() for word in bullying_patterns)


def detect_toxicity(text):
    toxic_patterns = [
        "go die", "kill yourself", "hate you", "disgusting ", "filthy"
    ]
    return any(word in text.lower() for word in toxic_patterns)


def analyze_text(text):
    text = text.lower()

    if detect_phishing(text)[0]:
        return "Phishing", "High"

    if detect_scam(text):
        return "Scam/Fraud", "High"

    if detect_extortion(text):
        return "Extortion / Blackmail", "High"

    if detect_threat(text):
        return "Threatening", "Medium"

    if detect_bullying(text):
        return "Cyberbullying", "Medium"

    if detect_abuse(text):
        return "Abusive / Harassment", "Medium"

    if detect_toxicity(text):
        return "Toxic / Hate Speech", "High"

    return "Safe", "Low"
