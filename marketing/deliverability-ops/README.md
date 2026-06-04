# /deliverability-ops - Email deliverability operations

Diagnosticheaza probleme de email deliverability: inbox placement, reputatie domeniu/IP, SPF/DKIM/DMARC, bounce-uri, spam complaints, list hygiene, warmup si compliance.

## Cand il folosesti

- Emailurile ajung in spam sau promotii.
- Open rate, click rate sau reply rate scad brusc.
- Pregatesti warmup sau crestere de volum.
- Vrei sa verifici infrastructura SPF/DKIM/DMARC si reputatia.
- Vrei un plan prudent de remediere pentru cold outreach, newsletter sau lifecycle email.

## Ce produce

- Diagnostic pe engagement, reputatie, infrastructura, lista si continut
- Infrastructure checklist
- Reputation/provider diagnosis
- List health review
- Remediation plan 48h / 7 zile / 30 zile
- Warmup/ramp plan
- Compliance checklist

## Compatibilitate

```yaml
compatibility: codex-and-claude-code
```

## Instalare Claude Code

```bash
cp marketing/deliverability-ops/skill.md ~/.claude/commands/deliverability-ops.md
```

## Instalare Codex

```bash
mkdir -p ~/.codex/skills/deliverability-ops
cp marketing/deliverability-ops/skill.md ~/.codex/skills/deliverability-ops/SKILL.md
```

## Sursa

Adaptat din [iannuttall/gtm-agents](https://github.com/iannuttall/gtm-agents) - Apache-2.0 License.
