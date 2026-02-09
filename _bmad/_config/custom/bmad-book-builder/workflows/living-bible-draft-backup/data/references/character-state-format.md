# Character State Format Reference

This document provides the standard format for character state entries in the living bible.

## Template Structure

```markdown
### [Character Name]

**État psychologique actuel:**
- Phase: [X/5] ([Phase name])
- État émotionnel: [Emotional state description]
- Croyances dominantes: "[Core belief]"
- Contradictions internes: [Internal conflicts]

**Relations actuelles:**
| Personnage | Nature | Intensité | Dynamique |
|------------|--------|-----------|-----------|
| [Name 1] | [Relationship type] | [Intensity] | [Dynamic description] |
| [Name 2] | [Relationship type] | [Intensity] | [Dynamic description] |

**Arc en cours:** [Arc name, e.g., "Individualisme → Collectivisme"]
- Phase actuelle: [X/5] ([Phase name])
- Progression: [Progress status]
- Prochaine étape: [Next step description]

**Apparitions:**
- Dernière apparition: Chapitre [N]
- Prochaine apparition planifiée: Chapitre [N]

**Historique récent:**
- Chapitre [N]: [Event description] (Phase change if applicable)
- Chapitre [N]: [Event description] (consolidation/change)
```

## Example

```markdown
### Marc

**État psychologique actuel:**
- Phase: 3/5 (Point de bascule)
- État émotionnel: Doute croissant, peur de l'échec
- Croyances dominantes: "Je dois tout contrôler pour protéger les autres"
- Contradictions internes: Veut protéger mais étouffe

**Relations actuelles:**
| Personnage | Nature | Intensité | Dynamique |
|------------|--------|-----------|-----------|
| Élise | Rivale/Alliée | Haute | Tension sur le leadership |
| Julie | Intérêt romantique | Moyenne | Alliance fragile |
| Chen | Subordonné | En déclin | Loyauté questionnée |

**Arc en cours:** Individualisme → Collectivisme
- Phase actuelle: 3/5 (Crise de contrôle)
- Progression: En progrès (premiers doutes)
- Prochaine étape: Lâcher-prise forcé

**Apparitions:**
- Dernière apparition: Chapitre 12
- Prochaine apparition planifiée: Chapitre 14

**Historique récent:**
- Chapitre 10: Confrontation avec Élise (Phase 2→3)
- Chapitre 12: Doutes sur ses décisions (consolidation Phase 3)
```

## Field Definitions

### Psychological State
- **Phase (X/5)**: Current position in psychological arc (see Psychological Phases Reference)
- **État émotionnel**: Brief description of current emotional state
- **Croyances dominantes**: Core belief system driving character behavior
- **Contradictions internes**: Internal conflicts creating tension

### Relationships Table
- **Personnage**: Related character name
- **Nature**: Type of relationship (rival, ally, romantic, subordinate, etc.)
- **Intensité**: Low/Medium/High intensity level
- **Dynamique**: Description of relationship dynamics

### Arc Progression
- **Arc en cours**: Name of character arc (typically "From → To" format)
- **Phase actuelle**: Current phase number/name
- **Progression**: Status of progression
- **Prochaine étape**: Expected next development

### Appearances
- **Dernière apparition**: Last chapter where character appeared
- **Prochaine apparition planifiée**: Next planned appearance (if known)

### Recent History
- **Chapitre [N]**: Chapter number and event description
- Note phase changes in parentheses
