# 在全新单元格执行以下代码覆盖文件
%%writefile /kaggle/working/ComfyUI/custom_nodes/symbol_loader.py
# 保存为 /kaggle/working/ComfyUI/custom_nodes/symbol_loader.py
import json
import os
from pathlib import Path

class SymbolLoader:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "symbol_path": ("STRING", {"default": "characters/cyberpunk_warrior.json"})
            }
        }

    RETURN_TYPES = ("DICT",)
    FUNCTION = "load_symbol"

    def load_symbol(self, symbol_path):
        symbol_file = Path("/kaggle/working/ComfyUI/symbols") / symbol_path
        with open(symbol_file, 'r') as f:
            data = json.load(f)
        return (data,)
