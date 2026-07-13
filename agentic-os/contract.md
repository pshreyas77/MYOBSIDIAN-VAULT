# Agentic OS Contract — Machine-Readable Interfaces

**Version:** 1.0  
**Compliance:** All scripts MUST conform to these schemas. `verify-contract.sh` enforces.

---

## 1. Work Item Schema (triage output → conduct input)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["id", "tier", "spec", "budget_tokens", "budget_usd", "created_at"],
  "properties": {
    "id": { "type": "string", "pattern": "^[a-z0-9-]{8,}$" },
    "tier": { "type": "string", "enum": ["auto", "queue", "watch", "reject"] },
    "spec": {
      "type": "object",
      "required": ["goal", "success_criteria", "constraints"],
      "properties": {
        "goal": { "type": "string", "minLength": 10 },
        "success_criteria": {
          "type": "array",
          "minItems": 1,
          "items": { "type": "string", "minLength": 5 }
        },
        "constraints": {
          "type": "array",
          "items": { "type": "string" }
        },
        "context_files": {
          "type": "array",
          "items": { "type": "string", "pattern": "^[./a-zA-Z0-9_-]+$" }
        }
      }
    },
    "budget_tokens": { "type": "integer", "minimum": 1000, "maximum": 500000 },
    "budget_usd": { "type": "number", "minimum": 0.001, "maximum": 5.0 },
    "created_at": { "type": "string", "format": "date-time" },
    "parent_id": { "type": ["string", "null"], "pattern": "^[a-z0-9-]{8,}$" }
  },
  "additionalProperties": false
}
```

**File:** `workers/<id>/work.json` (written by triage, read by conduct)

---

## 2. Plan Schema (conduct output → execute input)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["work_id", "steps", "checkpoints", "estimated_tokens", "estimated_usd"],
  "properties": {
    "work_id": { "type": "string", "pattern": "^[a-z0-9-]{8,}$" },
    "steps": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["name", "command", "verify_script", "max_tokens", "max_usd"],
        "properties": {
          "name": { "type": "string", "pattern": "^[a-z-]+$" },
          "command": { "type": "string", "minLength": 5 },
          "verify_script": { "type": "string", "pattern": "^verify-[a-z-]+\\.sh$" },
          "max_tokens": { "type": "integer", "minimum": 500 },
          "max_usd": { "type": "number", "minimum": 0.001 },
          "depends_on": { "type": "array", "items": { "type": "string" } }
        },
        "additionalProperties": false
      }
    },
    "checkpoints": {
      "type": "array",
      "items": { "type": "string", "pattern": "^[a-z-]+$" }
    },
    "estimated_tokens": { "type": "integer", "minimum": 1000 },
    "estimated_usd": { "type": "number", "minimum": 0.001 },
    "created_at": { "type": "string", "format": "date-time" }
  },
  "additionalProperties": false
}
```

**File:** `workers/<id>/plan.json` (written by conduct, read by execute & verify)

---

## 3. Execution Result Schema (execute output → verify input)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["work_id", "step_results", "artifacts", "token_usage", "usd_cost", "completed_at"],
  "properties": {
    "work_id": { "type": "string", "pattern": "^[a-z0-9-]{8,}$" },
    "step_results": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["step_name", "exit_code", "stdout", "stderr", "duration_ms"],
        "properties": {
          "step_name": { "type": "string" },
          "exit_code": { "type": "integer" },
          "stdout": { "type": "string" },
          "stderr": { "type": "string" },
          "duration_ms": { "type": "integer", "minimum": 0 }
        }
      }
    },
    "artifacts": {
      "type": "array",
      "items": { "type": "string", "pattern": "^workers/[a-z0-9-]+/.+" }
    },
    "token_usage": { "type": "integer", "minimum": 0 },
    "usd_cost": { "type": "number", "minimum": 0 },
    "completed_at": { "type": "string", "format": "date-time" }
  },
  "additionalProperties": false
}
```

**File:** `workers/<id>/result.json` (written by execute, read by verify)

---

## 4. Verification Result Schema (verify output → gate input)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["work_id", "overall", "checks", "evidence", "verified_at"],
  "properties": {
    "work_id": { "type": "string", "pattern": "^[a-z0-9-]{8,}$" },
    "overall": { "type": "string", "enum": ["PASS", "FAIL"] },
    "checks": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "result", "evidence"],
        "properties": {
          "name": { "type": "string" },
          "result": { "type": "string", "enum": ["PASS", "FAIL", "SKIP"] },
          "evidence": { "type": "string" },
          "details": { "type": "string" }
        }
      }
    },
    "evidence": {
      "type": "array",
      "items": { "type": "string", "pattern": "^workers/[a-z0-9-]+/.+" }
    },
    "verified_at": { "type": "string", "format": "date-time" }
  },
  "additionalProperties": false
}
```

