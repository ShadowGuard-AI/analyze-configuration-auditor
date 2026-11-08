![Intro scenery: a brass theodolite telescope close up aligned on the flag line, the white flags blurring in a straight row beyond it and one orange flag standing out of line at the right](intro-banner.png)

# analyze-configuration-auditor

![Wordmark banner: a green field at first light with a brass theodolite on its mahogany tripod at the centre, sighting along a straight row of white marker flags running to the horizon, one orange flag planted beside the line near the front](banner.png)

<p align="center"><img src="logo.png" alt="analyze-configuration-auditor logo: a brass theodolite straight on atop its mahogany tripod in a green field, its telescope level and one small orange marker flag planted in the grass beside the tripod foot" width="200"></p>

![Animated themed scene](scene.svg)

# analyze-configuration-auditor
Audits system configurations (e.g., SSH, Apache) against security best practices and flags deviations. Uses YAML/JSON configuration files for defining rules. - Focused on Data analysis and reporting

## Rules format

The first argument is a rules file in YAML or JSON. It must contain a top level `rules` list. An empty rules list is an error: the tool exits nonzero and writes no report, because no audit was performed.

Each rule is a mapping with four fields:

- `id`: a short identifier for the rule, for example `SSH-001`.
- `description`: what the rule requires, in plain text.
- `check`: the exact text to search for in the system configuration file. Lines that start with `#` are skipped, so a commented out setting does not count as a pass.
- `severity`: the severity label reported for the rule, for example `High`.

Example (YAML):

```yaml
rules:
  - id: SSH-001
    description: Root login is disabled
    check: "PermitRootLogin no"
    severity: High
```

A shipped rule set for OpenSSH server settings is included as `sshd_rules.yaml`, covering `PermitRootLogin`, `PasswordAuthentication`, and `PermitEmptyPasswords`. Run it with:

`python3 main.py sshd_rules.yaml /etc/ssh/sshd_config`

Operators can supply their own rules files in the same format for other systems, such as Apache.


![Major divider](sep-heavy.svg)

## Install
`git clone https://github.com/ShadowStrikeHQ/analyze-configuration-auditor`


![Minor divider](sep-light.svg)

## Usage
`./analyze-configuration-auditor [params]`


![Minor divider](sep-light.svg)

## Parameters
- `-h`: Show help message and exit
- `-o`: No description provided
- `-v`: Enable verbose logging.


![Minor divider](sep-light.svg)

## License
Copyright (c) ShadowStrikeHQ

> Pocket note: an empty rules list is an error. The tool exits nonzero and writes no report, because no audit was performed.
> Pocket note: lines that start with the hash character are skipped, so a commented out setting does not count as a pass. The parameter -o is listed with no description provided.
