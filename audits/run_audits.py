import json, re

payload = {
  "status": "SUCCESS",
  "project": "Project Lumiere (Life-Science)",
  "platform": "Handshake AI (HAI)",
  "submission_payload": {
    "assay_supertype": "Gel Electrophoresis & Western Blots",
    "image_metadata": {
      "format": "PNG",
      "license_verification": "CC BY 4.0",
      "source_url_or_doi": "https://doi.org/10.15252/embr.201439247"
    },
    "prompt": {
      "character_count": 0,
      "text": "The attached figure represents the results of a co-immunoprecipitation (Co-IP) experiment in Saccharomyces cerevisiae analyzing protein-protein interactions with the RNA Polymerase II subunit Rpb3 under varying temperatures and genetic backgrounds. Whole-cell extracts were prepared from wild-type and temperature-sensitive spt6-1004 cells grown at either 30 °C (permissive) or 37 °C (non-permissive, causing Spt6 depletion). Extracts were incubated with an anti-FLAG antibody targeting FLAG-tagged Rpb3, and the immunoprecipitated (IP) fractions were analyzed by Western blotting alongside input lysates. Probed targets include Rpb3-FLAG, Rpb1, Spt5, Spn1, Set2, Abd1, and the reference loading control Ceg1. Based strictly on the comparative band intensities in the IP fractions under permissive versus non-permissive temperatures, which of the probed candidate proteins require Spt6 to maintain their physical interaction with Rpb3?"
    },
    "options": {
      "A": "Rpb1 and Spt5",
      "B": "Abd1 and Set2",
      "C": "Spn1 only",
      "D": "Set2 only",
      "E": "Ceg1 and Spn1",
      "F": "Spn1 and Set2"
    },
    "correct_option": "F",
    "adversarial_justification": {
      "model_failure_rationale": "Frontier vision-language models fail this test across two distinct failure modes. Responder Model 1 exhibited 'Visual / Prior Override' by assuming that core transcription elongation factors (Spt5 and Rpb1) must dissociate when Spt6 is degraded, hallucinating reduced intensity in lane 9 where bands remain robust. Responder Model 2 exhibited 'Figure-based Quantitative & Condition Misattribution' by failing to distinguish input lysate lanes (lanes 1-5, which confirm invariant protein expression) from IP eluate lanes (lanes 6-10), incorrectly concluding that no interaction was altered because input bands were identical across all temperatures. Both models fail to execute the 3-hop reasoning chain required to isolate lane 8 (IP at 37 °C, wild-type with functional Spt6) vs. lane 9 (IP at 37 °C, spt6-1004 mutant with Spt6 depleted) and normalize against the Ceg1 recovery control.",
      "reasoning_hops": [
        "Hop 1: Visual observation — Map the 10-lane Western blot layout to identify lanes 1-5 as whole-cell input lysates and lanes 6-10 as anti-FLAG immunoprecipitates. Identify temperature condition headers: lanes 1-2, 5, 6-7, and 10 are at 30 °C, while lanes 3-4 and 8-9 are at 37 °C. In the IP fraction, identify lane 8 as wild-type cells at 37 °C (functional Spt6 present) and lane 9 as spt6-1004 mutant cells at 37 °C (Spt6 depleted).",
        "Hop 2: Intermediate mechanistic deduction — Cross-reference the 7 probed antibody tiers between lane 8 (IP at 37 °C, SPT6+) and lane 9 (IP at 37 °C, SPT6-depleted), while using lane 7 (IP at 30 °C, spt6-1004 permissive) as the genetic baseline. In lanes 6-8, robust bands are visible across all tiers. However, in lane 9 at 37 °C, while Rpb3-FLAG, Rpb1, Spt5, and Abd1 retain strong signal and Ceg1 confirms equivalent recovery, the bands for Spn1 and Set2 are completely lost.",
        "Hop 3: Final terminal conclusion — Conclude that the physical association of Spn1 and Set2 with Rpb3 is selectively abolished upon thermal depletion of Spt6 at 37 °C in vivo (lane 9 vs. lane 8 and lane 7), demonstrating that Spt6 is strictly required for the interaction of Spn1 and Set2 with Rpb3."
      ]
    },
    "five_pillar_image_description": {
      "word_count": 0,
      "pillar_1_setup": "A 7-tier Western blot stack derived from a co-immunoprecipitation experiment in budding yeast (Saccharomyces cerevisiae) evaluating temperature-dependent association with FLAG-tagged RNA Polymerase II subunit Rpb3.",
      "pillar_2_layout": "A vertical composite of 7 chemiluminescent gel membranes, each displaying 10 vertical lanes labeled sequentially from left to right. A common header panel marks lanes 1-5 as 'Input' (lanes 1-4 Rpb3-FLAG positive, lane 5 untagged control; lanes 1-2 at 30 °C, lanes 3-4 at 37 °C) and lanes 6-10 as 'IP' (lanes 6-9 Rpb3-FLAG positive, lane 10 untagged control; lanes 6-7 at 30 °C, lanes 8-9 at 37 °C). Specifically, lane 8 represents wild-type cells at 37 °C (SPT6+), whereas lane 9 represents temperature-sensitive spt6-1004 cells at 37 °C (SPT6-depleted). Lane 7 represents spt6-1004 cells at 30 °C (permissive temperature, SPT6+). External labels along the left margin indicate the probed antibody targets: Rpb3-FLAG, Rpb1, Spt5, Spn1, Set2, Abd1, and Ceg1.",
      "pillar_3_readouts": "In the input lanes (1-5), distinct dark horizontal bands of uniform intensity are visible across all probed tiers at their expected molecular weights, confirming equivalent total protein expression across wild-type and mutant strains at both 30 °C and 37 °C. In the IP lanes (6-10), the Rpb3-FLAG, Rpb1, Spt5, and Ceg1 panels show intense, sharp bands in lanes 6-9 with complete absence of signal in untagged control lane 10. In the Spn1 and Set2 panels, lanes 6, 7 (at 30 °C), and lane 8 (wild-type at 37 °C) display prominent, well-defined bands of comparable intensity, whereas lane 9 (spt6-1004 at 37 °C) shows a complete void of signal with no detectable band above background.",
      "pillar_4_artifacts": "Authentic experimental artifacts include slight meniscus band curvature ('smiling') of approximately 15 degrees upward on the right edge of lanes 8 and 9 in the lower panels, a faint non-specific background smudge between lanes 4 and 5 in the Abd1 tier, and minor edge vignetting along the bottom perimeter of the Ceg1 membrane. No air bubbles, membrane puncta, or over-saturated signal flares are present.",
      "pillar_5_ground_truth": "The visual presentation presents an unambiguous contrast between temperature-resilient bands (retained in both lane 8 and lane 9 at 37 °C) and temperature-sensitive bands (abruptly lost between lane 8 and lane 9 at 37 °C), without any textual labels or annotation callouts indicating which factor is dependent on Spt6.",
      "full_text": ""
    },
    "distractor_explanations": {
      "distractor_1": "Rpb1 and Spt5: Fails because both Rpb1 and Spt5 maintain strong, unaltered band intensities in the IP fraction across lanes 8 and 9 at 37 °C, indicating their interaction with Rpb3 is constitutive and independent of Spt6.",
      "distractor_2": "Abd1 and Set2: Fails because Abd1 remains stably bound to Rpb3 in lane 9 despite Spt6 depletion at 37 °C; only Set2 displays loss of co-purification in this pair.",
      "distractor_3": "Spn1 only: Fails because it overlooks the concurrent and complete disappearance of the Set2 band in the 37 °C IP fraction of the mutant (lane 9), rendering the answer incomplete.",
      "distractor_4": "Set2 only: Fails because it identifies Set2 while omitting Spn1, which exhibits identical Spt6-dependent loss of co-immunoprecipitation in lane 9 at 37 °C.",
      "distractor_5": "Ceg1 and Spn1: Fails because Ceg1 is the invariant loading and recovery control, showing robust and equivalent band density across all positive IP lanes (lanes 6-9) at both temperatures."
    }
  },
  "audit_checklist_verified": True
}

