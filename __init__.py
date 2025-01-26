'''
    2025.1
    把此扩展包安装到  ComfyUI\custom_nodes 目录下
    使用方法:
        在工作流中添加此 AivParam 节点,不用连接任何输入和输出
        只要把工作流中需要输出的参数按照说明一一录入即可
'''

import os,sys
from .nodes.aivapp import AivParamNode
import nodes


NODE_CLASS_MAPPINGS = {
    "AivParam": AivParamNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AivParam": "Aiv Param"
}


WEB_DIRECTORY = "./js" # -- deprecated method
# nodes.EXTENSION_WEB_DIRS["ComfyUI-Aiv-Param"] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'js')
