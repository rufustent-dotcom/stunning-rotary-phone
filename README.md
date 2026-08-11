<div align="center">
<img width="1200" height="475" alt="GHBanner" src="https://ai.google.dev/static/site-assets/images/share-ais-513315318.png" />
</div>

# Rotary Phone World

An interactive Next.js app that lets you spin a virtual rotary phone dial — click any digit to "dial" it, and learn fun facts about the history of rotary phones.

## Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Frufustent-dotcom%2Fstunning-rotary-phone&root-directory=app)

The `vercel.json` at the repo root configures Vercel to use the `app/` directory as the project root.

## Run Locally

**Prerequisites:** Node.js

```bash
cd app
npm install
npm run dev
```

Then open [http://localhost:3000](http://localhost:3000).

## Project Structure

```
app/           Next.js web app (Rotary Phone World UI)
vercel.json    Vercel deployment configuration
*.py           Python simulation scripts (signal / mapping / deployment pipeline)
```

## Python Simulation

The repository also contains a Python-based signal-to-fleet orchestration simulation:

```bash
python greed.py --asset GREED --ticks 50
```
