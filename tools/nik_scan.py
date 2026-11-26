"""Legacy module name retained for compatibility.

The implementation performs local NID input-format checks only. It does not
look up, infer, generate, or return personal identity information.
"""

import re
from datetime import datetime


class NIDProcessor:
    ACCEPTED_LENGTHS = (10, 13, 17)

    def parse_nid(self, nid_number):
        raw_value = str(nid_number or "").strip()
        if not re.fullmatch(r"[0-9\s-]+", raw_value):
            return {
                "timestamp": datetime.now().astimezone().isoformat(timespec="seconds"),
                "target_nid": None,
                "status": "Invalid input",
                "identity_verified": False,
                "error": "NID input must contain digits, spaces, or hyphens only."
            }

        digits = re.sub(r"\D", "", raw_value)
        if not digits:
            return {
                "timestamp": datetime.now().astimezone().isoformat(timespec="seconds"),
                "target_nid": None,
                "status": "Invalid input",
                "identity_verified": False,
                "error": "No digits were provided."
            }

        masked = "*" * max(0, len(digits) - 4) + digits[-4:]
        recognized = len(digits) in self.ACCEPTED_LENGTHS
        return {
            "timestamp": datetime.now().astimezone().isoformat(timespec="seconds"),
            "target_nid": masked,
            "status": "Format check completed",
            "digit_count": len(digits),
            "recognized_common_length": recognized,
            "identity_verified": False,
            "notice": (
                "A recognized length is not proof that the NID is genuine or belongs "
                "to anyone. No government system or personal-data source was queried."
            )
        }

    def analyze_nid(self, nid_number):
        """Compatibility alias used by older callers."""
        return self.parse_nid(nid_number)


# Backward-compatible class alias; the public terminology is NID.
NIKProcessor = NIDProcessor
