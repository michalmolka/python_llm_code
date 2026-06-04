# source /Users/m...a/Downloads/fine-tuning/.venv/bin/activate
# pip install mlx-lm
# MODEL CARD: https://huggingface.co/Qwen/Qwen3-4B-MLX-bf16/tree/main


# LORA TRAINING:
mlx_lm lora \
--model ./Qwen3-4B-MLX-bf16 \
--train \
--data ./data \
--fine-tune-type lora \
--adapter-path ./qwen3-4b-iowa-lora-v2/ \
--batch-size 1 \
--iters 4000 \
--learning-rate 2e-4 \
--num-layers 24 \
--mask-prompt \
--save-every 500 \
--max-seq-length 2048

# GENERATE RESPONSE:
mlx_lm generate \
--model ./Qwen3-4B-MLX-bf16 \
--adapter-path ./qwen3-4b-iowa-lora-v2 \
--prompt "What is the iowa_sales table?" \
--max-tokens 200


# CREATE TRAIN/VALID/TEST DATA:
head -n 2700 qwen3_iowa_multiturn_balanced.jsonl > train.jsonl 
sed -n '2701,2850p' qwen3_iowa_multiturn_balanced.jsonl > valid.jsonl
sed -n '2851,3000p' qwen3_iowa_multiturn_balanced.jsonl > test.jsonl 



# LORA TRAINING NEXT STEP:
mlx_lm lora \
--model ./Qwen3-4B-MLX-bf16 \
--train \
--data ./data \
--fine-tune-type lora \
--adapter-path ./qwen3-4b-iowa-lora-v2-relations \
--resume-adapter-file ./qwen3-4b-iowa-lora-v2/adapters.safetensors \
--batch-size 1 \
--iters 1200 \
--learning-rate 5e-5 \
--num-layers 8 \
--save-every 400 \
--max-seq-length 1024

# GENERATE RESPONSE:
mlx_lm generate \
  --model ./Qwen3-4B-MLX-bf16 \
  --adapter-path ./qwen3-4b-iowa-lora-v2-relations \
  --prompt "What relationships does the iowa_sales table contain?" \
  --max-tokens 300


# CHECK THE MODEL AND ADAPTER:
python -m mlx_lm.generate \
  --model ./Qwen3-4B-MLX-bf16 \
  --adapter-path ./qwen3-4b-iowa-lora-v2-relations \
  --prompt "What relationships does the iowa_sales table contain?" \
  --max-tokens 100

# RUN SERVER:
python -m mlx_lm.server \
  --model ./Qwen3-4B-MLX-bf16 \
  --adapter-path ./qwen3-4b-iowa-lora-v2-relations \
  --port 8000

# QUERY SERVER:
curl http://127.0.0.1:8000/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
  "model": "Qwen3-4B-MLX-bf16",
  "messages": [
    {"role": "user", "content": "What relationships does the iowa_sales table contain?"}
  ],
  "max_tokens": 100
}'