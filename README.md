# coolChem · AQA AS & A-Level Chemistry Revision Portal

> **coolChem** is an ultra-fast, minimalist past paper question bank, cheatsheet repository, and interactive revision system designed specifically for **AQA AS and A-Level Chemistry (7404 / 7405)**.

Live site: [https://chanale-lab.github.io/coolChem/](https://chanale-lab.github.io/coolChem/)

---

## 🧪 Key Features

1. **Specification & Curriculum Browser:**
   - Organized strictly by the official AQA specification sections across **Physical Chemistry**, **Inorganic Chemistry**, **Organic Chemistry**, and **Required Practicals (RP1–RP12)**.
   - Live mark counters and topic mastery tracking.

2. **Past Paper Question Bank:**
   - Multi-dimensional filtering by **Level** (AS / A-Level), **Topic**, **Paper**, **Skill** (Maths, Practical, Mechanisms, Analysis), and **Minimum Marks**.
   - Side-by-side split view for questions and official mark schemes.
   - Individual question PDF printing and batch question worksheet generation.
   - Star/Bookmark system and Mark-as-Done mastery tracking (saved persistently to `localStorage`).

3. **High-Yield Revision Cheatsheets:**
   - Dedicated specification checklists and structured notes for all 35 topics.
   - Includes essential definitions, SI equations, curly arrow mechanisms, colours of transition metal complexes, and required practical methods.
   - Instant 1-click **Export to PDF / Print** formatting.

4. **Interactive Practice & Flashcards:**
   - Over 80 high-impact flashcards covering key definitions, reaction conditions, reagents, and formulas.
   - Spaced repetition mode, starred filter, and mastery tracking.

5. **Teacher's Revision & Classroom Hub:**
   - **Classroom Quiz Game:** Projector-ready interactive quiz game with Team 1 vs Team 2 scoreboard, countdown timer, sound effects, and celebratory confetti.
   - **Question & Worksheet Generator:** Assemble custom worksheets and mock exams by topic and target marks with printable ruled answer lines and full teacher mark keys.
   - **Chemillion Trivia Game:** Deep chemical trivia game exploring elements, mechanisms, reagents, catalysts, and experimental techniques.

6. **Interactive Periodic Table & Data Reference:**
   - Built-in data sheet reference accessible from any page: physical constants ($R$, $L$, $K_w$, $c$), Group & Period layout, and infrared absorption wavenumber ranges.

---

## 🔬 AQA Chemistry Specification Structure

### 3.1 Physical Chemistry
- **3.1.1** Atomic structure & TOF Mass Spectrometry
- **3.1.2** Amount of substance, Ideal gas equation & Titrations
- **3.1.3** Bonding & crystal structures
- **3.1.4** Energetics & Hess's Law
- **3.1.5** Kinetics & Maxwell-Boltzmann distributions
- **3.1.6** Chemical equilibria, Le Chatelier's & $K_c$
- **3.1.7** Oxidation, reduction & redox equations
- **3.1.8** Thermodynamics, Born-Haber cycles & $\Delta G$ *(A-Level)*
- **3.1.9** Rate equations & Arrhenius equation *(A-Level)*
- **3.1.10** Equilibrium constant $K_p$ for gas equilibria *(A-Level)*
- **3.1.11** Electrode potentials & electrochemical cells *(A-Level)*
- **3.1.12** Acids, bases, pH curves & buffer action *(A-Level)*

### 3.2 Inorganic Chemistry
- **3.2.1** Periodicity & Period 3 trends
- **3.2.2** Group 2, the alkaline earth metals
- **3.2.3** Group 7(17), the halogens
- **3.2.4** Period 3 elements and their oxides *(A-Level)*
- **3.2.5** Transition metals & complex ions *(A-Level)*
- **3.2.6** Reactions of ions in aqueous solution *(A-Level)*

### 3.3 Organic Chemistry
- **3.3.1** Introduction to organic chemistry, nomenclature & isomerism
- **3.3.2** Alkanes, fractional distillation & cracking
- **3.3.3** Halogenoalkanes, nucleophilic substitution & elimination
- **3.3.4** Alkenes & electrophilic addition
- **3.3.5** Alcohols & biofuels
- **3.3.6** Organic analysis (Infrared & High-Resolution MS)
- **3.3.7** Optical isomerism & enantiomers *(A-Level)*
- **3.3.8** Aldehydes and ketones *(A-Level)*
- **3.3.9** Carboxylic acids, esters & acylation *(A-Level)*
- **3.3.10** Aromatic chemistry & benzene mechanisms *(A-Level)*
- **3.3.11** Amines & base properties *(A-Level)*
- **3.3.12** Condensation polymers *(A-Level)*
- **3.3.13** Amino acids, proteins & DNA *(A-Level)*
- **3.3.14** Organic synthesis routes *(A-Level)*
- **3.3.15** Nuclear magnetic resonance (NMR) spectroscopy *(A-Level)*
- **3.3.16** Chromatography (TLC, CC, GC) *(A-Level)*

### Practical Assessment
- **RP:** Required Practicals 1 through 12

---

## 🚀 Running Locally or Deploying

Because coolChem is built with pure standards-based HTML5, CSS3, and vanilla JavaScript, it has **zero build steps** and **zero dependencies**.

### Local Preview:
Simply serve the repository folder with any local HTTP server:
```bash
# Python
python -m http.server 8000

# or Node / npx
npx serve .
```
Then open `http://localhost:8000`.

### GitHub Pages Deployment:
In your repository settings:
1. Navigate to **Settings > Pages**.
2. Under **Build and deployment > Branch**, select `main` / `(root)`.
3. Click **Save**. The website is immediately published to `https://<username>.github.io/<repo>/`!

---

## 🔒 Access & Passcode
- The portal includes an optional security gate.
- Default unlock passcode: `chemistry` (or `coolchem`).
- Can also be customized or bypassed directly in `index.html`.

---

## 📄 License
Educational resource aligned with the AQA AS and A-level Chemistry specifications (7404 / 7405).
