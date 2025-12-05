from pydantic import BaseModel, Field


# Step 1 — define a configuration model
class TrainConfig(BaseModel):
    dataset_path: str
    batch_size: int = Field(gt=0)
    learning_rate: float = Field(gt=0)
    epochs: int = Field(gt=0)
    optimizer: str = Field(pattern="^(adam|sgd|rmsprop)$")
    device: str = Field(default="cpu", pattern="^(cpu|cuda)$")


# Step 2 — define a function that uses those fields
def combine_info(dataset_path: str, batch_size: int, learning_rate: float,
                 epochs: int, optimizer: str, device: str) -> str:
    """Just a dummy function that concatenates stuff."""
    return (
        f"[{optimizer.upper()}] Training on {device} with {batch_size} batches, "
        f"learning_rate={learning_rate}, epochs={epochs}, data='{dataset_path}'"
    )


# Step 3 — create and validate config
cfg = TrainConfig(
    dataset_path="data/train.csv",
    batch_size="32",        # note: auto coerced str → int
    learning_rate=0.001,
    epochs=10,
    optimizer="adam",
    device="cuda",
)

cfg.model_dump()
print(cfg)
print(cfg.dataset_path)
breakpoint()

print("✅ Config validated:")
print(cfg)
print()

# Step 4 — use config directly in function with unpacking (**)
result = combine_info(**cfg.model_dump())

print("🚀 Function output:")
print(result)

