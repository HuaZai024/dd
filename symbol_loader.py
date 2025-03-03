# 保存为 /kaggle/working/ComfyUI/custom_nodes/comfyui-symbol-loader/symbol_loader.py
import json
from pathlib import Path
import comfy.sd # 关键依赖

class SymbolLoader:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "symbol_path": ("STRING", {"default": "characters/cyberpunk_warrior.json"})
            }
        }
    
    RETURN_TYPES = ("DICT",)
    RETURN_NAMES = ("symbol_data",)
    FUNCTION = "load_symbol"
    CATEGORY = "Custom Nodes/Symbols"  # 定义节点分类

    def load_symbol(self, symbol_path):
        symbol_file = Path("/kaggle/working/ComfyUI/symbols") / symbol_path
        with open(symbol_file, 'r', encoding='utf-8') as f:
            return (json.load(f),)

# 关键：注册节点到 ComfyUI
NODE_CLASS_MAPPINGS = {
    "SymbolLoader": SymbolLoader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SymbolLoader": "🔣 Symbol Loader"
}
