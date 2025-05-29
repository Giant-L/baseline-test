import pandas as pd
import os

# 加载 CSV
df = pd.read_csv("buffer_detect_val_mod_blank_sliced_deepseek.csv")

# 创建输出文件夹
output_dir = "output_c_files"
os.makedirs(output_dir, exist_ok=True)

# 遍历每一行，将 func_before 内容写入 .cpp 文件
for idx, func_code in enumerate(df["func_before"]):
    filename = os.path.join(output_dir, f"sample_{idx}.cpp")
    with open(filename, "w") as f:
        f.write("#include <iostream>\n\n")  # 使用 C++ 的头文件
        f.write(func_code)
        f.write("\n\nint main() {\n    return 0;\n}")

print(f"共生成 {idx + 1} 个 .cpp 文件，保存在 {output_dir}/")