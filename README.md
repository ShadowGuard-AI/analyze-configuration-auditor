![The bench before work: an open gouge roll with one pocket empty and one tool out on the wood](intro-banner.png)

# analyze-configuration-auditor

*The Linocut Artist's Gouge Roll: five tools in their pockets, each one named by the cut it must make.*

![Wordmark banner](banner.png)

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
