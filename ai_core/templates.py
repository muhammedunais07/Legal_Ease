DOCUMENT_TEMPLATES = {

    "Freelance Work Contract": {
        "sections": [
            "Parties",
            "Scope of Work",
            "Payment Terms",
            "Confidentiality",
            "Intellectual Property",
            "Termination",
            "Dispute Resolution",
            "Signatures"
        ]
    },

    "Employment Agreement": {
        "sections": [
            "Parties",
            "Position and Duties",
            "Compensation",
            "Working Hours",
            "Leave",
            "Confidentiality",
            "Termination",
            "Signatures"
        ]
    },

    "Rental Agreement": {
        "sections": [
            "Parties",
            "Property Details",
            "Rental Period",
            "Rent and Deposit",
            "Maintenance",
            "Utilities",
            "Termination",
            "Signatures"
        ]
    },

    "Service Agreement": {
        "sections": [
            "Parties",
            "Services",
            "Fees and Payment",
            "Responsibilities",
            "Confidentiality",
            "Intellectual Property",
            "Termination",
            "Signatures"
        ]
    },

    "Non-Disclosure Agreement": {
        "sections": [
            "Parties",
            "Purpose",
            "Confidential Information",
            "Obligations",
            "Permitted Disclosure",
            "Duration",
            "Remedies",
            "Signatures"
        ]
    },

    "Partnership Agreement": {
        "sections": [
            "Partners",
            "Business Purpose",
            "Capital Contributions",
            "Profit and Loss Sharing",
            "Management",
            "Confidentiality",
            "Dissolution",
            "Signatures"
        ]
    },

    "Sales Agreement": {
        "sections": [
            "Parties",
            "Goods or Services",
            "Purchase Price",
            "Payment Terms",
            "Delivery",
            "Warranties",
            "Termination",
            "Signatures"
        ]
    },

    "Loan Agreement": {
        "sections": [
            "Parties",
            "Loan Amount",
            "Interest",
            "Repayment",
            "Late Payment",
            "Security",
            "Default",
            "Signatures"
        ]
    }
}


def get_template(document_type):

    return DOCUMENT_TEMPLATES.get(
        document_type,
        {
            "sections": [
                "Parties",
                "Purpose",
                "Terms and Conditions",
                "Responsibilities",
                "Termination",
                "Signatures"
            ]
        }
    )