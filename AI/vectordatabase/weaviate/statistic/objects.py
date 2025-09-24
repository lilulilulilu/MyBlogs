

import weaviate
import json
from langchain_community.vectorstores import Weaviate
from langchain.docstore.document import Document
from langchain_dashscope import DashScopeEmbeddings


    
client = weaviate.Client("http://localhost:8080")

def query_all_objects_in_classes(client):
    """查询每个类中的所有对象"""
    print("\n2. 查询每个类中的所有对象：")
    
    try:
        # 获取所有类
        schema = client.schema.get()
        classes = schema.get("classes", [])
        
        for class_info in classes:
            class_name = class_info["class"]
            print(f"\n   查询类: {class_name}")
            
            try:
                # 查询所有对象
                result = client.query.get(class_name).do()
                objects = result.get("data", {}).get("Get", {}).get(class_name, [])
                
                print(f"   ✅ 找到 {len(objects)} 个对象")
                
                # 显示前几个对象的详细信息
                for i, obj in enumerate(objects[:3], 1):
                    print(f"   \n   对象 {i}:")
                    print(f"     UUID: {obj.get('_additional', {}).get('id', 'N/A')}")
                    
                    # 显示所有属性
                    for key, value in obj.items():
                        if key != "_additional":
                            if isinstance(value, str) and len(value) > 100:
                                value = value[:100] + "..."
                            print(f"     {key}: {value}")
                
                if len(objects) > 3:
                    print(f"   ... 还有 {len(objects) - 3} 个对象")
                    
            except Exception as e:
                print(f"   ❌ 查询类 {class_name} 失败: {e}")
                
    except Exception as e:
        print(f"   ❌ 查询所有对象失败: {e}")


if __name__ == "__main__":
    query_all_objects_in_classes(client)