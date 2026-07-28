#!/bin/bash
# Log user commands to a log file
# Called by the user_prompt_submit hook; receives user input on stdin

LOG_DIR="$HOME/ai-berkshire/logs"
LOG_FILE="$LOG_DIR/command-log.jsonl"
COUNTER_FILE="$LOG_DIR/.counter"

mkdir -p "$LOG_DIR"

# Read user input
PROMPT=$(cat)

# Skip empty input
[ -z "$PROMPT" ] && exit 0

# Timestamp accurate to the second
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Take the first 200 characters as the record (avoid overly long input)
PROMPT_SHORT=$(echo "$PROMPT" | head -c 200 | tr '\n' ' ' | tr '"' "'")

# Append to the log (JSONL format)
echo "{\"time\":\"$TIMESTAMP\",\"prompt\":\"$PROMPT_SHORT\"}" >> "$LOG_FILE"

# Counter
if [ -f "$COUNTER_FILE" ]; then
    COUNT=$(cat "$COUNTER_FILE")
else
    COUNT=0
fi
COUNT=$((COUNT + 1))
echo "$COUNT" > "$COUNTER_FILE"

# Emit a reminder every 10 commands (hook stdout is shown to Claude)
if [ $((COUNT % 10)) -eq 0 ]; then
    TOTAL=$(wc -l < "$LOG_FILE" | tr -d ' ')
    echo "[Command log] ${TOTAL} commands logged so far. Consider running /command-log to add background summaries for recent commands."
fi
