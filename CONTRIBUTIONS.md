# mp-mini-ctf-2k27

## Overview

This project is one of the mini-projects for the 2026–2027 season. It involves creating mini CTF challenges for the Shellmates yearly mini-CTF. Contributing to this project is required to join the club.

### Membership Requirements

To become an official Shellmates member, you must submit **at least 3 approved challenges** to this repository.

### Challenge Guidelines

- **Difficulty Range:** Very easy to easy
- **Target Audience:** Newbies and beginner participants
- **LLM Usage:** Participants are not allowed to use large language models, so you don't need to worry about making challenges that can't be solved using them

---

## Getting Started

### Initial Setup

1. **Fork the repository** on GitHub

2. **Clone your fork** (SSH recommended for faster operations):
   ```bash
   git clone git@github.com:${your_username}/mp-mini-ctf-2k27.git
   ```

   Or using HTTPS:
   ```bash
   git clone https://github.com/${your_username}/mp-mini-ctf-2k27.git
   ```

3. **Configure the upstream repository**:
   ```bash
   git remote add upstream git@github.com:Shellmates/mp-mini-ctf-2k27.git
   ```

   Or using HTTPS:
   ```bash
   git remote add upstream https://github.com/Shellmates/mp-mini-ctf-2k27.git
   ```

4. **Sync with upstream**:
   ```bash
   git pull upstream main
   git push origin main
   ```

---

## Contributing a Challenge

### Workflow

Follow these steps for each challenge you create:

1. **Get approval from your mentors** for your challenge idea before implementation

2. **Sync with upstream** (do this every time before starting work):
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

3. **Create a feature branch** with the naming convention:
   ```bash
   git checkout -b {difficulty}-{category}-{challenge_name}
   ```

   Example: `easy-web-sql_injection`

4. **Implement your challenge** in the appropriate directory

5. **Stage your changes**:
   ```bash
   git add /path/to/challenge_directory
   ```

6. **Commit with a descriptive message**:
   ```bash
   git commit -m "Add {difficulty} {category} challenge: {challenge_name}"
   ```

7. **Push to your fork**:
   ```bash
   git push origin {difficulty}-{category}-{challenge_name}
   ```

8. **Create a pull request** on GitHub targeting the appropriate team branch

### Branch Naming Convention

Use lowercase with hyphens:
```
{difficulty}-{category}-{challenge_name}
```

**Examples:**
- `easy-crypto-caesar_cipher`
- `veryeasy-forensics-hidden_message`
- `easy-pwn-buffer_overflow`

---

## Challenge Requirements

When creating your challenge, ensure you include:

- **Challenge files** (source code, binaries, etc.)
- **Solution/writeup** with step-by-step explanation
- **Flag** in the format: `shellmates{flag_here}`
- **Flags** must be at least 12 bytes (without counting the flag format) and should not be guessable
- **challenge.yaml** with challenge description and any setup instructions
- **Dockerfile** (if your challenge requires a remote instance)

---

## Categories

There are no limitations on what categories you can create challenges for. Make challenges in categories you feel comfortable with. You don't have to stick to only one category. You are free to make challenges in whatever category you like.

**Available categories:** crypto, forensics, misc, rev, pwn, web and osint

**Note:**
- The `misc` category includes: AI, jails, etc.
- Steganography is not something we are looking for

---

## For Team Leaders

Team leaders are responsible for merging pull requests to the `team_{number}` branch (e.g., `team_1`, `team_2`, etc.).

---

## Important Notes

### Getting Help
- Tag your team mentors for any questions or clarifications
- Use descriptive PR titles and descriptions to facilitate review

### Docker/Instance Requirements
If your challenge requires a running instance or Docker container, inform your mentors early. We might organize a Docker workshop for those who have never used it.

### Best Practices
- Always pull from upstream before starting new work
- Test your challenges thoroughly before submitting
- Write clear, concise challenge descriptions
- Avoid making the challenge unclear. Use hints in descriptions when needed
- Include all necessary files in your PR
- Be responsive to feedback during code review

---

## Questions?

Don't hesitate to reach out to your team mentors if you need guidance on:
- Challenge ideas and approval
- Technical implementation
- Git workflow
- Docker setup
- General contribution questions
