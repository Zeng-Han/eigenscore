import pickle

with open(
        "/mnt/f7a57ea9-f9b0-4806-966e-7f21cbc76421/zenghan/eigenscore_base/output/llama-7b-hf_coqa_0/0.pkl",
        "rb"
) as f:
    data = pickle.load(f)
    print(len(data))

pass
