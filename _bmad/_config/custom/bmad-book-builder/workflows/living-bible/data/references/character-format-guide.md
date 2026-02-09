# Character Format Guide

## Standard Character Entry Format

This reference shows the complete structure for character entries in the living bible.

## Template

```markdown
### [Character Name]

**Phase psychologique actuelle:** [X/5] ([Phase Name])

**Émotions dominantes:**
- [Emotion 1]
- [Emotion 2]
- [Emotion 3]

**Croyances actuelles:**
- Sur lui-même: [Belief about self]
- Sur le monde: [Belief about world]
- Sur les autres: [Belief about others]

**Relations:**
| Avec | Nature | Intensité | Évolution |
|------|--------|-----------|-----------|
| [Character] | [type] | [low/medium/high] | [direction] |

**Arc en cours:**
- Défini: [Start state] → [End state]
- Position: [percentage] (description)
- Dernière progression: [when last change occurred]
- Prochaine étape: [what needs to happen next]

**Dernière apparition:** [Chapter/Event]
**Prochaine apparition prévue:** [Chapter/Event] (optional)
```

## Field Definitions

### Phase Psychologique Actuelle
The character's current position on the 1-5 psychological scale.
- Format: `[X/5] ([Phase Name])`
- Example: `3/5 (Point de bascule)`
- See `character-phases.md` for complete phase definitions

### Émotions Dominantes
List the 2-4 emotions currently driving the character's behavior.
- Focus on feelings affecting decisions and actions
- Update when psychological phase changes
- Be specific (not just "sad" but "guilt-ridden", "hopeful", etc.)

### Croyances Actuelles
Track core beliefs across three dimensions:
- **Sur lui-même:** Self-concept and identity
- **Sur le monde:** Understanding of how reality works
- **Sur les autres:** Expectations of people

Update when character's worldview shifts.

### Relations Table
Document the character's connections to others:

| Column | Description | Values |
|--------|-------------|--------|
| Avec | Related character | Name |
| Nature | Relationship type | Alliance, Rivalry, Romance, Familial, etc. |
| Intensité | Strength of bond | Low, Medium, High |
| Évolution | Direction of change | Croissante, Stable, Décroissante |

**Critical:** All relationships must be bidirectional. If A→B exists, B→A must also exist.

### Arc en Cours
Track the character's transformation journey:
- **Défini:** The thematic arc (e.g., "Méfiance → Confiance")
- **Position:** Where they are (percentage and description)
- **Dernière progression:** When last significant change occurred
- **Prochaine étape:** What must happen next for arc to advance

### Apparition Tracking
- **Dernière apparition:** Last chapter/event where character appeared
- **Prochaine apparition prévue:** When character is expected to appear next (optional but helpful)

## Example: Complete Character Entry

```markdown
### Marc

**Phase psychologique actuelle:** 3/5 (Point de bascule)

**Émotions dominantes:**
- Doute croissant sur son leadership
- Culpabilité envers Chen (blessure)
- Attraction conflictuelle envers Julie

**Croyances actuelles:**
- Sur lui-même: "Je dois protéger le groupe, même contre leur volonté"
- Sur le monde: "Les ressources sont rares, la survie exige des choix durs"
- Sur les autres: "La confiance est un luxe qu'on ne peut pas se permettre"

**Relations:**
| Avec | Nature | Intensité | Évolution |
|------|--------|-----------|-----------|
| Élise | Conflit de leadership | Haute | Croissante |
| Julie | Attraction + Alliance | Moyenne | En développement |
| Chen | Loyauté mise à l'épreuve | Haute | Fragilisée |

**Arc en cours:**
- Défini: Individualisme → Collectivisme
- Position: 40% (milieu de transformation)
- Dernière progression: Jour 50 (sacrifice pour Chen)
- Prochaine étape: Accepter l'aide d'Élise

**Dernière apparition:** Chapitre 12
**Prochaine apparition prévue:** Chapitre 14
```

## New Character Template

When introducing a new character:

```markdown
### [New Character Name]

**Phase psychologique actuelle:** [X/5] ([Phase Name])
*(Use 1/5 for established characters, adjust if introduced mid-arc)*

**Émotions dominantes:**
- [Initial emotional state]

**Croyances actuelles:**
- Sur lui-même: [Initial self-concept]
- Sur le monde: [Initial worldview]
- Sur les autres: [Initial expectations]

**Relations initiales:**
| Avec | Nature | Intensité | Évolution |
|------|--------|-----------|-----------|
| [Character] | [type] | [level] | [direction] |

**Arc potentiel:**
- Point de départ: [Current state]
- Direction probable: [Where they might go]

**Première apparition:** [Chapter/Event]
```

## Relationship Nature Types

**Positive:**
- Alliance: Partnership toward shared goal
- Amitié: Friendship with emotional bond
- Romance: Romantic attraction or relationship
- Familial: Family connection (blood or chosen)
- Mentorat: Teaching/learning relationship

**Negative:**
- Rivalité: Competition for same goal/resource
- Inimitié: Active opposition or hostility
- Trahison: Broken trust (may evolve)
- Manipulation: Using another for personal gain

**Neutral/Complex:**
- Respect mutuel: Professional regard without friendship
- Obligation: Duty-bound relationship
- Ambiguïté: Unclear or shifting nature
- Dépendance: Reliance on another (may be unequal)

## Intensity Guidelines

**Low:**
- Casual acquaintance
- Occasional interaction
- Minimal emotional investment
- Example: "Know each other's names"

**Medium:**
- Regular interaction
- Some emotional significance
- Affects decisions sometimes
- Example: "Work together occasionally"

**High:**
- Constant interaction or emotional weight
- Significantly affects decisions
- Central to character's story
- Example: "Daily collaboration, life-altering bond"

## Related References

- **Phase Definitions:** See `character-phases.md`
- **Update Procedures:** See `character-update-procedures.md`
- **Relationship Guidelines:** See `character-relationships.md`
