# evaluation/evaluate.py

import json
from sklearn.metrics import precision_score, recall_score, f1_score

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def evaluate_field(pred, actual):
    return 1 if str(pred).strip().lower() == str(actual).strip().lower() else 0

def evaluate_skills(predicted_skills, actual_skills):
    pred_set = set([s.lower() for s in predicted_skills])
    true_set = set([s.lower() for s in actual_skills])
    
    tp = len(pred_set & true_set)
    fp = len(pred_set - true_set)
    fn = len(true_set - pred_set)

    precision = tp / (tp + fp + 1e-6)
    recall = tp / (tp + fn + 1e-6)
    f1 = 2 * precision * recall / (precision + recall + 1e-6)
    
    return precision, recall, f1

def evaluate_all(pred_jsons, gt_jsons):
    name_score = email_score = phone_score = 0
    skill_p = skill_r = skill_f1 = 0

    n = len(gt_jsons)
    for i in range(n):
        pred = pred_jsons[i]
        actual = gt_jsons[i]

        name_score += evaluate_field(pred["name"], actual["name"])
        email_score += evaluate_field(pred["email"], actual["email"])
        phone_score += evaluate_field(pred["phone"], actual["phone"])

        p, r, f1 = evaluate_skills(pred["skills"], actual["skills"])
        skill_p += p
        skill_r += r
        skill_f1 += f1

    return {
        "name_accuracy": round(name_score / n * 100, 2),
        "email_accuracy": round(email_score / n * 100, 2),
        "phone_accuracy": round(phone_score / n * 100, 2),
        "skills_precision": round(skill_p / n * 100, 2),
        "skills_recall": round(skill_r / n * 100, 2),
        "skills_f1": round(skill_f1 / n * 100, 2)
    }
