# 创建 /kaggle/working/ComfyUI/custom_nodes/symbol_to_prompt.py
import comfy.sd
from comfy.sd import CLIPTextEncode

class SymbolToPrompt:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "symbol_data": ("DICT",),
                "template": ("STRING", {
                    "multiline": True,
                    "default": "A {name} wearing {armor}, holding {weapon}, {texture} texture"
                })
            }
        }

    RETURN_TYPES = ("CONDITIONING",)
    RETURN_NAMES = ("conditioning",)
    FUNCTION = "convert"
    CATEGORY = "Symbol Processing"

    def convert(self, symbol_data, template):
        # 提取符号数据
        attributes = symbol_data.get("attributes", {})
        
        # 动态填充模板
        prompt = template.format(
            name=symbol_data.get("name", "character"),
            ​**attributes
        )
        
        # 调用原生CLIP编码器
        return CLIPTextEncode().encode(text=prompt)[0]

# 注册节点
NODE_CLASS_MAPPINGS = {"SymbolToPrompt": SymbolToPrompt}
NODE_DISPLAY_NAME_MAPPINGS = {"SymbolToPrompt": "🔣 Symbol → Prompt"}
