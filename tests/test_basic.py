"""Tests for training pipeline"""
import pytest


def test_dataset_loader():
    """Test dataset loading"""
    from sovalune_training.datasets.loader import prepare_training_data
    
    examples = [
        {"input": "test", "output": "result"},
    ]
    
    prepared = prepare_training_data(examples)
    assert len(prepared) == 1
    assert prepared[0]["input"] == "test"
