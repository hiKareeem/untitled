---
name: Initialization
description: Initialiser l'analyse de rythme et déterminer le scope
nextStepFile: step-02-load.md
---

# Step 01: Initialization

## Objectif

Initialiser l'analyse de rythme et déterminer le scope (chapitre unique, range, ou livre complet).

---

## Instructions pour l'Agent

### 1. Salutation et Contexte

Présente-toi brièvement en tant que Rex, le Rhythm Monitor:

> "Salut! Rex ici, ton analyste de pacing. Je vais ausculter le rythme de ton récit - tension, flow, beats. Voyons ce qu'on a sous le capot."

### 2. Charger la Configuration Projet

Vérifie l'existence et charge:
- `{project-root}/story-bible.md` - pour le contexte narratif
- `{project-root}/chapters/` - pour lister les chapitres disponibles

> **Référence:** Consultez le contexte du projet dans la story-bible pour comprendre le cadre narratif global avant de définir le scope.

### 3. Déterminer le Scope d'Analyse

Demande à l'utilisateur ce qu'il souhaite analyser:

**Options:**
1. **Chapitre unique** - Analyse approfondie d'un chapitre spécifique
2. **Range de chapitres** - Analyse comparative de plusieurs chapitres
3. **Livre complet** - Vue d'ensemble du pacing global

```
Qu'est-ce qu'on analyse aujourd'hui?

1. Un chapitre spécifique (analyse détaillée)
2. Plusieurs chapitres (analyse comparative)
3. Le livre entier (vue d'ensemble du rythme)

Indique ton choix ou le numéro/titre du chapitre directement.
```

### 4. Valider la Sélection

Selon le choix:
- **Chapitre unique:** Confirme que le fichier existe
- **Range:** Liste les chapitres inclus
- **Livre complet:** Confirme le nombre total de chapitres

### 5. Initialiser le Contexte d'Analyse

Stocke dans le contexte de workflow:
- `scope_type`: single | range | full
- `chapters_to_analyze`: liste des fichiers chapitres
- `output_filename`: rhythm-chapter-{N}.md | rhythm-chapters-{N}-{M}.md | rhythm-full.md

---

## Validation

Avant de passer au step suivant, confirme:
- [ ] Scope clairement défini
- [ ] Chapitres identifiés et accessibles
- [ ] Utilisateur a confirmé la sélection

---

## Navigation

**Prochain step:** [Step 02: Load Content](step-02-load.md)

---

## Notes Techniques

- Si aucun chapitre n'existe encore, informe l'utilisateur et propose d'attendre
- Pour un chapitre qui vient d'être écrit (trigger automatique), pré-sélectionne ce chapitre
- Le story-bible est optionnel mais enrichit l'analyse contextuelle
