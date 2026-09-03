"""Dataset loading and preparation"""
import json
from pathlib import Path
from typing import List, Dict


def load_dataset(uri: str) -> List[Dict]:
    """Load dataset from URI (file path or S3-like URI).
    
    Args:
        uri: Dataset URI
        
    Returns:
        List of examples
    """
    # TODO: Support S3 and other storage backends
    path = Path(uri)
    
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {uri}")
    
    with open(path) as f:
        data = json.load(f)
    
    return data


def prepare_training_data(examples: List[Dict]) -> List[Dict]:
    """Prepare examples for training.
    
    Args:
        examples: Raw examples
        
    Returns:
        Prepared examples
    """
    prepared = []
    
    for example in examples:
        # Format for instruction tuning
        prepared.append({
            "input": example.get("input", ""),
            "output": example.get("output", ""),
            "context": example.get("context", ""),
        })
    
    return prepared
