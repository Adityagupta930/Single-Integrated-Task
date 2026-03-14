# Training Diagnosis & Hyperparameter Fix

---

## Part 2 — Training Diagnosis

### Issue 1 — Overfitting

**Observed Symptoms**
- Training loss drops sharply while validation loss stagnates or rises.
- Model repeats memorized phrases ("Please check your email", "Go to account settings") regardless of context.
- Responses are correct for training examples but fail on slightly different inputs.

**Root Cause → Small, repetitive dataset.**
Only 4–5 near-identical conversations exist. The model has nothing to generalize from, so it memorizes token sequences instead of learning support reasoning. Running too many epochs amplifies this.

---

### Issue 2 — Poor / Unsafe Data Quality

**Observed Symptoms**
- Responses assume platform features that may not exist ("Go to profile settings").
- No examples of the assistant refusing harmful requests or escalating sensitive issues.
- Answers are vague and not grounded in any specific system context.

**Root Cause → Generic, context-free training pairs.**
The original samples lack platform specificity, edge cases, and safety-refusal examples. A model trained on this data will hallucinate platform details and ignore safety boundaries.

---

### Issue 3 — Gradient Instability

**Observed Symptoms**
- Loss spikes mid-training (NaN or sudden jumps in the training log).
- Model outputs become incoherent after a certain step.
- Gradient norm grows unboundedly.

**Root Cause → No gradient clipping + learning rate too high.**
With a tiny dataset, each batch is nearly identical, causing large, correlated gradient updates. Without clipping, a single bad batch can push weights into an unstable region.

---

### Issue 4 — Instruction / Safety Drift

**Observed Symptoms**
- Model stops following the system prompt after several epochs.
- Responses become less polite or structured over time.
- Safety rules defined in the system message are ignored.

**Root Cause → Lack of diverse instruction-following and safety-refusal examples.**
The system prompt is repeated verbatim across all samples with no variation. The model learns to treat it as boilerplate and eventually ignores it. There are zero examples of refusing unsafe requests, so the model never learns that boundary.

---

### Symptom → Root Cause Summary

| Symptom | Root Cause |
|---|---|
| Training loss low, validation loss high | Dataset too small → overfitting |
| Memorized, context-blind responses | Repetitive data + too many epochs |
| Vague / hallucinated platform details | Generic data with no grounding |
| No safety refusals | Missing safety-refusal examples in training set |
| Loss spikes / NaN gradients | High LR + no gradient clipping |
| Model ignores system prompt | No diverse instruction-following examples |

---

## Part 3 — Hyperparameter Fix

| Parameter | Old (Assumed) | Recommended | Why It Helps |
|---|---|---|---|
| **Epochs** | 10+ | **2–3** | Fewer passes over a tiny dataset prevent memorization. Stop early if validation loss stops improving. |
| **Learning Rate** | 1e-4 or higher | **2e-5** | Standard fine-tuning LR for transformer models. Large LR causes unstable updates on small data. |
| **Batch Size** | 1–2 | **8–16** | Larger batches average out noisy gradients, producing smoother and more stable updates. |
| **Gradient Clipping** | None | **1.0** | Caps the gradient norm so a single bad batch cannot destabilize the entire model. Directly fixes loss spikes. |
| **Warmup Steps** | 0 | **5–10% of total steps** | Starts with a near-zero LR and ramps up gradually, preventing large destructive updates in the first few batches. |

### Additional Recommendations
- Add **early stopping** (patience = 2) monitoring validation loss.
- Expand dataset to **500+ diverse conversations** before any serious fine-tuning run.
- Include **safety-refusal examples** (user asks something harmful → assistant politely declines).
- Use **data augmentation** (paraphrase existing samples) to increase variety without manual labeling.