# String Sanitization Audit
prompt_text = payload["submission_payload"]["prompt"]["text"]
assert "\n" not in prompt_text, "Line break found in prompt text!"
payload["submission_payload"]["prompt"]["character_count"] = len(prompt_text)

pillars = payload["submission_payload"]["five_pillar_image_description"]
full_text = f"{pillars['pillar_1_setup']} {pillars['pillar_2_layout']} {pillars['pillar_3_readouts']} {pillars['pillar_4_artifacts']} {pillars['pillar_5_ground_truth']}"
assert "\n" not in full_text, "Line break found in full_text!"
payload["submission_payload"]["five_pillar_image_description"]["full_text"] = full_text
words = len(full_text.split())
payload["submission_payload"]["five_pillar_image_description"]["word_count"] = words

# Distractor count audit
options = payload["submission_payload"]["options"]
distractors = [k for k, v in options.items() if k != payload["submission_payload"]["correct_option"]]
assert len(distractors) == 5, f"Distractor count is {len(distractors)}, expected 5!"
assert len(payload["submission_payload"]["distractor_explanations"]) == 5, "Distractor explanations count != 5!"

# Word & Char count audit
assert len(prompt_text) <= 2000, f"Prompt length {len(prompt_text)} > 2000!"
assert words >= 200, f"Image description word count {words} < 200!"

# Logical Consistency Audit
# Check Lane 8 references:
json_str = json.dumps(payload, ensure_ascii=False)
for m in re.finditer(r'lane 8[^\.]*?(30|37)\s*°C', json_str, re.IGNORECASE):
    temp = m.group(1)
    assert temp == "37", f"Conflict! Lane 8 associated with {temp} °C in: {m.group(0)}"

for m in re.finditer(r'lane 9[^\.]*?(30|37)\s*°C', json_str, re.IGNORECASE):
    temp = m.group(1)
    assert temp == "37", f"Conflict! Lane 9 associated with {temp} °C in: {m.group(0)}"

for m in re.finditer(r'lane 7[^\.]*?(30|37)\s*°C', json_str, re.IGNORECASE):
    temp = m.group(1)
    assert temp == "30", f"Conflict! Lane 7 associated with {temp} °C in: {m.group(0)}"

print("=== ALL AUDITS PASSED SUCCESSFULLY ===")
print(f"Prompt character count: {len(prompt_text)} (limit: 2000)")
print(f"Five-pillar word count: {words} (minimum: 200)")
print(f"Distractor count: {len(distractors)}")
print(f"JSON character length: {len(json_str)}")

with open("scratch/final_verified_payload.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, ensure_ascii=False)
