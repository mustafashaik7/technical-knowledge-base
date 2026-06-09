# Maintain Two GitHub Accounts Simultaneously Using SSH

## Objective

This article explains how to configure a local machine to work with two different GitHub accounts at the same time without repeatedly logging in and out.

The recommended approach is to use:

- Separate SSH keys for each GitHub account
- SSH host aliases in `~/.ssh/config`
- The correct Git remote URL for each repository
- Repository-level Git author identity settings

This avoids common permission errors such as:

```text
Permission to <account>/<repository>.git denied to <other-account>
fatal: unable to access '<repo-url>': The requested URL returned error: 403
```

---

## Account Naming Used in This Article

To keep this article reusable and safe for public documentation, the GitHub account names are generalized.

| Placeholder | Meaning |
|---|---|
| `GHAcc1` | First GitHub account, for example personal GitHub account |
| `GHAcc2` | Second GitHub account, for example work, client, training, or organization GitHub account |
| `repo-for-GHAcc1` | A repository owned by `GHAcc1` |
| `repo-for-GHAcc2` | A repository owned by `GHAcc2` |
| `github-ghacc1` | SSH host alias for `GHAcc1` |
| `github-ghacc2` | SSH host alias for `GHAcc2` |

Example mapping:

```text
GHAcc1 = your personal GitHub username
GHAcc2 = your second GitHub username
repo-for-GHAcc1 = any repository owned by GHAcc1
repo-for-GHAcc2 = any repository owned by GHAcc2
```

Do not use the literal placeholder names unless you intentionally want to. Replace them with your actual GitHub usernames and repository names when applying the commands.

---

## Why This Setup Is Needed

If you use HTTPS authentication or a single SSH key for multiple GitHub accounts, GitHub may authenticate you as the wrong account.

For example, you may try to push to a repository owned by `GHAcc1`, but your local Git credentials authenticate as `GHAcc2`. GitHub then rejects the push because `GHAcc2` does not have permission to write to `GHAcc1`'s repository.

The fix is to tell SSH exactly which key to use for each GitHub account.

---

## Recommended Solution

Use SSH aliases:

```text
github-ghacc1 -> GitHub account GHAcc1
github-ghacc2 -> GitHub account GHAcc2
```

Then use different remote URL formats depending on the repository owner:

```text
git@github-ghacc1:GHAcc1/repo-for-GHAcc1.git
git@github-ghacc2:GHAcc2/repo-for-GHAcc2.git
```

The alias after `git@` tells your machine which SSH key to use.

---

## Step 1: Create Separate SSH Keys

Create one SSH key for `GHAcc1`:

```bash
ssh-keygen -t ed25519 -C "GHAcc1@github" -f ~/.ssh/id_ed25519_ghacc1
```

Create another SSH key for `GHAcc2`:

```bash
ssh-keygen -t ed25519 -C "GHAcc2@github" -f ~/.ssh/id_ed25519_ghacc2
```

When prompted, you may add a passphrase. A passphrase is recommended for better security.

This creates files similar to:

```text
~/.ssh/id_ed25519_ghacc1
~/.ssh/id_ed25519_ghacc1.pub
~/.ssh/id_ed25519_ghacc2
~/.ssh/id_ed25519_ghacc2.pub
```

Important:

- `.pub` files are public keys and can be uploaded to GitHub.
- Files without `.pub` are private keys and must never be shared or committed to GitHub.

---

## Step 2: Add Both Keys to the SSH Agent

Start the SSH agent:

```bash
eval "$(ssh-agent -s)"
```

Add the first account key:

```bash
ssh-add ~/.ssh/id_ed25519_ghacc1
```

Add the second account key:

```bash
ssh-add ~/.ssh/id_ed25519_ghacc2
```

Verify loaded keys:

```bash
ssh-add -l
```

---

## Step 3: Add Public Keys to the Correct GitHub Accounts

Copy the public key for `GHAcc1`:

```bash
cat ~/.ssh/id_ed25519_ghacc1.pub
```

Add it to the `GHAcc1` GitHub account:

```text
GitHub -> Settings -> SSH and GPG keys -> New SSH key
```

Copy the public key for `GHAcc2`:

```bash
cat ~/.ssh/id_ed25519_ghacc2.pub
```

Add it to the `GHAcc2` GitHub account:

```text
GitHub -> Settings -> SSH and GPG keys -> New SSH key
```

Each public key must be added to the matching GitHub account.

---

## Step 4: Configure SSH Host Aliases

Open the SSH config file:

```bash
nano ~/.ssh/config
```

Add the following configuration:

```sshconfig
# GitHub account 1
Host github-ghacc1
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_ghacc1
  IdentitiesOnly yes

# GitHub account 2
Host github-ghacc2
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_ghacc2
  IdentitiesOnly yes
```

Set correct permissions:

```bash
chmod 600 ~/.ssh/config
```

### What This Configuration Means

| Field | Meaning |
|---|---|
| `Host github-ghacc1` | Local alias used in Git remote URLs for `GHAcc1` |
| `HostName github.com` | Actual GitHub SSH server |
| `User git` | Required SSH user for GitHub |
| `IdentityFile` | SSH private key to use for that account |
| `IdentitiesOnly yes` | Forces SSH to use the specified key only |

---

## Step 5: Test SSH Authentication

Test the first account:

```bash
ssh -T git@github-ghacc1
```

Expected result:

```text
Hi GHAcc1! You've successfully authenticated, but GitHub does not provide shell access.
```

