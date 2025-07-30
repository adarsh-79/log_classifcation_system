import re
from model.regex_patterns import patterns

def classify_with_regex(log_msg: str) -> str:
    for pattern in patterns:
        if re.search(pattern, log_msg):
            return patterns[pattern]
        if "nova" in log_msg and "HTTP" not in log_msg:
            return "Resource Usage"
    return None