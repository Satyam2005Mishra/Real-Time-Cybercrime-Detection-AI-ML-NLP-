# backend/advice.py

advice_map = {
    "Phishing": {
        "avoid": [
            "Do NOT click any links",
            "Do NOT share OTP, PIN, or passwords",
            "Verify directly on the official portal",
        ],
        "steps": [
            "Change your password immediately",
            "Enable 2-factor authentication",
            "Report to cybercrime.gov.in",
            "Contact your bank and block card/UPI",
        ]
    },
    "Scam/Fraud": {
        "avoid": [
            "Ignore messages claiming rewards or money",
            "Do NOT share bank details",
            "Avoid unknown job or prize offers",
        ],
        "steps": [
            "Collect screenshots",
            "Report at cybercrime.gov.in",
            "Inform your bank if money was lost",
        ]
    },
    "Extortion / Blackmail": {
        "avoid": [
            "Do NOT respond",
            "Do NOT send money",
        ],
        "steps": [
            "Keep all screenshots/evidence",
            "File a complaint on cybercrime.gov.in",
            "Inform local police if threat is serious",
        ]
    },
    "Threatening": {
        "avoid": [
            "Do NOT engage with the sender",
            "Block immediately",
        ],
        "steps": [
            "Inform police if threat is severe",
            "Report on platform",
        ]
    },
    "Cyberbullying": {
        "avoid": [
            "Do not reply emotionally",
            "Block the bully",
        ],
        "steps": [
            "Report to platform",
            "Talk to trusted person",
        ]
    },
    "Abusive / Harassment": {
        "avoid": [
            "Avoid replying",
            "Do NOT escalate the conversation",
        ],
        "steps": [
            "Save screenshots",
            "Block sender and report",
        ]
    },
    "Toxic / Hate Speech": {
        "avoid": [
            "Avoid responding",
        ],
        "steps": [
            "Report to platform",
        ]
    },
    "Safe": {
        "avoid": [],
        "steps": ["Message looks safe 😊"]
    }
}
