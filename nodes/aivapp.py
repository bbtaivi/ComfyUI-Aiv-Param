# 把本模块py代码放到ComfyUI项目的 ComfyUI/custom_nodes 才能正确导入 2025.1
from comfy.comfy_types import IO

class AivParamNode:
    @classmethod
    def INPUT_TYPES(s):
        # "text" 组件中是用户需要输入的参数列表 2025.1
        # "note" 是使用说明示例
        # 字符串顶格设置是为了在js端从<textarea>元素左侧显示
        return {
                "required": {
                    "text_param": (IO.STRING, {"multiline": True, "dynamicPrompts": True, "tooltip": "<请在此输入需要输出的参数设置(json格式)>",
                                "default": 
r'''[
    {"id": 18, "name": "clip", "title": "这是参数例子, 详情参考下面的说明","default":"一个漂亮的女孩", "option": {"type": "text", "multi": true, "tooltip": "请在此输入提示词(中文)"} }
]
'''
                                   
                }),
                    "text_note": (IO.STRING, {"multiline": True, "dynamicPrompts": True, "tooltip": "这是使用说明", 
                            "default": 
r'''
    上面输入框填写格式: json格式数组,每个参数一个对象元素,之间用豆号","分隔, 参考如下: 
    [
        {"id": 18, "name": "clip", "title": "提示词", "option": {"type": "text", "multi": true, "tooltip": "请在此输入提示词内容(中文)"} },
        {"id": 30, "name": "seed", "title": "种子", "default": 512356789158, "option": {"type": "seed"} },
        {"id": 21, "name": "steps", "title": "步数", "option": {"type": "number", "step": 1, "min": 1, "max": 100} },
        {"id": 21, "name": "enabled", "title": "启用", "default": true, "option": {"type": "bool", "tooltip": "开启人脸增强效果"} },
        {"id": 25, "name": "model", "title": "模型", "default": "GFPGANv1.4.pth", "order": 10, "option": {"type": "combo", "values": ["GFPGANv1.3.pth", "GFPGANv1.4.pth","GPEN-BFR-512.onnx"]} },
        {"id": 117, "name": "image", "title": "头像", "required": true, "option": {"type": "file"} }
    ]

    注意事项：
        - 每个工作流只能有一个 Aiv Param 节点;
        - 注意检查 json 格式是否正确, 可以使用在线网站检测;
        - 参数设置中,必需字段是"id"、"name",其它可选,默认是'text'类型, "id"对应ComfyUI节点的序列号(如果不知道如何显示ComfyUI节点序列中,请上网查询),"name"是节点的参数名(如果不知道参数名,可以先保存为json,再打开看);
        - 参数设置尽量指定参数类型,支持的类型有: "text"、"number"、"bool"、"seed"(种子)、"combo"(下拉框)、"file"(打开文件)等, "option"字段可以设置数据类型的一些属性;
        - "order"字段对参数排序显示,大值排前面(不填默认为10); "required"标识是否必填参数,未设置默认为true;
        - 设计好工作流后,使用ComfyUI的 Workflow -> Export(API) 菜单把工作流导出为API格式文件,在AIV平台写py代码调用json文件即可;
'''
                    })
                
                }
        }

    RETURN_TYPES = ()
    FUNCTION = "execute"

    CATEGORY = "utils"  # 默认放在 "utils" 分组下

    def execute(self):
        # py服务器端无需执行代码 (这个组件只是在js端对用户输入进行格式化处理, 文件./js/check.js 中处理) 2025.1
        pass
