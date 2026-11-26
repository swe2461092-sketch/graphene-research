---
name: graphene-research
description: Capstone research rules and human approval workflow for Graphene DFT calculations.
---
# Graphene Research Skill Rules
1. Use the textbook structure (`references/QE-SSP/gr/bands/scf.in`) or an approved CIF file.
2. Record pseudopotentials (including SHA-256 hash) and DFT settings.
3. Use `dft-qe` to prepare input files.
4. Show the exact calculation manifest before execution.
5. Request explicit researcher approval before running calculations.
6. Execute calculations using approved scripts only.
7. Analyze only actual QE output files. Do not fabricate calculation data.
8. Update the research Wiki only with verified findings.
