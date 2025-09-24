

import weaviate
import json
from langchain_community.vectorstores import Weaviate
from langchain.docstore.document import Document
from langchain_dashscope import DashScopeEmbeddings


    
client = weaviate.Client("http://localhost:8080")


def get_all_classes(client):
    """获取所有类"""
    print("\n1. 获取所有类：")
    try:
        schema = client.schema.get()
        classes = schema.get("classes", [])
        
        if not classes:
            print("   ❌ 没有找到任何类")
            return []
        
        print(f"   ✅ 找到 {len(classes)} 个类：")
        for i, class_info in enumerate(classes, 1):
            class_name = class_info.get("class", "Unknown")
            description = class_info.get("description", "No description")
            properties = class_info.get("properties", [])
            
            print(f"   {i}. 类名: {class_name}")
            print(f"      描述: {description}")
            print(f"      属性数量: {len(properties)}")
            
            # 显示属性列表
            if properties:
                print("      属性列表:")
                for prop in properties[:3]:  # 只显示前3个属性
                    prop_name = prop.get("name", "Unknown")
                    prop_type = prop.get("dataType", ["Unknown"])
                    print(f"        - {prop_name}: {prop_type}")
                if len(properties) > 3:
                    print(f"        ... 还有 {len(properties) - 3} 个属性")
            print()
        
        return [class_info["class"] for class_info in classes]
        
    except Exception as e:
        print(f"   ❌ 获取类信息失败: {e}")
        return []


if __name__ == "__main__":
    get_all_classes(client)