**File:** `workers/<id>/verify.json` (written by verify, read by gate)

---

## 5. Trust Ledger Entry (append-only, one per gate decision)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["timestamp", "worker_id", "work_id", "previous_tier", "new_tier", "reason", "verify_hash"],
  "properties": {
    "timestamp": { "type": "string", "format": "date-time" },
    "worker_id": { "type": "string", "pattern": "^[a-z0-9-]{8,}$" },
    "work_id": { "type": "string", "pattern": "^[a-z0-9-]{8,}$" },
    "previous_tier": { "type": "string", "enum": ["auto", "queue", "watch", "reject", "new"] },
    "new_tier": { "type": "string", "enum": ["auto", "queue", "watch", "reject"] },
    "reason": { "type": "string", "enum": ["promotion", "demotion", "initial", "manual"] },
    "verify_hash": { "type": "string", "pattern": "^[a-f0-9]{64}$" }
  },
  "additionalProperties": false
}
```

**File:** `trust/ledger.jsonl` (one line per entry, append-only)

---

## 6. Goal Spec Schema (goals/<id>/spec.md + verify.sh)

**spec.md (markdown with required frontmatter):**
```yaml
---
id: "goal-slug"
title: "Human-readable title"
cadence: "daily|weekly|event"
min_tier: "auto|queue|watch"
success_metric: "machine-checkable description"
---
```

**verify.sh:** Must exit 0 on success, non-zero on failure. Output JSON to stdout:
```json
{ "goal_id": "goal-slug", "status": "PASS|FAIL", "metric_value": 42, "threshold": 40, "details": "..." }
```

---

## 7. Budget Usage Entry (append-only)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["timestamp", "work_id", "worker_id", "tier", "tokens_in", "tokens_out", "usd_cost", "daily_total_tokens", "daily_total_usd"],
  "properties": {
    "timestamp": { "type": "string", "format": "date-time" },
    "work_id": { "type": "string" },
    "worker_id": { "type": "string" },
    "tier": { "type": "string", "enum": ["auto", "queue", "watch"] },
    "tokens_in": { "type": "integer", "minimum": 0 },
    "tokens_out": { "type": "integer", "minimum": 0 },
    "usd_cost": { "type": "number", "minimum": 0 },
    "daily_total_tokens": { "type": "integer", "minimum": 0 },
    "daily_total_usd": { "type": "number", "minimum": 0 }
  }
}
```

**File:** `budget/usage.jsonl` (one line per run)

---

## 8. Script Interface Contracts

### triage.sh
```
Input:  (none - reads from inbox/sources)
Output: workers/<id>/work.json (validates against schema #1)
Exit:   0 = work found, 1 = no work, 2 = error
```

### conduct.sh
```
Input:  workers/<id>/work.json
Output: workers/<id>/plan.json (validates against schema #2)
Exit:   0 = plan created, 1 = invalid work, 2 = cannot plan
```

### verify-plan.sh
```
Input:  workers/<id>/plan.json
Output: (stdout: PASS/FAIL, stderr: details)
Exit:   0 = valid plan, 1 = invalid plan
```

### execute.sh
```
Input:  workers/<id>/plan.json
Output: workers/<id>/result.json (validates against schema #3)
Exit:   0 = completed, 1 = step failed, 2 = budget exceeded, 3 = error
```

### verify.sh
```
Input:  workers/<id>/work.json, workers/<id>/plan.json, workers/<id>/result.json
Output: workers/<id>/verify.json (validates against schema #4)
Exit:   0 = PASS, 1 = FAIL, 2 = error
```

### gate.sh
```
Input:  workers/<id>/work.json, workers/<id>/verify.json
Output: Appends to trust/ledger.jsonl (schema #5)
Exit:   0 = updated, 1 = error
```

### budget/per-run.sh
```
Input:  (env: TIER, ESTIMATED_TOKENS, ESTIMATED_USD)
Output: (stdout: remaining budget, stderr: warning if >80%)
Exit:   0 = within budget, 42 = budget exceeded
```

### budget/daily.sh
```
Input:  (arg: check|reset)
Output: (stdout: daily totals)
Exit:   0 = under cap, 42 = cap exceeded
```

---

## 9. Validation Commands

```bash
# Validate work.json against schema
jsonschema -i workers/<id>/work.json schemas/work.schema.json

# Validate plan.json against schema
jsonschema -i workers/<id>/plan.json schemas/plan.schema.json

# Validate all contracts
make verify-contracts
```

---

## 10. Forbidden Output Patterns (auto-fail in verify)

Any script outputting these patterns to stdout/stderr **fails verification**:
- `I (verified|checked|confirmed|ensured)`
- `comprehensive|thorough|complete` (without metrics)
- `no issues|everything (looks|is) (good|fine|ok)`
- `successfully` (without evidence file path)

**Rationale:** These are self-evaluation signals. Evidence must be artifacts, not claims.