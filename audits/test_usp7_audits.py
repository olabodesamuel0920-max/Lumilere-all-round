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
      "source_url_or_doi": "https://doi.org/10.1038/s41467-023-41221-8"
    },
    "prompt": {
      "character_count": 0,
      "text": "The attached figure presents a co-immunoprecipitation (Co-IP) and Western blot assay in human osteosarcoma (U2OS) cells evaluating endogenous USP7 interactome remodeling during genotoxic stress. Cells were treated with vehicle (DMSO, 0 h) or 0.5 µM doxorubicin for 4 h and 8 h. Whole-cell extracts were analyzed as inputs (Lanes 1–3) or subjected to immunoprecipitation using an anti-USP7 antibody (Lanes 4–6). Probed targets in the IP fraction include MDM2, p53, and immunoprecipitated USP7 recovery control; input lysates are probed for USP7, MDM2, p53, p21, and GAPDH loading control. Based strictly on the visual band dynamics in the immunoprecipitated eluates (Lanes 4–6) relative to input abundance across the treatment time course, what is the precise impact of 8 hours of doxorubicin exposure (Lane 6 vs. Lane 4) on the physical association of USP7 with MDM2 and with p53, respectively?"
    },
    "options": {
      "A": "USP7 binding to MDM2 is increased, while binding to p53 is abolished.",
      "B": "USP7 binding to both MDM2 and p53 is constitutively maintained without change.",
      "C": "USP7 binding to MDM2 is abolished, while binding to p53 is selectively enriched.",
      "D": "USP7 binding to both MDM2 and p53 is completely lost due to global degradation of USP7.",
      "E": "USP7 binding to MDM2 is abolished, while p53 fails to physically associate with USP7 at any timepoint.",
      "F": "USP7 binding to MDM2 is preserved, while p53 binding is transiently induced at 4 hours and lost at 8 hours."
    },
    "correct_option": "C",
    "adversarial_justification": {
      "model_failure_rationale": "Frontier vision-language models consistently fail this multimodal assay due to two prominent multimodal blind spots. First, models exhibit 'Visual / Prior Override' by assuming that because total MDM2 protein diminishes in input Lane 3, the absence of an MDM2 band in IP Lane 6 is a trivial consequence of target depletion rather than an active dissociation mechanism. Second, models exhibit 'Condition Misattribution and Band Smeared Optical Confusion', misinterpreting the high-molecular-weight polyubiquitin smear of self-ubiquitinated MDM2 in Lane 5 as persistent USP7 binding, while overlooking the emerging distinct ~53 kDa band in IP Lane 6. Both models fail to connect the reciprocal switch from USP7-MDM2 binding in Lane 4 (0 h) to USP7-p53 binding in Lane 6 (8 h) while normalizing against invariant recovery of USP7.",
      "reasoning_hops": [
        "Hop 1: Visual observation — Map the 6-lane Western blot layout to identify Lanes 1–3 as input lysates (0 h, 4 h, 8 h doxorubicin) and Lanes 4–6 as anti-USP7 immunoprecipitates (0 h, 4 h, 8 h doxorubicin). Confirm invariant USP7 recovery across IP Lanes 4–6 and uniform GAPDH loading across input Lanes 1–3.",
        "Hop 2: Intermediate mechanistic deduction — Trace MDM2 and p53 band dynamics across the Co-IP tiers: In Lane 4 (0 h DMSO), a prominent ~90 kDa MDM2 band co-precipitates with USP7, whereas p53 signal is absent. In Lane 5 (4 h Dox), the MDM2 band weakens and shifts into a faint polyubiquitinated smear, while a faint p53 band emerges. In Lane 6 (8 h Dox), the MDM2 band in the IP fraction is completely abolished, whereas the co-precipitated p53 band reaches peak intensity.",
        "Hop 3: Final terminal conclusion — Synthesize that genotoxic stress induced by 8 hours of doxorubicin drives a complete reciprocal remodeling of the USP7 interactome: USP7 physical binding to MDM2 is completely lost/abolished (Lane 6 vs. Lane 4), while its physical binding to p53 is selectively and robustly enriched."
      ]
    },
    "five_pillar_image_description": {
      "word_count": 0,
      "pillar_1_setup": "A dual-panel Western blot montage displaying co-immunoprecipitation and input whole-cell lysate immunoblots from human osteosarcoma U2OS cells exposed to genotoxic doxorubicin treatment (0.5 µM).",
      "pillar_2_layout": "The image is vertically structured into two primary sections comprising 6 vertical lanes: the upper section contains the anti-USP7 immunoprecipitates (IP: USP7, Lanes 4–6) and the lower section contains whole-cell input lysates (Input 5%, Lanes 1–3). An experimental condition header across the top labels Lanes 1 and 4 as 0 h (DMSO vehicle control), Lanes 2 and 5 as 4 h (0.5 µM doxorubicin), and Lanes 3 and 6 as 8 h (0.5 µM doxorubicin). Tiers in the IP panel are probed for MDM2, p53, and USP7. Tiers in the input panel are probed for USP7, MDM2, p53, p21 (CDKN1A), and GAPDH. Molecular weight markers (kDa) are annotated along the right-hand margin.",
      "pillar_3_readouts": "In the input section (Lanes 1–3), GAPDH (37 kDa) and USP7 (130 kDa) exhibit uniform horizontal band intensities across all three timepoints. MDM2 (90 kDa) is abundant in Lane 1 (0 h), decreases moderately in Lane 2 (4 h), and displays marked depletion in Lane 3 (8 h). Conversely, p53 (53 kDa) is undetectable at 0 h (Lane 1), appears as a clear band at 4 h (Lane 2), and accumulates intensely at 8 h (Lane 3), with a corresponding strong induction of its transcriptional target p21 (21 kDa) in Lanes 2 and 3. In the IP section (Lanes 4–6), USP7 recovery is identical across all lanes. MDM2 shows a strong, well-defined co-precipitating band in Lane 4 (0 h), which weakens into a faint upward ladder in Lane 5 (4 h) and completely disappears with zero detectable signal in Lane 6 (8 h). Concurrently, p53 is absent in Lane 4 (0 h), emerges as a distinct band in Lane 5 (4 h), and demonstrates strong, dark band intensity in Lane 6 (8 h).",
      "pillar_4_artifacts": "Authentic experimental features include slight non-specific background hazing in the high-molecular-weight region (>130 kDa) of the MDM2 IP blot in Lane 5, minor edge-compression of the bottom-most GAPDH band on the far right perimeter, and a faint punctate transfer spot below Lane 2 in the p21 input tier. The chemiluminescent exposure is balanced with sharp band delineation and no evidence of saturated white-hole core pixels or air bubble voids.",
      "pillar_5_ground_truth": "The immunoblot demonstrates an unambiguous reciprocal binding switch in the IP series: the intense MDM2 band in Lane 4 disappears entirely by Lane 6, while the p53 signal transitions from completely negative in Lane 4 to strongly positive in Lane 6, without revealing verbal conclusions on the image membrane.",
      "full_text": ""
    },
    "distractor_explanations": {
      "distractor_1": "USP7 binding to MDM2 is increased, while binding to p53 is abolished: Fails due to direct inverted misreading of the IP lanes; MDM2 band intensity in Lane 6 is completely lost compared to Lane 4, whereas p53 band intensity increases from zero in Lane 4 to maximal in Lane 6.",
      "distractor_2": "USP7 binding to both MDM2 and p53 is constitutively maintained without change: Fails because it ignores the dynamic disappearance of the MDM2 band in Lane 6 and the de novo appearance and progressive accumulation of the co-immunoprecipitated p53 band in Lanes 5 and 6.",
      "distractor_3": "USP7 binding to both MDM2 and p53 is completely lost due to global degradation of USP7: Fails because both the whole-cell lysate inputs (Lanes 1–3) and the immunoprecipitated recovery control (Lanes 4–6) prove that total USP7 protein levels remain invariant across the entire 8-hour doxorubicin time course.",
      "distractor_4": "USP7 binding to MDM2 is abolished, while p53 fails to physically associate with USP7 at any timepoint: Fails because it correctly observes the loss of MDM2 but overlooks the prominent, specific ~53 kDa band co-precipitating with USP7 in Lane 6 (8 h).",
      "distractor_5": "USP7 binding to MDM2 is preserved, while p53 binding is transiently induced at 4 hours and lost at 8 hours: Fails because it falsely claims MDM2 binding persists at 8 hours (where Lane 6 shows complete absence of signal) and incorrectly asserts that p53 binding is lost at 8 hours (where p53 signal is actually at its highest intensity)."
    }
  },
  "audit_checklist_verified": True
}

