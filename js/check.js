/**
 * 2025.1
 * 动态检测Aiv Param 节点的输入参数
 */
import {app} from "../../scripts/app.js"

// let inputEvent
app.registerExtension({
    name: 'AivApp',     //名字随便起
    nodeCreated(node, app){
        if (node.comfyClass == 'AivParam') {
            // console.log('初始化了 AivParam 监听函数, node==', node)
            
            // 获取输入文本框的 widget 元素
            const widget = node.widgets.find( item => item.name == 'text_param')
            if(widget){
                // 获取组件中的DOM原生元素,准备添加监听事件 2025.1
                const inputWidget = widget.element

                // if(inputEvent){
                //     inputWidget.removeEventListener('input', inputEvent)
                // }
                // // 监听输入文本框的变化
                // inputEvent = inputWidget.addEventListener('input', (event) => {
                //     const inputValue = event.target.value;
                //     console.log('输入框内容改变：', inputValue)
                //     // 检查输入是否为 JSON 格式
                //     if (isJson(inputValue)) {
                //         // 对 JSON 字符串进行格式化处理
                //         const formattedJson = formatJson(inputValue);
                //         // 更新输入文本框的值
                //         event.target.value = formattedJson;
                //     }
                // })

                // 重写了组件的 'value'属性的设置和获取方法 2025.1
                Object.defineProperty(widget, 'value', {
                    set: function (value) {

                        // console.log('设置了值! ==> ', value) 2025.1
                        // 要设置<textarea>组件显示内容前,前 '{' 和 '}' 字符串前的  '\\' 删除,这样在文本框中
                        // 用户看到的与json格式完全一至           
                        const cleanStr = value.replace(/\\([{}])/g, '$1');                     
                        inputWidget.value = cleanStr
                    },

                    get: function () {
                        // console.log('获取了值! ==> ', inputWidget.value)
                        // 在获取值之前 (一般是系统获取值后保存到 工作流中), 获取前先把 '{' 和 '}' 前面添加'\\'转义符 2025.1
                        // 这样就是正确的json格式, 以方便后面获取字符串后再用json.loads() 转为对象 , 原因是这些值是嵌套的嵌套
                        const cleanStr = formatJson(inputWidget.value)
                        // const cleanStr = inputWidget.value.replace(/\\([{}])/g, '$1');
                        return cleanStr

                    }
                })
            }         
            // console.log('初始化了 AivParam 监听函数, index= ', index)           
        }
    }
});


// 检查字符串是否为 JSON 格式
// function isJson(str) {
//     try {
//         JSON.parse(str);
//         return true;
//     } catch (e) {
//         return false;
//     }
// }

// 对 JSON 字符串进行格式化处理 2025.1
function formatJson(jsonStr) {
    // 替换 '{' 和 '}' 前添加转义符 '\'
    let formattedStr = jsonStr.replace(/{/g, '\\{');
    formattedStr = formattedStr.replace(/}/g, '\\}');
    return formattedStr;
}
