# DevBox Monitor

A lightweight Python module that collects CPU and memory metrics for DevBoxes,
detects runaway processes, and sends email alerts when CPU usage exceeds 80%
for more than 2 minutes.

## Features

- Register DevBoxes with owner email.
- Collect metrics (CPU %, memory) with timestamps.
- Detect sustained high CPU (>80%) over 2 minutes.
- Send email alerts via local SMTP server.
- Retain metrics for 30 days; older metrics are cleaned up.

## Usage
