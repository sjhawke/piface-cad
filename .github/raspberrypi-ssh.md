Raspberry Pi SSH MCP server

This file documents the `raspberrypi-ssh` MCP server configuration for this repository and how to provide credentials safely.

Host and user to use for this project (provided by you):
- Host: 192.168.1.88
- User: pi

Recommended secrets to create in GitHub repository settings (Settings → Secrets and variables → Actions):
- RPI_SSH_PRIVATE_KEY — the private SSH key (contents of ~/.ssh/id_ed25519). Mark as secret.
- RPI_SSH_HOST — hostname or IP (optional; can be set to 192.168.1.88).
- RPI_SSH_USER — SSH user (optional; set to `pi`).

Local development using a .env file (recommended for local runs, not CI):
- Create a file named `.env` in your local clone and add the variables you need (example below). Add `.env` to your local `~/.gitignore_global` or the repo `.gitignore` so it is never committed.

Example .env for password-based auth:
RPI_SSH_HOST=192.168.1.88
RPI_SSH_USER=pi
RPI_SSH_PASSWORD=your_pi_password

Example .env for key-based auth (preferred):
RPI_SSH_HOST=192.168.1.88
RPI_SSH_USER=pi
# do NOT paste the private key value; instead point to the private key file
RPI_SSH_PRIVATE_KEY_PATH=$HOME/.ssh/id_ed25519

To load the .env for a local session:
- bash/zsh: `set -a; source .env; set +a`
- or use a tool like `direnv` or `dotenv` to load env vars automatically.

Notes:
- CI workflows cannot read your local `.env`; use GitHub Secrets for Actions.
- Avoid storing raw private keys in `.env` files; prefer pointing to a local key file and using ssh-agent.

Recommended steps:
1. Generate an SSH key pair locally (ed25519 recommended):
   ssh-keygen -t ed25519 -C "your_email@example.com"
2. Copy the public key to the Pi:
   ssh-copy-id -i ~/.ssh/id_ed25519.pub pi@192.168.1.88
3. Verify you can SSH without a password:
   ssh pi@192.168.1.88
4. Paste the private key into RPI_SSH_PRIVATE_KEY in GitHub Secrets (do not commit it into the repo).

Sample GitHub Actions workflow (see .github/workflows/raspberrypi-ssh.yml) will use the private key to run commands on the Pi for hardware-in-the-loop testing or to run pytest on device.

Security notes:
- Never commit private keys or passwords into source.
- Limit who can edit repository secrets in GitHub and rotate keys if they are exposed.
- Prefer key-based auth and consider disabling password auth on the Pi once keys are installed.
