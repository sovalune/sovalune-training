"""Artifact storage management"""
import json
from pathlib import Path
from typing import Optional


class ArtifactStore:
    """Manages training artifacts (adapters, metrics, etc.)."""
    
    def __init__(self, base_path: str = "./artifacts"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)
    
    def save_adapter(self, job_id: str, version: int, adapter_path: str) -> str:
        """Save adapter artifact.
        
        Args:
            job_id: Training job ID
            version: Artifact version
            adapter_path: Path to adapter files
            
        Returns:
            URI to saved artifact
        """
        artifact_dir = self.base_path / job_id / f"v{version}"
        artifact_dir.mkdir(parents=True, exist_ok=True)
        
        # TODO: Copy adapter files to artifact_dir
        
        return str(artifact_dir)
    
    def save_metrics(self, job_id: str, version: int, metrics: dict) -> str:
        """Save metrics artifact.
        
        Args:
            job_id: Training job ID
            version: Artifact version
            metrics: Metrics dictionary
            
        Returns:
            URI to saved metrics
        """
        artifact_dir = self.base_path / job_id / f"v{version}"
        artifact_dir.mkdir(parents=True, exist_ok=True)
        
        metrics_path = artifact_dir / "metrics.json"
        with open(metrics_path, "w") as f:
            json.dump(metrics, f, indent=2)
        
        return str(metrics_path)
    
    def load_metrics(self, job_id: str, version: int) -> Optional[dict]:
        """Load metrics from artifact.
        
        Args:
            job_id: Training job ID
            version: Artifact version
            
        Returns:
            Metrics dictionary or None
        """
        metrics_path = self.base_path / job_id / f"v{version}" / "metrics.json"
        
        if not metrics_path.exists():
            return None
        
        with open(metrics_path) as f:
            return json.load(f)
