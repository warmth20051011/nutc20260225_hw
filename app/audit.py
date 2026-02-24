import logging
import json

logging.basicConfig(
    filename="audit.log",
    level=logging.INFO,
    format="%(message)s"
)

def log_tool_usage(role, tool_name, input_data):
    log_entry = {
        "role": role,
        "tool": tool_name,
        "input": input_data,
    }
    logging.info(json.dumps(log_entry))
