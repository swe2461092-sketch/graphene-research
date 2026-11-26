# Research Proposal: AI-Agent-Managed Graphene Band Structure and DOS Calculation

## 1. Problem Statement
First-principles Density Functional Theory (DFT) calculations using Quantum ESPRESSO require careful parameter convergence (`ecutwfc`, `ecutrho`, k-point grids, smearing), strict provenance tracking (pseudopotential hashes, input manifests), and reproducible post-processing. Manual execution is prone to parameter drift, unverified outputs, and missing documentation. This project builds an AI-agent-managed scientific computing workflow using OpenClaw and Quantum ESPRESSO to automate input preparation, convergence planning, and verified result reporting under strict human-in-the-loop governance.

## 2. Target Users
- Computational materials science students and researchers performing DFT electronic structure calculations on 2D materials (graphene).
- Capstone evaluators reviewing reproducible, human-approved AI scientific workflows.

## 3. User Stories
- **US-1 (Input Preparation):** As a researcher, I want the AI agent to prepare Quantum ESPRESSO `scf`, `bands`, and `nscf/dos` input files from verified textbook templates (`QE-SSP`) so that crystal lattice and pseudopotential settings are accurate.
- **US-2 (Human-in-the-Loop Safety):** As a researcher, I want the agent to generate a calculation manifest and request explicit approval before running `pw.x` so that no unreviewed or expensive jobs execute automatically.
- **US-3 (Convergence & Analysis):** As a researcher, I want automated convergence input generation (`ecutwfc` and k-point sweeps) and verified plotting of band structure (Dirac cone at the K-point) and electronic Density of States (DOS) from actual QE outputs.
- **US-4 (Knowledge Provenance):** As a researcher, I want verified findings and pseudopotential SHA-256 hashes recorded in a structured research wiki (`wiki/`) so that every claim is traceable to raw outputs.

## 4. Acceptance Criteria
- [x] `graphene-qe` Conda environment active with Quantum ESPRESSO (`pw.x`, `bands.x`, `dos.x`), Python, `pymatgen`, `numpy`, and `matplotlib`.
- [x] Project repository structured with `AGENTS.md`, `skills/` (`dft-qe`, `pymatgen-structure`, `graphene-research`), `docs/`, `scripts/`, and `wiki/`.
- [x] `references/` and `runs/` excluded via `.gitignore`; pseudopotential SHA-256 hash documented in `docs/pseudopotential-sha256.txt`.
- [x] OpenClaw `graphene` agent bound to Telegram channel and verified via read-only Lab 0 health check without executing QE.
- [ ] (Lab 1+) Baseline SCF, Band Structure, DOS, and convergence sweeps executed after human approval and documented in `wiki/`.

## 5. Implementation Scope
- **In Scope:** Graphene primitive hexagonal cell (`ibrav = 4`), PBE ultrasoft pseudopotential (`C.pbe-n-rrkjus_psl.0.1.UPF`), SCF/Bands/DOS workflows, convergence sweep preparation (`scripts/prepare_convergence.py`), Telegram-based OpenClaw agent orchestration, and GitHub version control.
- **Out of Scope (Lab 0):** Executing `pw.x` production runs, modifying raw QE outputs, or exposing API tokens/credentials in Git.

## 6. Software Engineering Extension
- **Deterministic Manifest & Guardrail Wrapper:** Enforce pre-execution manifest generation (`manifest.json`) and SHA-256 pseudopotential verification before any solver script can be unlocked by human approval.
