"""
generate_dataset.py

Generates synthetic clinical notes dataset for BERT fine-tuning challenge.
Output: dataset/clinical_notes.csv
"""

import csv
import os
import random

random.seed(42)

CONDITIONS = {
    "cardiovascular": [
        "Patient presents with chest pain radiating to the left arm. ECG shows ST elevation in leads II, III, aVF. Troponin levels elevated at {val} ng/mL. Started on aspirin and heparin protocol.",
        "Hypertensive crisis with BP {val}/{val2} mmHg on admission. History of CAD and prior CABG. Echo reveals EF of 35%. Diuresis initiated with furosemide IV.",
        "Atrial fibrillation with RVR. HR {val} bpm. Patient anticoagulated with warfarin INR {val2}. Cardioversion considered pending cardiology consult.",
        "Congestive heart failure exacerbation. BNP elevated at {val} pg/mL. Bilateral pulmonary crackles. SpO2 88% on RA, improved to 96% on 4L NC O2.",
    ],
    "respiratory": [
        "Acute exacerbation of COPD. FEV1/FVC ratio {val}. Nebulized albuterol and ipratropium administered. ABG: pH 7.32, pCO2 55, pO2 62.",
        "Community-acquired pneumonia confirmed on CXR with right lower lobe consolidation. WBC {val} K/uL. Started on azithromycin and ceftriaxone.",
        "Asthma attack, moderate severity. Peak flow {val} L/min. Responded to bronchodilator therapy. Inhaled corticosteroids continued.",
        "Pulmonary embolism suspected based on Wells score {val}. D-dimer elevated. CT pulmonary angiography ordered. Anticoagulation started empirically.",
    ],
    "neurological": [
        "Ischemic stroke involving left MCA territory. NIHSS score {val}. tPA administered within {val2} hours of symptom onset. MRI confirms DWI positivity.",
        "First-time seizure, generalized tonic-clonic. Duration {val} minutes. EEG scheduled. Levetiracetam initiated at 500mg BID.",
        "Migraine with aura, severe intensity. Sumatriptan 100mg administered. Photophobia and phonophobia present. Prior history of 3 episodes monthly.",
        "Guillain-Barré syndrome suspected. Ascending weakness bilateral lower extremities. LP shows albuminocytologic dissociation. IVIG started.",
    ],
    "gastrointestinal": [
        "Upper GI bleed. Melena present. Hgb {val} g/dL, down from baseline. EGD reveals gastric ulcer with visible vessel. Epinephrine injection performed.",
        "Acute pancreatitis. Lipase {val} U/L, amylase elevated. Ranson score 3. NPO, IV fluids, pain management initiated. Etiology: gallstones.",
        "Inflammatory bowel disease flare. Colonoscopy shows active colitis from splenic flexure to rectum. CRP {val} mg/L. Steroids and mesalamine initiated.",
        "Appendicitis confirmed on CT with periappendiceal fat stranding. WBC {val} K/uL. Surgical consult obtained. Appendectomy scheduled.",
    ],
    "musculoskeletal": [
        "Rheumatoid arthritis flare. ESR {val} mm/hr, CRP elevated. Symmetric synovitis of MCP and PIP joints bilaterally. Methotrexate dose adjusted.",
        "Lumbar disc herniation at L4-L5 level on MRI. Radiculopathy affecting right L5 dermatome. Referred to physical therapy and pain specialist.",
        "Osteoporotic compression fracture T11. DEXA T-score {val}. Bisphosphonate therapy initiated. Kyphoplasty considered.",
        "Gout attack, acute, right first MTP joint. Uric acid {val} mg/dL. Colchicine and NSAIDs administered. Urate-lowering therapy discussed.",
    ],
    "endocrine": [
        "Diabetic ketoacidosis. Glucose {val} mg/dL. pH 7.22. Bicarbonate 10 mEq/L. Insulin drip and aggressive IV fluid resuscitation initiated.",
        "Hypothyroidism, newly diagnosed. TSH {val} mIU/L, free T4 low. Levothyroxine 50 mcg started. Follow-up labs in 6 weeks.",
        "Cushing syndrome workup. 24-hour urinary free cortisol elevated {val} mcg. Late-night salivary cortisol high. Pituitary MRI ordered.",
        "Adrenal insufficiency. Morning cortisol {val} mcg/dL. ACTH stimulation test non-responsive. Hydrocortisone replacement initiated.",
    ],
    "dermatological": [
        "Psoriasis vulgaris, moderate-severe. PASI score {val}. Plaques on elbows, knees, and scalp. Methotrexate prescribed after topical failure.",
        "Cellulitis, right lower extremity. Area of warmth and erythema {val} cm. Cephalexin 500mg QID prescribed. INR and glucose checked.",
        "Atopic dermatitis exacerbation. Extensive eczematous plaques. Eosinophil count {val} cells/mcL. Dupilumab injection administered.",
        "Melanoma, superficial spreading, Breslow thickness {val} mm. Wide local excision performed. Sentinel lymph node biopsy negative.",
    ],
}

SPECIALTIES = {
    "cardiovascular": "cardiology",
    "respiratory": "pulmonology",
    "neurological": "neurology",
    "gastrointestinal": "gastroenterology",
    "musculoskeletal": "rheumatology",
    "endocrine": "endocrinology",
    "dermatological": "dermatology",
}

COUNTS = {"cardiovascular": 4000, "respiratory": 3500, "neurological": 3000,
          "gastrointestinal": 3000, "musculoskeletal": 2500, "endocrine": 2000, "dermatological": 2000}


def render(template):
    val = round(random.uniform(1, 500), 1)
    val2 = round(random.uniform(1, 200), 1)
    return template.format(val=val, val2=val2)


def generate():
    os.makedirs("dataset", exist_ok=True)
    rows = []
    note_id = 1

    for condition, count in COUNTS.items():
        templates = CONDITIONS[condition]
        specialty = SPECIALTIES[condition]
        for _ in range(count):
            template = random.choice(templates)
            text = render(template)
            # Add some filler sentences to vary note length
            extra = random.randint(0, 3)
            for _ in range(extra):
                text += " " + random.choice([
                    "Vitals stable at time of assessment.",
                    "Patient tolerating oral intake.",
                    "Family notified and present at bedside.",
                    "Plan discussed with attending physician.",
                    "Follow-up scheduled in outpatient clinic.",
                    "Nursing staff updated on plan of care.",
                ])
            rows.append({
                "note_id": note_id,
                "text": text,
                "condition": condition,
                "specialty": specialty,
                "note_length": len(text.split()),
                "has_medication": any(w in text.lower() for w in ["mg", "mcg", "iv", "oral"]),
                "has_procedure": any(w in text.lower() for w in ["performed", "scheduled", "administered"]),
            })
            note_id += 1

    random.shuffle(rows)

    fields = ["note_id", "text", "condition", "specialty", "note_length", "has_medication", "has_procedure"]
    with open("dataset/clinical_notes.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Generated {len(rows)} clinical notes -> dataset/clinical_notes.csv")


if __name__ == "__main__":
    generate()