Test the second account:

```bash
ssh -T git@github-ghacc2
```

Expected result:

```text
Hi GHAcc2! You've successfully authenticated, but GitHub does not provide shell access.
```

### Why GitHub Says "Does Not Provide Shell Access"

This is normal and not an error.

GitHub allows SSH access for Git operations such as:

- `git clone`
- `git pull`
- `git push`
- `git fetch`

GitHub does not allow an interactive server shell session over SSH. The message confirms that authentication worked, but shell access is not available.

---

## Step 6: Set the Correct Remote URL Per Repository

For a repository owned by `GHAcc1`, use:

```bash
git remote set-url origin git@github-ghacc1:GHAcc1/repo-for-GHAcc1.git
```

For a repository owned by `GHAcc2`, use:

```bash
git remote set-url origin git@github-ghacc2:GHAcc2/repo-for-GHAcc2.git
```

Verify the remote:

```bash
git remote -v
```

Expected for a `GHAcc1` repository:

```text
origin  git@github-ghacc1:GHAcc1/repo-for-GHAcc1.git (fetch)
origin  git@github-ghacc1:GHAcc1/repo-for-GHAcc1.git (push)
```

Expected for a `GHAcc2` repository:

```text
origin  git@github-ghacc2:GHAcc2/repo-for-GHAcc2.git (fetch)
origin  git@github-ghacc2:GHAcc2/repo-for-GHAcc2.git (push)
```

---

## Step 7: Push Code

For a `GHAcc1` repository:

```bash
git push -u origin main
```

For a `GHAcc2` repository:

```bash
git push -u origin main
```

The command is the same because the `origin` remote already determines which account and key are used.

If your branch is named `master`, use:

```bash
git push -u origin master
```

---

## Step 8: Configure Git Author Identity Per Repository

SSH authentication determines which GitHub account is allowed to push.

Git author configuration determines the name and email shown on commits.

Inside a repository owned by `GHAcc1`:

```bash
git config user.name "Your Name"
git config user.email "ghacc1-email@example.com"
```

Inside a repository owned by `GHAcc2`:

```bash
git config user.name "Your Name"
git config user.email "ghacc2-email@example.com"
```

Verify:

```bash
git config user.name
git config user.email
```

Use repository-level Git config instead of global config when you work with multiple accounts.

---

## Common Troubleshooting

### Problem: Permission denied to one account while authenticated as another

Example:

```text
Permission to GHAcc1/repo-for-GHAcc1.git denied to GHAcc2.
```

Cause:

The repository remote is using the wrong SSH alias or HTTPS credentials.

Fix:

```bash
git remote set-url origin git@github-ghacc1:GHAcc1/repo-for-GHAcc1.git
```

Then verify:

```bash
git remote -v
ssh -T git@github-ghacc1
```

---

### Problem: SSH asks for passphrase every time

Cause:

The private key has a passphrase and may not be stored in the SSH agent.

Fix:

```bash
ssh-add ~/.ssh/id_ed25519_ghacc1
ssh-add ~/.ssh/id_ed25519_ghacc2
```

On macOS, you can store the passphrase in Keychain:

```bash
ssh-add --apple-use-keychain ~/.ssh/id_ed25519_ghacc1
ssh-add --apple-use-keychain ~/.ssh/id_ed25519_ghacc2
```

---

### Problem: SSH uses the wrong key

Cause:

SSH may be trying multiple keys or not using the alias-specific key.

Fix:

Make sure `~/.ssh/config` includes:

```sshconfig
IdentitiesOnly yes
```

Then test with verbose output:

```bash
ssh -vT git@github-ghacc1
ssh -vT git@github-ghacc2
```

Look for the `Offering public key` line to confirm which key is being used.

---

### Problem: Remote still uses HTTPS

Check:

```bash
git remote -v
```

If you see this:

```text
https://github.com/GHAcc1/repo-for-GHAcc1.git
```

Change it to SSH:

```bash
git remote set-url origin git@github-ghacc1:GHAcc1/repo-for-GHAcc1.git
```

---

## Best Practices

- Use one SSH key per GitHub account.
- Use clear SSH aliases such as `github-personal` and `github-work`, or generalized aliases such as `github-ghacc1` and `github-ghacc2`.
- Never commit private SSH keys.
- Avoid using HTTPS for multiple GitHub accounts unless you are comfortable managing credential helpers and tokens.
- Set `user.name` and `user.email` at the repository level.
- Verify the active account with `ssh -T` before pushing.
- Use private repositories for sensitive notes or client-specific work.

---

## Quick Reference

### Test accounts

```bash
ssh -T git@github-ghacc1
ssh -T git@github-ghacc2
```

### Set remote for account 1

```bash
git remote set-url origin git@github-ghacc1:GHAcc1/repo-for-GHAcc1.git
```

### Set remote for account 2

```bash
git remote set-url origin git@github-ghacc2:GHAcc2/repo-for-GHAcc2.git
```

### Verify remote

```bash
git remote -v
```

### Push

```bash
git push -u origin main
```

---

## Summary

The best way to maintain two GitHub accounts simultaneously is to use separate SSH keys and SSH host aliases.

Use this pattern:

```text
git@github-ghacc1:GHAcc1/repo-for-GHAcc1.git
git@github-ghacc2:GHAcc2/repo-for-GHAcc2.git
```

This ensures each repository uses the correct GitHub account and avoids authentication conflicts between accounts.
