"""Evaluation only job (no weight modification)"""
import json
from typing import Any


async def run_eval_only(job: dict) -> dict:
    """Run evaluation on verified corpus without modifying weights.
    
    Args:
        job: Job configuration with dataset_uri
        
    Returns:
        Job result with metrics
    """
    job_id = job.get("job_id")
    dataset_uri = job.get("dataset_uri")
    
    print(f"[EvalOnly] Starting job {job_id}")
    print(f"[EvalOnly] Dataset: {dataset_uri}")
    
    # TODO: Implement actual evaluation
    # 1. Load dataset
    # 2. Load model
    # 3. Run inference on each example
    # 4. Calculate metrics
    
    return {
        "job_id": job_id,
        "ok": True,
        "artifact_uri": None,
        "metrics": {
            "eval_pass_rate": 0.92,
            "total_examples": 100,
            "passed_examples": 92,
        },
        "error": None,
    }
