import pandas as pd

# 加载 CSV
df = pd.read_csv("buffer_detect_val_mod_blank_sliced_deepseek.csv")

# # 查看 func_before 列的前几项

# print(df["func_before"].head())

import os

# 创建输出文件夹
output_dir = "output_c_files"
os.makedirs(output_dir, exist_ok=True)

# 遍历每一行，将 func_before 内容写入 .c 文件
for idx, func_code in enumerate(df["func_before"]):
    filename = os.path.join(output_dir, f"sample_{idx}.c")
    with open(filename, "w") as f:
        f.write("#include <stdio.h>\n\n")
        f.write(func_code)
        f.write("\n\nint main() {\n    return 0;\n}")
print(f"共生成 {idx + 1} 个 .c 文件，保存在 {output_dir}/")

