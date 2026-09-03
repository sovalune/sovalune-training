# Sovalune Training

Python training pipeline for Sovalune AI model fine-tuning.

## Overview

This package provides:
- NATS worker for receiving training jobs
- Adapter/LoRA fine-tuning
- Evaluation pipeline
- Artifact management

## Development

```bash
# Install
pip install -e ".[dev]"

# Run tests
pytest

# Lint
ruff check .
ruff format .
```

## Jobs

- `adapter_tune` - LoRA/adapter fine-tuning
- `eval_only` - Evaluation without weight modification
