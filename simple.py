import datetime
from openai import OpenAI

# 定义系统要求的字符串常量
DECOMPOSE_SYSTEM = """SYSTEM:
You serve as an assistant that helps me play Minecraft.
...
"""

def get_formatted_today():
    """获取今天的日期，格式为'YYYY-MM-DD'"""
    return datetime.date.today().strftime("%Y-%m-%d")

def ask_perplexity(prompt):
    """向Perplexity API发送请求，并输出结果"""
    client = OpenAI(
        base_url="https://api.perplexity.ai",
        api_key="your_api_key_here",  # 应该使用配置文件或环境变量来管理API密钥
    )

    messages = [
        {"role": "system", "content": DECOMPOSE_SYSTEM},
        {"role": "user", "content": prompt},
    ]

    try:
        response = client.chat.completions.create(
            model="mixtral-8x7b-instruct",
            messages=messages,
        )
        answer = response.choices[0].message.content
        print(answer)
    except Exception as e:
        print(f"Error while asking Perplexity: {e}")

# 主程序入口
if __name__ == "__main__":
    # 示例提示
    example_prompt = "I want to build a house in Minecraft."
    ask_perplexity(example_prompt)