# 1. String Sanitization Audit
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
correct_opt = payload["submission_payload"]["correct_option"]
distractors = [k for k in options if k != correct_opt]
assert len(distractors) == 5, f"Distractor count is {len(distractors)}, expected 5!"
assert len(payload["submission_payload"]["distractor_explanations"]) == 5, "Distractor explanations count != 5!"

# Word & Char count audit
assert len(prompt_text) <= 2000, f"Prompt length {len(prompt_text)} > 2000!"
assert words >= 200, f"Image description word count {words} < 200!"

# 2. Logical Consistency Audit: verify all Lane (X h) pairs
json_str = json.dumps(payload, ensure_ascii=False)
lane_matches = re.findall(r'Lane ([1-6])\s*\(([^)]+)\)', json_str)
for lane_num, condition in lane_matches:
    if lane_num in ['1', '4']:
        assert '0 h' in condition, f'Lane {lane_num} has condition {condition}, expected 0 h!'
    elif lane_num in ['2', '5']:
        assert '4 h' in condition, f'Lane {lane_num} has condition {condition}, expected 4 h!'
    elif lane_num in ['3', '6']:
        assert '8 h' in condition, f'Lane {lane_num} has condition {condition}, expected 8 h!'

print("=== ALL AUDITS PASSED ===")
print(f"Prompt characters: {len(prompt_text)} (<= 2000)")
print(f"Five-pillar description word count: {words} (>= 200)")
print(f"Distractor count: {len(distractors)}")
print(f"Correct option: {correct_opt}")
print(f"Total options: {len(options)}")
print(f"JSON character length: {len(json_str)}")

with open("scratch/verified_usp7_payload.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, ensure_ascii=False)
print("Saved scratch/verified_usp7_payload.json successfully!")
