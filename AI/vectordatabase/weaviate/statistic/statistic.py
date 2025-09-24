

import weaviate
import json
from langchain_community.vectorstores import Weaviate
from langchain.docstore.document import Document
from langchain_dashscope import DashScopeEmbeddings


client = weaviate.Client("http://localhost:8080")

def get_database_statistics(client):
    """获取数据库统计信息"""
    print("\n7. 数据库统计信息：")
    
    try:
        schema = client.schema.get()
        classes = schema.get("classes", [])
        
        total_objects = 0
        total_properties = 0
        
        print("   📊 详细统计:")
        for class_info in classes:
            class_name = class_info["class"]
            properties = class_info.get("properties", [])
            
            try:
                # 获取对象数量
                result = client.query.aggregate(class_name).with_meta_count().do()
                count = result.get("data", {}).get("Aggregate", {}).get(class_name, [{}])[0].get("meta", {}).get("count", 0)
                
                total_objects += count
                total_properties += len(properties)
                
                print(f"   {class_name}:")
                print(f"     对象数量: {count}")
                print(f"     属性数量: {len(properties)}")
                print(f"     向量索引: {class_info.get('vectorIndexConfig', {}).get('distance', 'N/A')}")
                
            except Exception as e:
                print(f"   ❌ 获取 {class_name} 统计失败: {e}")
        
        print(f"\n   📈 总计:")
        print(f"     总类数: {len(classes)}")
        print(f"     总对象数: {total_objects}")
        print(f"     总属性数: {total_properties}")
        
    except Exception as e:
        print(f"   ❌ 获取统计信息失败: {e}")


if __name__ == "__main__":
    get_database_statistics(client)