import os
from llama_cpp import Llama

# 요약 및 번역
def summarize_with_llm(papers):
    repo_id = "Qwen/Qwen3-1.7B-GGUF"
    file_name = "Qwen3-1.7B-Q8_0.gguf"

    settings = {
        "n_ctx": 2048,
        "n_batch": 512,
        "n_threads": 4,
        "n_gpu_layers": 0, # CPU 사용
        "verbose": False,
        "seed": -1,
        "f16_kv": True,
        "use_mlock": False,
        "use_mmap": True,
    }
    
    llm = Llama.from_pretrained(
        repo_id=repo_id,
        filename=file_name,
        **settings,
        chat_format = "qwen"
    )
    print("모델 로딩 완료")
    summarize = []
    SYSTEM_PROMPT = os.environ.get("SYSTEM_PROMPT")

    for idx, (key, content) in enumerate(papers.items(),1):
        title, link = key
        print("="*10, idx, title, "="*10)
        result = {
            "title": title,
            "link": link,
            "response": None
        }
        
        msg = [
            {"role": "system", "content":SYSTEM_PROMPT},
            {"role": "user", "content": f"Please read the following text and provide a one-sentence summary in Korean: {content}"}
        ]
        
        output = llm.create_chat_completion(
            messages = msg,
            max_tokens=1024,
            temperature=0.7,
            top_p=0.9,
            stream=False
        )

        response = output['choices'][0]['message']['content']

        print(response.split("</think>")[-1].strip())
        result["response"] = response.split("</think>")[-1].strip()
        summarize.append(result)
        print("summarize 개수", len(summarize))
    return summarize