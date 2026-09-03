"""NATS worker for training jobs"""
import asyncio
import json
import os
from typing import Optional

import nats


class NatsWorker:
    def __init__(self, nats_url: str = "nats://localhost:4222"):
        self.nats_url = nats_url
        self.nc: Optional[nats.Nats] = None

    async def connect(self):
        self.nc = await nats.connect(self.nats_url)
        print(f"[NATS] Connected to {self.nats_url}")

    async def subscribe_training_jobs(self, callback):
        if not self.nc:
            raise RuntimeError("Not connected to NATS")
        
        async def handler(msg):
            data = json.loads(msg.data.decode())
            print(f"[NATS] Received training job: {data.get('job_id')}")
            
            result = await callback(data)
            
            await msg.respond(json.dumps(result).encode())
        
        sub = await self.nc.subscribe("training.job.request", cb=handler)
        print("[NATS] Subscribed to training.job.request")
        return sub

    async def publish_result(self, result: dict):
        if not self.nc:
            raise RuntimeError("Not connected to NATS")
        
        await self.nc.publish("training.job.result", json.dumps(result).encode())
        print(f"[NATS] Published result for job: {result.get('job_id')}")

    async def close(self):
        if self.nc:
            await self.nc.close()
