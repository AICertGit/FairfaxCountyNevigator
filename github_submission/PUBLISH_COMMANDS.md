# Publish Commands

Use these after review and after confirming no secrets are present.

## Initialize Git

```bash
git init
git branch -M main
git remote add origin https://github.com/AICertGit/FairfaxCountyNevigator.git
```

## Review Files

```bash
git status --short
git diff --stat
```

## Secret Scan

```bash
rg -n "OPENAI_API_KEY|GOOGLE_API_KEY|AIza|sk-|Bearer|private_key" .
```

## Commit

```bash
git add .
git commit -m "Prepare Fairfax Resource Navigator demo submission"
```

## Push

```bash
git push -u origin main
```

If GitHub authentication is not configured on this machine, Git will prompt for browser or token-based authentication depending on the installed Git credential manager.
